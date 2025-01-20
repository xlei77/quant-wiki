import os
import re

def update_pdf_links(directory):
    """
    遍历目录下所有markdown文件，更新PDF链接为GitHub链接
    """
    # 编译正则表达式模式 - 匹配markdown链接格式 [text](./path.pdf)
    pattern = r'\[(.*?)\]\((\.\/.*?\.pdf)\)'
    github_base = 'https://github.com/LLMQuant/asset/blob/main'
    
    # 遍历所有markdown文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找并替换PDF链接
                def replace_link(match):
                    text = match.group(1)  # 链接文本
                    pdf_path = match.group(2)  # PDF路径
                    # 提取PDF文件名
                    pdf_name = os.path.basename(pdf_path)
                    # 构建新的GitHub链接
                    new_link = f'{github_base}/{pdf_name}'
                    return f'[{text}]({new_link})'
                
                new_content = re.sub(pattern, replace_link, content)
                
                # 如果内容有变化，写回文件
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Updated: {file_path}')

if __name__ == '__main__':
    # 指定要处理的目录
    docs_dir = 'docs'
    update_pdf_links(docs_dir)
    print('PDF links update completed!')