# Manual da CAEPRO

## Objetivo

O foco é apenas um: ajudar a comunidade de Engenharia de Produção da UFPI

## Serviços

Temos uma página online elegante criada usando [mdBook](https://github.com/rust-lang/mdBook). A página pode ser acessada de qualquer navegador no seguinte endereço: https://maupdoc.github.io/Manual-da-CAEPRO/

Além disso, ofertamos versões em [EPUB](https://github.com/maupdoc/Manual-da-CAEPRO/raw/main/asciidoc_build/book.epub) e em [PDF](https://github.com/maupdoc/Manual-da-CAEPRO/raw/main/asciidoc_build/book.pdf) para quem achar mais prático.

# Colaboração

## Estrutura do projeto

Os documentos que compõem o Manual estão listados e devem ser editados na pasta [src](https://github.com/maupdoc/Manual-da-CAEPRO/tree/main/src). Nessa pasta, há o SUMMARY.md que indica quais arquivos (escritos em Markdown) são incluídos no resultado final do Manual e como são organizados na hierarquia.

É **muito importante** seguir a convenção de nomes para os arquivos, pois facilita a compreensão e a execução de scripts essenciais para o projeto. A convenção adotada é juntar o número do capítulo, número do subcapítulo e o título do documento unidos com hífen . Exemplos:

* ch00-00-introducao.md (capítulo 0, subcapítulo 0, título legível: introducao)
* ch00-01-subintroducao.md (capítulo 0, subcapítulo 1, título legível: subintroducao)

A construção do SUMMARY.md está detalhado na [documentação do mdBook](https://rust-lang.github.io/mdBook/format/summary.html).
