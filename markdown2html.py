#!/usr/bin/python3
import sys, os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(markdown_file, 'r') as md_file:
            md_content = md_file.readlines()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)