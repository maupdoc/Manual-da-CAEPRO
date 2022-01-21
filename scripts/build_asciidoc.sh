#!/usr/bin/bash

# A partir do root
asciidoc_build_path="asciidoc_build"
sed -i -e '/^######/ ! s/^#/##/' ${asciidoc_build_path}/book.md
sed -i -e '1i# MANUAL DA CAEPRO\n' ${asciidoc_build_path}/book.md 
kramdoc ${asciidoc_build_path}/book.md
asciidoctor-pdf ${asciidoc_build_path}/book.adoc
asciidoctor-epub3 ${asciidoc_build_path}/book.adoc
