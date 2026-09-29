# Login simples com PocketBase e Alpine.js

Projeto didático para iniciantes com duas páginas: `login.html` e `logado.html`. HTML, CSS e JavaScript ficam em arquivos separados desde a primeira etapa. Cada branch é uma fotografia do projeto ao final de uma aula.

## Sequência de aprendizagem

1. `etapa-01-html-estatico` - criar as duas páginas e separar `css/` e `js/`. O link apenas navega.
2. `etapa-02-alpine` - mostrar o e-mail digitado em tempo real com `x-data`, `x-model` e `x-text`. O botão Entrar continua desativado.
3. `etapa-03-login-pocketbase` - autenticar de verdade com `authWithPassword` e abrir a segunda página após sucesso.
4. `etapa-04-sessao-e-saida` - confirmar a sessão com `authRefresh`, mostrar o usuário e permitir sair.

A versão completa está em `main`, igual ao código da etapa 4. Use `git switch etapa-01-html-estatico` para começar e `git switch main` para voltar ao resultado final. Leia [PLANO_DE_AULA.md](PLANO_DE_AULA.md) para a condução da aula.

O PDF de apoio para os alunos fica em `output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf`. Sua fonte editável é `material/gerar_guia.py`.

## Preparação

1. Baixe e extraia o PocketBase pelo site oficial: https://pocketbase.io/.
2. Na pasta do executável, inicie o servidor com `pocketbase.exe serve` (no PowerShell, `./pocketbase.exe serve`).
3. Abra `http://127.0.0.1:8090/_/`, crie o administrador e uma coleção Auth chamada `users`.
4. Cadastre um aluno nessa coleção com e-mail e senha.
5. Em outro terminal, nesta pasta, execute `py -m http.server 5500` (ou `python -m http.server 5500`).
6. Abra `http://127.0.0.1:5500/login.html`.

Na etapa 1 não é necessário rodar o PocketBase. Na etapa 2, o navegador precisa de internet para carregar Alpine.js; nas etapas 3 e 4, também para o SDK do PocketBase. Mantenha `127.0.0.1` nos endereços do exemplo para usar a mesma origem no navegador.

## Onde está cada parte

- `login.html` e `logado.html`: estrutura das páginas.
- `css/estilo.css`: aparência compartilhada.
- `js/login.js`: estado do formulário e autenticação.
- `js/logado.js`: confirmação da sessão e saída.
- `js/pocketbase.js`: endereço do servidor, introduzido na etapa 3.

A página e seus scripts podem ser baixados pelo navegador. Para dados privados, configure regras de API nas coleções do PocketBase. Uma regra de leitura apenas para usuários autenticados é `@request.auth.id != ""`.