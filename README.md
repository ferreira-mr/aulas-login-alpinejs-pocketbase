# Etapa 2 - reatividade com Alpine.js

Os arquivos continuam separados desde a primeira etapa. Agora `js/login.js` define a função `formulario()`, e o Alpine.js liga o campo de e-mail à variável `email`. O texto muda enquanto você digita.

Conceitos: `x-data` cria o estado, `x-model` acompanha o campo e `x-text` mostra o valor na página. O botão Entrar continua desativado. Não há envio do formulário nem autenticação nesta etapa.

Para visualizar, execute `py -m http.server 5500` nesta pasta e abra `http://127.0.0.1:5500/login.html`. O navegador precisa de internet para carregar Alpine.js pela CDN. Se `py` não funcionar, use `python -m http.server 5500`.

Próxima etapa: `etapa-03-login-pocketbase`. Guia completo: `output/pdf/guia-passo-a-passo-login-pocketbase-alpine.pdf`.