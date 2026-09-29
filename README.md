# Etapa 1: duas páginas HTML

## Objetivo

Reconhecer a estrutura de uma página e navegar entre login.html e logado.html.

## Observe no código

- h1 é o título da página.
- label descreve o campo ligado a um input.
- a com href abre outro arquivo HTML.

Os campos de e-mail e senha são apenas visuais. O link "Ver a segunda página" não usa os valores digitados nem autentica ninguém.

## Experimente

1. Abra login.html em http://127.0.0.1:5500/login.html.
2. Clique no link sem digitar nada.
3. Abra logado.html diretamente na barra de endereços.

Para iniciar o servidor de arquivos na pasta do projeto:

    py -m http.server 5500

Se py não funcionar, tente python -m http.server 5500.

## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.

## Próxima etapa

Na branch etapa-02-alpine, o formulário vai responder ao envio. A autenticação virá depois.