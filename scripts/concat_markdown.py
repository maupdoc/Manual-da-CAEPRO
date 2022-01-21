#!/usr/bin/python3
import os
import shutil

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
media_dir = os.path.join(docs_dir, 'media')
asciidoc_build_media_dir = os.path.join('asciidoc_build', 'media')
if os.path.isdir(asciidoc_build_media_dir):
    try:
        shutil.rmtree(asciidoc_build_media_dir)
    except:
        print("Error: Unable to delete media folder in asciidoc_build")

shutil.copytree(media_dir, asciidoc_build_media_dir, dirs_exist_ok=True)

with open(os.path.join('asciidoc_build', 'book.md'), 'w') as outfile:
    for md_file in markdown_files:
        with open(os.path.join(docs_dir, md_file), 'r') as infile:
            for line in infile:
                outfile.write(line)

print("Markdown compiled to asciidoc_build")
