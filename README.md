# Etapa 2: interatividade com Alpine.js

Nesta etapa, o Alpine.js lê os campos e reage ao envio do formulário.

## O que praticar

- x-data guarda o estado da tela.
- x-model acompanha o que foi digitado.
- @submit.prevent chama a função sem recarregar o formulário.
- x-show e x-text exibem uma mensagem de erro.

## Atenção

O login é uma simulação: qualquer e-mail e senha preenchidos levam à outra página. Ainda não existe validação de usuário nem conexão com um servidor.

## Abrir o exemplo

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html.

## Próxima etapa

Na branch etapa-03-login-pocketbase, vamos trocar a simulação por authWithPassword do PocketBase.
## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.
