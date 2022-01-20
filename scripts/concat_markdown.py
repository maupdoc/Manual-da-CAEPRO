#!/usr/bin/python3
import os

docs_dir = 'src'

def is_markdown(filename):
    return str(filename).endswith('.md')

markdown_files = list(filter(is_markdown, os.listdir(docs_dir)))
try:
    markdown_files.remove("SUMMARY.md")
except:
    print("Error: SUMMARY.md not found")
    exit()
# Order it's important
markdown_files.sort()

try:
    os.mkdir('asciidoc_build')
except FileExistsError:
    pass
except:
    exit
with open(os.path.join('asciidoc_build', 'book.md'), 'w') as outfile:
    for md_file in markdown_files:
        with open(os.path.join(docs_dir, md_file), 'r') as infile:
            for line in infile:
                outfile.write(line)
print("Markdown compiled to asciidoc_build")
