# Etapa 4 - sessão e saída

Projeto completo: duas páginas, arquivos HTML/CSS/JS separados, reatividade com Alpine.js e autenticação com PocketBase.

Após o login, `logado.html` usa `authRefresh()` para confirmar a sessão no servidor antes de mostrar o e-mail. O botão Sair limpa o estado de autenticação no navegador. A checagem local `authStore.isValid` apenas verifica se há token não expirado; a confirmação vem do PocketBase.

Para usar, inicie o PocketBase com `pocketbase.exe serve`, crie a coleção Auth `users` e um aluno no painel `http://127.0.0.1:8090/_/`. Nesta pasta, execute `py -m http.server 5500` e abra `http://127.0.0.1:5500/login.html`. Se `py` não funcionar, use `python -m http.server 5500`. As bibliotecas carregadas por CDN exigem internet.

Os arquivos da interface podem ser baixados pelo navegador. Ao adicionar dados privados, configure regras de API nas coleções do PocketBase. Para leitura por usuários autenticados, um exemplo de regra é `@request.auth.id != ""`.

O guia completo fica em `output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf`.