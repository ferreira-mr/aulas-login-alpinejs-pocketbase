# Login simples com PocketBase e Alpine.js

Projeto didático com duas páginas: login e área do aluno. As cinco branches mostram o código ao fim de cada etapa da aula. O PDF de apoio acompanha todas elas.

## Etapas da aula

1. etapa-01-html-estatico - conhecer o HTML e a navegação entre duas páginas.
2. etapa-02-alpine - ler e responder ao formulário no navegador, sem autenticar.
3. etapa-03-login-pocketbase - usar authWithPassword para entrar de verdade.
4. etapa-04-sessao-e-saida - confirmar a sessão no PocketBase e implementar Sair.
5. etapa-05-arquivos-organizados - mover CSS e JavaScript para arquivos próprios.

Abra uma etapa com git switch etapa-01-html-estatico. Volte ao resultado final com git switch main. As etapas são checkpoints: você pode abrir cada branch, ler os comentários e comparar os arquivos.

O material de apoio fica em output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf. A fonte editável do PDF está em material/gerar_guia.py; execute python material/gerar_guia.py para recriá-lo.

## Preparar o PocketBase

1. Baixe o PocketBase em https://pocketbase.io/ e extraia o arquivo.
2. Na pasta do executável, rode:

       .\pocketbase.exe serve

3. Abra http://127.0.0.1:8090/_/ e crie sua conta de administrador.
4. Crie uma coleção do tipo Auth chamada users.
5. Na coleção users, cadastre um aluno com e-mail e senha.

## Abrir as páginas

Com o PocketBase rodando, abra outro terminal nesta pasta:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html. Se py não funcionar, tente python -m http.server 5500.

Use 127.0.0.1 de forma consistente no navegador e na configuração para manter o login salvo na mesma origem. O navegador precisa de internet para carregar Alpine.js e o SDK pelos links CDN.

## Onde está cada parte

- login.html e logado.html contêm as duas páginas.
- css/estilo.css contém os estilos das duas páginas.
- js/pocketbase.js guarda o endereço do PocketBase.
- js/login.js envia e-mail e senha para a coleção users.
- js/logado.js confirma a sessão com authRefresh, mostra o e-mail e limpa o login ao sair.

O HTML e o JavaScript da interface podem ser baixados pelo navegador. Quando você adicionar dados privados, configure regras de API nas coleções do PocketBase. Por exemplo, para permitir listar e visualizar registros somente a usuários autenticados, use a regra @request.auth.id != "".