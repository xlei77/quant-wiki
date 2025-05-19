#!/usr/bin/env python3
"""
Quant Wiki Markdown Translation Script (Using Anthropic Claude API and asyncio)

This script translates all Markdown files in a directory from Chinese to English
using the Anthropic Claude API, with asyncio for rate-limited concurrency.

Usage:
    python translate_claude_async.py --api_key YOUR_ANTHROPIC_API_KEY [--input_dir INPUT_DIR]
        [--output_dir OUTPUT_DIR] [--translate_filenames] [--model MODEL_NAME]

Requirements:
    pip install anthropic python-frontmatter tqdm
"""
import argparse
import asyncio
import os
import re
import logging
from functools import partial
from pathlib import Path

import frontmatter
from anthropic import Anthropic
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # set to DEBUG for detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# Concurrency ceiling for API calls
API_CONCURRENCY = 5
semaphore = asyncio.Semaphore(API_CONCURRENCY)

# Section header to skip entirely (preserve original)
SKIP_SECTION_HEADER = "## 关于LLMQuant"

async def translate_text_async(text, anthropic_client, model="claude-3-5-sonnet-20241022",
                               src_lang='Chinese', dest_lang='English'):
    if not text or not text.strip():
        logger.debug("Empty or whitespace-only text, skipping translation.")
        return text

    prompt = (
        f"""Translate the following text from {src_lang} to {dest_lang}.
        This text is from a quantitative finance wiki, so please maintain technical accuracy.
        Preserve all markdown formatting, math expressions, and code elements, and ensure every detail is retained.
        Ensure the translation is natural, clear, and maintains the technical precision required for financial documentation:

        {text}

        Output only the translated text.
        """
    )
    logger.debug(f"Requesting translation for text chunk of length {len(text)}.")

    async with semaphore:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            partial(
                anthropic_client.messages.create,
                model=model,
                max_tokens=4000,
                temperature=0.0,
                system="You are a professional translator specializing in financial and technical content. Translate precisely while maintaining all formatting.",
                messages=[{"role": "user", "content": prompt}]
            )
        )
        # Spread out requests to avoid bursts
        await asyncio.sleep(0.5)
        translated = response.content[0].text
        logger.debug(f"Received translated chunk of length {len(translated)}.")
        return translated


def chunk_text(text):
    """
    Split text into chunks at Markdown headers (lines starting with #).
    This honors natural section boundaries for better context.
    """
    lines = text.split('\n')
    chunks = []
    current = []
    header_pattern = re.compile(r'^#{1,6}\s')
    for line in lines:
        if header_pattern.match(line) and current:
            chunks.append("\n".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append("\n".join(current))
    logger.debug(f"Split content into {len(chunks)} section-based chunks.")
    return chunks


def should_translate_chunk(chunk):
    if not chunk.strip():
        return False
    stripped = chunk.strip()
    if stripped.startswith('```') and stripped.endswith('```'):
        return False
    if re.match(r'^!\[.*\]\(.*\)$', stripped):
        return False
    if re.match(r'^\[.*\]\(.*\)$', stripped):
        return False
    return True

async def translate_md_content_async(content, anthropic_client, model):
    logger.debug("Starting markdown content translation.")
    # Preserve code blocks
    code_blocks = []
    code_pattern = r'```[^\n]*\n(.*?)```'
    content_ = content
    for match in re.finditer(code_pattern, content, re.DOTALL):
        block = match.group(0)
        placeholder = f"CODE_BLOCK_{len(code_blocks)}"
        code_blocks.append(block)
        content_ = content_.replace(block, placeholder)

    # Preserve inline code
    inline_codes = []
    inline_pattern = r'`([^`]+)`'
    for match in re.finditer(inline_pattern, content_):
        ic = match.group(0)
        placeholder = f"INLINE_CODE_{len(inline_codes)}"
        inline_codes.append(ic)
        content_ = content_.replace(ic, placeholder)

    # Preserve math expressions
    math_exprs = []
    math_pattern = r'\$\$(.*?)\$\$|\$(.*?)\$'
    for match in re.finditer(math_pattern, content_, re.DOTALL):
        expr = match.group(0)
        placeholder = f"MATH_EXPR_{len(math_exprs)}"
        math_exprs.append(expr)
        content_ = content_.replace(expr, placeholder)

    # Split on section boundaries
    chunks = chunk_text(content_)
    tasks = []
    for chunk in chunks:
        if chunk.strip().startswith(SKIP_SECTION_HEADER):
            logger.info(f"Skipping special section: {SKIP_SECTION_HEADER}")
            tasks.append(asyncio.sleep(0, result=chunk))
        elif should_translate_chunk(chunk):
            tasks.append(translate_text_async(chunk, anthropic_client, model))
        else:
            tasks.append(asyncio.sleep(0, result=chunk))

    # Preserve order by gathering
    translated_chunks = await asyncio.gather(*tasks)
    translated = "\n\n".join(translated_chunks)

    # Restore placeholders
    for i, expr in enumerate(math_exprs):
        translated = translated.replace(f"MATH_EXPR_{i}", expr)
    for i, ic in enumerate(inline_codes):
        translated = translated.replace(f"INLINE_CODE_{i}", ic)
    for i, block in enumerate(code_blocks):
        translated = translated.replace(f"CODE_BLOCK_{i}", block)

    logger.debug("Finished markdown content translation.")
    return translated

async def translate_frontmatter_async(metadata, anthropic_client, model):
    logger.debug(f"Translating {len(metadata)} frontmatter items.")
    translated = {}
    for key, value in metadata.items():
        if isinstance(value, str):
            translated[key] = await translate_text_async(value, anthropic_client, model)
        elif isinstance(value, list):
            sub = []
            for item in value:
                if isinstance(item, str):
                    sub.append(await translate_text_async(item, anthropic_client, model))
                else:
                    sub.append(item)
            translated[key] = sub
        else:
            translated[key] = value
    logger.debug("Finished frontmatter translation.")
    return translated

async def translate_filename_async(filename, anthropic_client, model):
    logger.debug(f"Translating filename: {filename}")
    name, ext = os.path.splitext(filename)
    translated_name = await translate_text_async(name, anthropic_client, model)
    translated_name = re.sub(r'[^\w\-]', '_', translated_name)
    translated_name = re.sub(r'_{2,}', '_', translated_name)
    result = f"{translated_name}{ext}"
    logger.debug(f"Translated filename to: {result}")
    return result

async def translate_md_file_async(input_path, output_path, anthropic_client, model, translate_filenames):
    if os.path.exists(output_path):
        logger.debug(f"Skipping existing file: {output_path}")
        return
    logger.info(f"Translating file: {input_path}")
    post = frontmatter.load(input_path)

    # Translate frontmatter and content
    meta = await translate_frontmatter_async(post.metadata, anthropic_client, model)
    content = await translate_md_content_async(post.content, anthropic_client, model)

    out_post = frontmatter.Post(content, **meta)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(out_post))
    logger.info(f"Finished file: {input_path}")

