#!/usr/bin/bash

# A partir do root
asciidoc_build_path="asciidoc_build"
kramdoc ${asciidoc_build_path}/book.md
asciidoctor-pdf ${asciidoc_build_path}/book.adoc
asciidoctor-epub3 ${asciidoc_build_path}/book.adoc
