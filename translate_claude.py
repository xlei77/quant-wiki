#!/usr/bin/env python3
"""
Quant Wiki Markdown Translation Script (Using Anthropic Claude API)

This script translates all Markdown files in a directory from Chinese to English
using the Anthropic Claude API, which provides high-quality translations especially
for technical content in quantitative finance.

Usage:
    python translate_claude.py --api_key YOUR_ANTHROPIC_API_KEY [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR] [--translate_filenames] [--model MODEL_NAME]

Requirements:
    pip install anthropic python-frontmatter tqdm
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path
import frontmatter
import logging
from anthropic import Anthropic
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

def translate_text(text, anthropic_client, model="claude-3-5-sonnet-20241022", src_lang='Chinese', dest_lang='English'):
    """
    Translate text using Anthropic Claude API.
    
    Args:
        text: Text to translate
        anthropic_client: Anthropic API client
        model: Claude model to use (default: "claude-3-5-sonnet-20241022")
        src_lang: Source language (default: 'Chinese')
        dest_lang: Destination language (default: 'English')
        
    Returns:
        Translated text or original text if translation fails
    """
    if not text or not text.strip():
        return text
    
    try:
        # Create the prompt for translation
        prompt = f"""Translate the following text from {src_lang} to {dest_lang}. 
        This text is from a quantitative finance wiki, so please maintain technical accuracy.
        Preserve all markdown formatting, math expressions, and code elements.
        Ensure the translation is natural, clear, and maintains the technical precision required for financial documentation:

        {text}
        """
        
        # Make the API call for translation
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=4000,
            temperature=0.1,  # Lower temperature for more consistent translations
            system="You are a professional translator specializing in financial and technical content. Translate precisely while maintaining all formatting.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the translated text
        translated_text = response.content[0].text
        
        # Add a slight delay to avoid hitting API rate limits
        time.sleep(0.5)
        
        return translated_text
    except Exception as e:
        logger.error(f"Translation error: {e}")
        logger.error(f"Failed to translate: {text[:100]}...")
        return text

def chunk_text(text, max_chunk_size=3000):
    """
    Split text into chunks to avoid exceeding API limits.
    
    Args:
        text: Text to split
        max_chunk_size: Maximum size of each chunk in characters
        
    Returns:
        List of text chunks
    """
    # Split by paragraphs first
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        # If adding this paragraph would exceed the max chunk size, 
        # start a new chunk (unless the current chunk is empty)
        if current_chunk and len(current_chunk) + len(paragraph) > max_chunk_size:
            chunks.append(current_chunk)
            current_chunk = paragraph
        else:
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph
    
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def should_translate_chunk(chunk):
    """
    Determine if a chunk should be translated or kept as is.
    
    Args:
        chunk: Text chunk to check
        
    Returns:
        Boolean indicating whether the chunk should be translated
    """
    # Skip empty chunks
    if not chunk.strip():
        return False
    
    # Skip chunks that are entirely code blocks
    if chunk.strip().startswith('```') and chunk.strip().endswith('```'):
        return False
    
    # Skip chunks that are just URLs or image references
    if re.match(r'^!\[.*\]\(.*\)$', chunk.strip()) or re.match(r'^\[.*\]\(.*\)$', chunk.strip()):
        return False
    
    return True

def translate_md_content(content, anthropic_client, model):
    """
    Translate Markdown content from Chinese to English using Anthropic Claude API.
    
    Args:
        content: Markdown content to translate
        anthropic_client: Anthropic API client
        model: Claude model to use
        
    Returns:
        Translated Markdown content
    """
    # Extract code blocks to preserve them
    code_blocks = []
    content_without_code = content
    
    # Find all code blocks and replace them with placeholders
    code_block_pattern = r'```[^\n]*\n(.*?)```'
    for match in re.finditer(code_block_pattern, content, re.DOTALL):
        code_block = match.group(0)
        placeholder = f"CODE_BLOCK_{len(code_blocks)}"
        code_blocks.append(code_block)
        content_without_code = content_without_code.replace(code_block, placeholder)
    
    # Also preserve inline code
    inline_codes = []
    inline_code_pattern = r'`([^`]+)`'
    for match in re.finditer(inline_code_pattern, content_without_code):
        inline_code = match.group(0)
        placeholder = f"INLINE_CODE_{len(inline_codes)}"
        inline_codes.append(inline_code)
        content_without_code = content_without_code.replace(inline_code, placeholder)
    
    # Also preserve math expressions
    math_expressions = []
    math_pattern = r'\$\$(.*?)\$\$|\$(.*?)\$'
    for match in re.finditer(math_pattern, content_without_code, re.DOTALL):
        math_expr = match.group(0)
        placeholder = f"MATH_EXPR_{len(math_expressions)}"
        math_expressions.append(math_expr)
        content_without_code = content_without_code.replace(math_expr, placeholder)
    
    # Split the content into chunks
    chunks = chunk_text(content_without_code)
    translated_chunks = []
    
    # Add progress bar for chunk translation
    with tqdm(total=len(chunks), desc="Translating chunks", leave=False) as pbar:
        for chunk in chunks:
            if should_translate_chunk(chunk):
                translated_chunk = translate_text(chunk, anthropic_client, model)
                translated_chunks.append(translated_chunk)
            else:
                translated_chunks.append(chunk)
            pbar.update(1)
    
    # Combine the translated chunks
    translated_content = '\n\n'.join(translated_chunks)
    
    # Replace math expression placeholders with original math expressions
    for i, math_expr in enumerate(math_expressions):
        placeholder = f"MATH_EXPR_{i}"
        translated_content = translated_content.replace(placeholder, math_expr)
    
    # Replace inline code placeholders with original inline codes
    for i, inline_code in enumerate(inline_codes):
        placeholder = f"INLINE_CODE_{i}"
        translated_content = translated_content.replace(placeholder, inline_code)
    
    # Replace code block placeholders with original code blocks
    for i, code_block in enumerate(code_blocks):
        placeholder = f"CODE_BLOCK_{i}"
        translated_content = translated_content.replace(placeholder, code_block)
    
    return translated_content

def translate_frontmatter(metadata, anthropic_client, model):
    """
    Translate frontmatter metadata using Anthropic Claude API.
    
    Args:
        metadata: Dictionary of frontmatter metadata
        anthropic_client: Anthropic API client
        model: Claude model to use
        
    Returns:
        Dictionary with translated metadata
    """
    translated_metadata = {}
    
    # Add progress bar for frontmatter translation
    with tqdm(total=len(metadata), desc="Translating frontmatter", leave=False) as pbar:
        for key, value in metadata.items():
            # Translate string values
            if isinstance(value, str):
                translated_metadata[key] = translate_text(value, anthropic_client, model)
            elif isinstance(value, list):
                # Translate list items
                translated_metadata[key] = [
                    translate_text(item, anthropic_client, model) if isinstance(item, str) else item
                    for item in value
                ]
            else:
                # Keep other types unchanged
                translated_metadata[key] = value
            pbar.update(1)
    
    return translated_metadata

def translate_md_file(input_path, output_path, anthropic_client, model):
    """
    Translate a single Markdown file using Anthropic Claude API.
    
    Args:
        input_path: Path to the input file
        output_path: Path to the output file
        anthropic_client: Anthropic API client
        model: Claude model to use
    """
    try:
        # Check if the input file exists
        if os.path.exists(output_path):
            logger.warning(f"Output file {output_path} already exists. Skipping translation.")
            return
        logger.info(f"Translating {input_path} to {output_path}")
        
        # Read the file
        post = frontmatter.load(input_path)
        
        # Translate frontmatter
        translated_metadata = translate_frontmatter(post.metadata, anthropic_client, model)
        
        # Translate content
        translated_content = translate_md_content(post.content, anthropic_client, model)
        
        # Create a new frontmatter post
        translated_post = frontmatter.Post(translated_content, **translated_metadata)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the translated file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(translated_post))
            
        logger.info(f"Successfully translated {input_path}")
    except Exception as e:
        logger.error(f"Error translating {input_path}: {e}")

def translate_filename(filename, anthropic_client, model):
    """
    Translate a filename from Chinese to English using Anthropic Claude API.
    
    Args:
        filename: Filename to translate
        anthropic_client: Anthropic API client
        model: Claude model to use
        
    Returns:
        Translated filename
    """
    # Split the filename into name and extension
    name, ext = os.path.splitext(filename)
    
    # Translate the name part
    translated_name = translate_text(name, anthropic_client, model)
    
    # Clean up the translated name (remove spaces, special characters)
    translated_name = re.sub(r'[^\w\-]', '_', translated_name)
    translated_name = re.sub(r'_{2,}', '_', translated_name)
    
    # Combine the translated name with the original extension
    return f"{translated_name}{ext}"

def process_directory(input_dir, output_dir, anthropic_client, model, translate_filenames=False):
    """
    Process all Markdown files in a directory using Anthropic Claude API.
    
    Args:
        input_dir: Input directory path
        output_dir: Output directory path
        anthropic_client: Anthropic API client
        model: Claude model to use
        translate_filenames: Whether to translate filenames
    """
    # Get all markdown files recursively
    input_dir_path = Path(input_dir)
    md_files = list(input_dir_path.glob('**/*.md'))
    
    logger.info(f"Found {len(md_files)} Markdown files to translate")
    
    # Group files by directory for better progress tracking
    files_by_dir = {}
    for input_path in md_files:
        parent_dir = input_path.parent.relative_to(input_dir_path) if input_path.parent != input_dir_path else Path('.')
        if parent_dir not in files_by_dir:
            files_by_dir[parent_dir] = []
        files_by_dir[parent_dir].append(input_path)
    
    # Process files directory by directory with progress bars
    for dir_path, dir_files in tqdm(files_by_dir.items(), desc="Processing directories", unit="dir"):
        dir_desc = str(dir_path) if str(dir_path) != '.' else 'root'
        logger.info(f"Processing directory: {dir_desc} ({len(dir_files)} files)")
        
        for input_path in tqdm(dir_files, desc=f"Files in {dir_desc}", unit="file", leave=False):
            # Get the relative path from the input directory
            rel_path = input_path.relative_to(input_dir_path)
            
            # Translate the filename if requested
            if translate_filenames:
                # Translate each part of the path
                translated_parts = []
                for part in rel_path.parts:
                    if part.endswith('.md'):
                        translated_parts.append(translate_filename(part, anthropic_client, model))
                    else:
                        translated_part = translate_text(part, anthropic_client, model)
                        translated_part = re.sub(r'[^\w\-]', '_', translated_part)
                        translated_parts.append(translated_part)
                
                output_path = os.path.join(output_dir, *translated_parts)
            else:
                output_path = os.path.join(output_dir, rel_path)
            
            # Translate the file
            translate_md_file(input_path, output_path, anthropic_client, model)

def translate_mkdocs_yml(input_path, output_path, anthropic_client, model):
    """
    Translate the mkdocs.yml file using Anthropic Claude API.
    
    Args:
        input_path: Path to the input file
        output_path: Path to the output file
        anthropic_client: Anthropic API client
        model: Claude model to use
    """
    try:
        logger.info(f"Translating {input_path} to {output_path}")
        
        # Read the file
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create a specific prompt for YAML translation
        prompt = """
        Translate the following YAML configuration file for a MkDocs site from Chinese to English. 
        Focus only on translating user-visible text content (like titles, site name, descriptions), 
        not keys or structural elements. Preserve all markdown file paths, formatting, and YAML syntax.
        
        Here's the content:
        
        """
        
        # Make the API call for translation
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=4000,
            temperature=0.1,
            system="You are an expert in translating YAML files while preserving their structure. Only translate the visible text content, not configuration keys or paths.",
            messages=[
                {"role": "user", "content": prompt + content}
            ]
        )
        
        # Extract and return the translated content
        translated_content = response.content[0].text
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the translated file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
            
        logger.info(f"Successfully translated {input_path}")
    except Exception as e:
        logger.error(f"Error translating {input_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Translate Markdown files from Chinese to English using Anthropic Claude API')
    parser.add_argument('--api_key', type=str, required=True,
                        help='Anthropic API key')
    parser.add_argument('--input_dir', type=str, default='.',
                        help='Input directory containing Markdown files (default: current directory)')
    parser.add_argument('--output_dir', type=str, default='./translated',
                        help='Output directory for translated files (default: ./translated)')
    parser.add_argument('--translate_filenames', action='store_true',
                        help='Translate filenames in addition to content')
    parser.add_argument('--model', type=str, default='claude-3-5-sonnet-20241022',
                        help='Claude model to use (default: claude-3-5-sonnet-20241022)')
    
    args = parser.parse_args()
    
    logger.info("Starting translation process using Anthropic Claude API")
    logger.info(f"Input directory: {args.input_dir}")
    logger.info(f"Output directory: {args.output_dir}")
    logger.info(f"Translate filenames: {args.translate_filenames}")
    logger.info(f"Using model: {args.model}")
    
    # Set up the Anthropic client
    anthropic_client = Anthropic(api_key=args.api_key)
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Translate mkdocs.yml if it exists
    mkdocs_path = os.path.join(args.input_dir, 'mkdocs.yml')
    if os.path.exists(mkdocs_path):
        translate_mkdocs_yml(mkdocs_path, os.path.join(args.output_dir, 'mkdocs.yml'), 
                            anthropic_client, args.model)
    
    # Process all Markdown files
    process_directory(args.input_dir, args.output_dir, anthropic_client, args.model, 
                    args.translate_filenames)
    
    logger.info("Translation process completed")

if __name__ == "__main__":
    main()