async def process_directory_async(input_dir, output_dir, anthropic_client, model, translate_filenames):
    input_path = Path(input_dir)
    md_files = list(input_path.rglob('*.md'))
    logger.info(f"Found {len(md_files)} Markdown files to process.")
    for md in tqdm(md_files, desc="Processing files", unit="file"):
        rel = md.relative_to(input_path)
        if translate_filenames:
            parts = []
            for part in rel.parts:
                if part.endswith('.md'):
                    newp = await translate_filename_async(part, anthropic_client, model)
                else:
                    newp = re.sub(r'[^\w\-]', '_',
                                  await translate_text_async(part, anthropic_client, model))
                parts.append(newp)
            out = os.path.join(output_dir, *parts)
        else:
            out = os.path.join(output_dir, rel)
        await translate_md_file_async(str(md), out, anthropic_client, model, translate_filenames)

async def translate_mkdocs_yml_async(input_path, output_path, anthropic_client, model):
    if not os.path.exists(input_path):
        return
    logger.info(f"Translating mkdocs.yml: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    prompt = """
        Translate the following YAML configuration file for a MkDocs site from Chinese to English.
        Focus only on translating user-visible text content (like titles, site name, descriptions),
        not keys or structural elements. Preserve all markdown file paths, formatting, and YAML syntax.

        Here's the content:

    """
    async with semaphore:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            partial(
                anthropic_client.messages.create,
                model=model,
                max_tokens=4000,
                temperature=0.0,
                system="Expert YAML translator. Do not alter keys or structure.",
                messages=[{"role": "user", "content": prompt + content}]
            )
        )
        await asyncio.sleep(0.5)
        translated = response.content[0].text
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    logger.info(f"Finished mkdocs.yml: {input_path}")

async def main_async():
    parser = argparse.ArgumentParser(
        description="Translate Markdown files from Chinese to English using Anthropic Claude with asyncio"
    )
    parser.add_argument('--api_key', required=True, help="Anthropic API key")
    parser.add_argument('--input_dir', default='./docs', help="Source directory (default: .)")
    parser.add_argument('--output_dir', default='./translated', help="Output directory")
    parser.add_argument('--translate_filenames', action='store_true',
                        help="Also translate directory and file names")
    parser.add_argument('--model', default='claude-3-5-sonnet-20241022',
                        help="Claude model to use")
    args = parser.parse_args()

    client = Anthropic(api_key=args.api_key)
    os.makedirs(args.output_dir, exist_ok=True)

    # Translate mkdocs.yml if present
    await translate_mkdocs_yml_async(
        os.path.join(args.input_dir, 'mkdocs.yml'),
        os.path.join(args.output_dir, 'mkdocs.yml'),
        client, args.model
    )

    # Process all Markdown files
    await process_directory_async(
        args.input_dir, args.output_dir, client, args.model, args.translate_filenames
    )

    logger.info("Translation complete")

if __name__ == "__main__":
    asyncio.run(main_async())
