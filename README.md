# Etapa 4: estado do login, redirecionamento e saída

Nesta etapa, as páginas consultam o estado mantido pelo SDK do PocketBase.

## Conceitos

- authStore.isValid informa se o token guardado ainda está dentro do prazo.
- A página login.html encaminha para logado.html se já houver um token válido.
- A página logado.html volta ao login quando não há login salvo.
- authStore.clear apaga o token local e encerra o fluxo neste navegador.

## Pratique

1. Entre com um usuário válido.
2. Atualize logado.html: a página continua mostrando o aluno.
3. Clique em Sair e tente abrir logado.html diretamente.
4. Confira que o navegador volta para login.html.

## Importante sobre segurança

O redirecionamento é uma verificação de interface no navegador. Ele não protege sozinho dados da API. O PocketBase precisa ter regras de acesso configuradas nas coleções que guardam dados.

## Abrir o exemplo

Mantenha o PocketBase rodando e, em outro terminal, inicie o servidor da página:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html.

## Próxima etapa

Na branch etapa-05-arquivos-organizados, vamos separar HTML, CSS e JavaScript em arquivos próprios.
## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.
