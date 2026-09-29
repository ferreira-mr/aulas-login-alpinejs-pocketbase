# Plano de aula - login simples

## Objetivo

Ao final, o aluno consegue reconstruir duas páginas, explicar a função de HTML, CSS, JavaScript, Alpine.js e PocketBase, autenticar um usuário, confirmar a sessão e sair. O projeto usa a menor quantidade de conceitos novos possível em cada etapa.

## Estratégia para o professor

1. Antes de mostrar código, apresente o problema: uma página recebe e-mail e senha; um servidor precisa confirmar a conta. Pergunte por que um link entre páginas não prova a identidade do aluno.
2. Em cada etapa, mostre o resultado no navegador, peça uma previsão do que acontecerá e só então abra os arquivos. Demonstre uma mudança pequena, deixe os alunos reproduzirem e encerre com a pergunta de verificação indicada abaixo.
3. Evite introduzir `fetch`, módulos, empacotador, banco de dados manual ou regras de API detalhadas antes de a autenticação funcionar. O SDK do PocketBase já fornece a chamada de login e o armazenamento da sessão.
4. Depois da demonstração, peça a reconstrução independente com o PDF, sem copiar a branch pronta. As branches servem para consulta e comparação quando alguém travar.

## Preparação do ambiente

- Navegador, editor de texto, Python para servir arquivos estáticos e PocketBase local para as etapas 3 e 4.
- Internet para as bibliotecas carregadas por CDN.
- No PocketBase, uma coleção Auth `users` e uma conta de aluno fictícia. Não use senhas reais dos alunos.
- Para iniciar a interface: `py -m http.server 5500` nesta pasta; URL: `http://127.0.0.1:5500/login.html`.

## Etapas e checkpoints

| Etapa | Conteúdo novo | O aluno faz | Como verificar a compreensão |
| --- | --- | --- | --- |
| 1. `etapa-01-html-estatico` | Duas páginas; caminhos entre arquivos; HTML e CSS separados; arquivos JS reservados | Cria `login.html`, `logado.html`, `css/estilo.css`, `js/login.js` e `js/logado.js`; usa um link para conhecer a segunda página | Explica por que o link abre a página sem login e identifica qual arquivo altera a aparência |
| 2. `etapa-02-alpine` | Estado local com `x-data`; vínculo `x-model`; apresentação `x-text` | Mostra o e-mail digitado enquanto escreve; mantém o botão Entrar desativado | Aponta onde o valor mora e confirma que nenhum dado foi enviado ao servidor |
| 3. `etapa-03-login-pocketbase` | Coleção Auth, SDK, `async/await`, `try/catch`, `authWithPassword` | Configura `js/pocketbase.js`, ativa o formulário e trata sucesso/erro | Compara senha errada e correta; reconhece que a segunda página ainda abre diretamente |
| 4. `etapa-04-sessao-e-saida` | Token local, `authRefresh`, carregamento, saída e regra de API | Confirma a sessão antes de mostrar o usuário e limpa o login ao sair | Atualiza a página, sai e tenta abrir `logado.html` diretamente; explica onde os dados privados são protegidos |

## Estrutura dos arquivos desde a primeira etapa

```text
login.html
logado.html
css/
  estilo.css
js/
  login.js
  logado.js
  pocketbase.js  (entra somente na etapa 3)
```

Os arquivos JS das páginas começam com comentários. Isso mostra o lugar do comportamento sem inventar uma ação antes de ela ser necessária. Na etapa 2, só `js/login.js` recebe a função de estado local.

## Reconstrução individual após a explicação

1. Esconder o código pronto e seguir as instruções do PDF na ordem.
2. Criar as pastas e os cinco arquivos da etapa 1. Abrir as duas páginas e identificar o papel de cada arquivo.
3. Acrescentar Alpine.js e fazer o e-mail aparecer em tempo real, mantendo o botão desativado.
4. Criar a coleção Auth `users` no PocketBase, adicionar `js/pocketbase.js` e implementar `authWithPassword`.
5. Acrescentar `authRefresh` e o botão Sair. Experimentar senha incorreta, acesso direto, atualização e saída.
6. Comparar o próprio resultado com a branch de cada etapa e corrigir diferenças com base no comportamento observado.

## Critério de conclusão

O aluno consegue explicar oralmente ou por escrito: o que muda em cada etapa; por que o exemplo da etapa 2 ainda não autentica; qual chamada consulta o servidor; por que `authStore.isValid` sozinho não confirma a sessão; e por que dados privados exigem regras de API no PocketBase.

## Limite consciente do exemplo

A interface é pública por natureza. O redirecionamento organiza a experiência do usuário; a autorização de dados pertence às regras da API do PocketBase. O exemplo não contém dados privados além do próprio e-mail mostrado após a confirmação da sessão.