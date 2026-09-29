# Etapa 3: autenticar com PocketBase

## Objetivo

Trocar a resposta local do formulário por uma chamada real de autenticação.

## Observe no código

- O SDK cria window.pb para conversar com o PocketBase.
- collection('users') aponta para a coleção Auth dos alunos.
- authWithPassword envia e-mail e senha ao servidor.
- await espera a resposta; try/catch trata sucesso e erro.
- O SDK guarda o token e o registro autenticado no navegador.

## Preparar o PocketBase

1. Baixe o PocketBase e rode .\pocketbase.exe serve.
2. Abra http://127.0.0.1:8090/_/ e crie uma coleção do tipo Auth chamada users.
3. Cadastre um usuário com e-mail e senha nessa coleção.

Em outro terminal, dentro da pasta do projeto:

    py -m http.server 5500

Abra http://127.0.0.1:5500/login.html.

## Experimente

1. Tente entrar com uma senha errada e observe a mensagem.
2. Entre com o usuário cadastrado e veja o e-mail em logado.html.
3. Abra logado.html diretamente em outra sessão do navegador.

A última ação mostra um limite desta etapa: a página ainda pode ser aberta diretamente. O controle do estado e a confirmação da sessão no servidor virão na etapa 4.

## Material de apoio

Consulte output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf para o passo a passo completo.

## Próxima etapa

Na branch etapa-04-sessao-e-saida, vamos confirmar a sessão e implementar o botão Sair.