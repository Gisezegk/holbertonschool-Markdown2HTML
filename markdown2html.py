#!/usr/bin/python3

import sys
import os
import re


def convert_markdown_to_html(markdown_text):
    html_lines = []

    heading_pattern = re.compile(r'^(#{1,6})\s*(.*)')

    for line in markdown_text.splitlines():
        match = heading_pattern.match(line)
        if match:
            level = len(match.group(1))
            content = match.group(2).strip()
            html_lines.append(f"<h{level}>{content}</h{level}>")
        else:
            html_lines.append(line)

    return "\n".join(html_lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
            html_content = markdown.markdown(md_content)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
