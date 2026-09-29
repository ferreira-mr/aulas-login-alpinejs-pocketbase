# Etapa 3 - login real com PocketBase

Os arquivos continuam separados. O formulário agora envia e-mail e senha ao PocketBase com `authWithPassword`. Só após a resposta de sucesso a página abre `logado.html`.

Antes de abrir o site, inicie o PocketBase com `pocketbase.exe serve`, abra `http://127.0.0.1:8090/_/`, crie uma coleção Auth chamada `users` e cadastre um aluno. Em outro terminal nesta pasta, execute `py -m http.server 5500` e abra `http://127.0.0.1:5500/login.html`.

O navegador precisa de internet para carregar PocketBase SDK e Alpine.js pelas CDNs. Se `py` não funcionar, use `python -m http.server 5500`.

Nesta etapa, `logado.html` ainda pode ser aberta diretamente. A confirmação da sessão e o botão Sair entram na `etapa-04-sessao-e-saida`. Guia completo: `output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf`.