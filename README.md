# Login simples com PocketBase e Alpine.js

Projeto didático com duas páginas: login e área do aluno. As branches contam a construção do projeto em etapas cumulativas. Comece pela primeira e avance uma etapa por vez.

## Branches da aula

1. etapa-01-html-estatico - marcação HTML e navegação simples entre páginas.
2. etapa-02-alpine - estado, campos ligados ao Alpine e envio de formulário simulado.
3. etapa-03-login-pocketbase - autenticação real com e-mail e senha no PocketBase.
4. etapa-04-pagina-protegida - redirecionamento quando não há login e botão Sair.
5. etapa-05-arquivos-organizados - versão final com HTML, CSS e JavaScript separados.

Para abrir uma etapa:

    git switch etapa-01-html-estatico

Para voltar à versão final:

    git switch main

O material de apoio em PDF fica em output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf.

## Preparar o PocketBase

1. Baixe o PocketBase para seu sistema em https://pocketbase.io/ e extraia o arquivo.
2. Em um terminal na pasta do executável, rode:

       .\pocketbase.exe serve

3. Abra http://127.0.0.1:8090/_/ e crie uma conta de administrador.
4. Crie uma coleção do tipo Auth chamada users.
5. Na coleção users, crie um registro com e-mail e senha para o aluno.

## Abrir o projeto

Com o PocketBase rodando, abra outro terminal nesta pasta e inicie um servidor para os arquivos:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html. Se py não funcionar, use python -m http.server 5500.

## Como funciona

- login.html tem o formulário; Alpine chama a função entrar quando o aluno envia.
- js/login.js usa authWithPassword para conferir as credenciais na coleção users.
- js/logado.js confere o token salvo, mostra o e-mail e permite sair.
- js/pocketbase.js guarda o endereço do servidor.
- css/estilo.css contém os estilos compartilhados pelas duas páginas.

A verificação em logado.html controla a interface no navegador. Para proteger dados, configure também as regras de acesso das coleções no PocketBase.