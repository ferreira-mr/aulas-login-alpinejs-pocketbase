# Etapa 4: confirmar a sessão e sair

## Objetivo

Conferir o login ao abrir a área do aluno e permitir que o aluno saia.

## Observe no código

- authStore.isValid lê o token salvo e verifica se ele ainda não expirou.
- authRefresh consulta o PocketBase para confirmar a sessão e atualizar o registro.
- usuario começa vazio; o conteúdo aparece depois da resposta do servidor.
- verificando mostra uma mensagem enquanto aguardamos.
- authStore.clear remove o login salvo neste navegador.

## Experimente

1. Entre com um usuário válido e atualize logado.html.
2. Clique em Sair e tente abrir logado.html diretamente.
3. Confira que você volta ao formulário.
4. Abra uma janela anônima e acesse logado.html sem fazer login.

Mantenha o PocketBase rodando. Em outro terminal, inicie o servidor das páginas:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html.

## Dados privados

O navegador consegue baixar os arquivos HTML e JavaScript. O redirecionamento organiza a interface, e authRefresh confirma o token com o servidor. Quando adicionarmos dados privados, as regras de API das coleções também precisam exigir autenticação. Uma regra simples para listar e visualizar registros apenas com login é:

    @request.auth.id != ""

## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.

## Próxima etapa

Na branch etapa-05-arquivos-organizados, vamos mover CSS e JavaScript para arquivos próprios sem mudar o fluxo.