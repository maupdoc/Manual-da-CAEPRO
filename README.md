[![CI](https://github.com/maupdoc/Manual-da-CAEPRO/actions/workflows/main.yml/badge.svg)](https://github.com/maupdoc/Manual-da-CAEPRO/actions/workflows/main.yml)

# Manual da CAEPRO

## Objetivo

O foco é apenas um: ajudar a comunidade de Engenharia de Produção da UFPI

## Serviços

Temos uma página online elegante criada usando [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). A página pode ser acessada de qualquer navegador no seguinte endereço: https://maupdoc.github.io/Manual-da-CAEPRO/

## Instalação e Execução

### Pré-requisitos

Os pacotes python necessários para rodar e construir o projeto estão listados no arquivo "requirements.txt". Execute o seguinte comando para instalar esses pacotes usando o PIP:

```
pip install -r requirements.txt
```
---

Todos os comandos envolvendo "mkdocs" devem ser executados no início da pasta que contém o arquivo "mkdocs.yml". 

---

Após isso, rode:

```
mkdocs serve
```

Esse comando retorna o endereço, que pode ser acessado no navegador, para visualizar o site gerado. Algo como `[10:23:05] Serving on http://127.0.0.1:8000/` vai ser o endereço.

Para construir, rode:

```
mkdocs build
```

Depois disso, acesse a pasta "site". Haverá o site criado a partir dos documentos em Markdown, além de uma pasta "pdf" com o PDF criado a partir do site.

