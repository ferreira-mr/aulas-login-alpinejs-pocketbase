# Etapa 2: formulário com Alpine.js

## Objetivo

Ler os campos do formulário e responder ao envio sem recarregar a página.

## Observe no código

- x-data guarda as variáveis e a função da tela.
- x-model acompanha o valor digitado.
- @submit.prevent chama enviar() sem o envio padrão do navegador.
- x-show e x-text apresentam o erro ou a mensagem.

Nesta etapa, o código apenas mostra uma mensagem local. Ele não compara senhas, não envia dados e não abre logado.html. Um e-mail precisa ter formato válido por causa do tipo do campo HTML.

## Experimente

1. Envie os campos vazios e leia o erro.
2. Digite um e-mail válido e uma senha qualquer e envie.
3. Observe que o campo senha é limpo e seu conteúdo nunca aparece na mensagem.

Inicie o servidor de arquivos na pasta do projeto:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html.

## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.

## Próxima etapa

Na branch etapa-03-login-pocketbase, authWithPassword vai enviar as credenciais ao PocketBase.