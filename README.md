# Etapa 3: login real com PocketBase

Nesta etapa, trocamos a simulação por uma chamada ao PocketBase.

## Conceitos

- O SDK é uma biblioteca que facilita as chamadas HTTP para o PocketBase.
- authWithPassword envia e-mail e senha para a coleção de autenticação.
- A resposta inclui o registro autenticado e um token.
- O SDK guarda o token no armazenamento local do navegador, para a outra página recuperar o estado.

## Preparar o PocketBase

1. Baixe e inicie o PocketBase: .\pocketbase.exe serve
2. Abra http://127.0.0.1:8090/_/ e crie uma coleção do tipo Auth chamada users.
3. Crie um registro de usuário com e-mail e senha.

## Abrir o projeto

Em outro terminal, dentro da pasta do projeto:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html e entre com o usuário cadastrado.

## Atenção

A área do aluno ainda não bloqueia quem abre logado.html diretamente. Vamos cuidar disso na etapa 4.

## Próxima etapa

Na branch etapa-04-pagina-protegida, a página vai conferir o estado do login e permitir sair.
## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.
