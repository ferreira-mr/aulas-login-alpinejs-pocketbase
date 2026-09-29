"""Gera o PDF do guia didático. Execute: python material/gerar_guia.py."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
DESTINO = ROOT / "output" / "pdf" / "guia-passo-a-passo-login-pocketbase-alpine.pdf"
DESTINO.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Code", r"C:\Windows\Fonts\consola.ttf"))

AZUL_ESCURO = colors.HexColor("#17324D")
AZUL = colors.HexColor("#2563EB")
VERDE = colors.HexColor("#0F766E")
CINZA = colors.HexColor("#536273")
TEXTO = colors.HexColor("#243447")
BORDA = colors.HexColor("#D7E0E8")
FUNDO = colors.HexColor("#F1F5F9")
FUNDO_AZUL = colors.HexColor("#EFF6FF")
FUNDO_LARANJA = colors.HexColor("#FFF7ED")
LARANJA = colors.HexColor("#B45309")
BRANCO = colors.white

ESTILOS = {
    "sobretitulo": ParagraphStyle(
        "sobretitulo", fontName="Arial-Bold", fontSize=10, leading=13,
        textColor=VERDE, spaceAfter=9,
    ),
    "capa": ParagraphStyle(
        "capa", fontName="Arial-Bold", fontSize=29, leading=34,
        textColor=AZUL_ESCURO, spaceAfter=12,
    ),
    "subcapa": ParagraphStyle(
        "subcapa", fontName="Arial", fontSize=13, leading=19,
        textColor=CINZA, spaceAfter=12,
    ),
    "titulo": ParagraphStyle(
        "titulo", fontName="Arial-Bold", fontSize=22, leading=27,
        textColor=AZUL_ESCURO, spaceAfter=8,
    ),
    "secao": ParagraphStyle(
        "secao", fontName="Arial-Bold", fontSize=13, leading=17,
        textColor=VERDE, spaceBefore=8, spaceAfter=5,
    ),
    "corpo": ParagraphStyle(
        "corpo", fontName="Arial", fontSize=9.5, leading=14.2,
        textColor=TEXTO, spaceAfter=6,
    ),
    "pequeno": ParagraphStyle(
        "pequeno", fontName="Arial", fontSize=8.2, leading=11.5,
        textColor=CINZA, spaceAfter=5,
    ),
    "item": ParagraphStyle(
        "item", fontName="Arial", fontSize=9.2, leading=13.4,
        textColor=TEXTO, leftIndent=13, firstLineIndent=-10, spaceAfter=3,
    ),
    "codigo": ParagraphStyle(
        "codigo", fontName="Code", fontSize=7.6, leading=10.5,
        textColor=colors.HexColor("#E6EDF3"),
    ),
    "cabecalho_tabela": ParagraphStyle(
        "cabecalho_tabela", fontName="Arial-Bold", fontSize=8.2,
        leading=11, textColor=BRANCO,
    ),
    "celula": ParagraphStyle(
        "celula", fontName="Arial", fontSize=8, leading=11,
        textColor=TEXTO,
    ),
    "celula_forte": ParagraphStyle(
        "celula_forte", fontName="Arial-Bold", fontSize=8,
        leading=11, textColor=AZUL_ESCURO,
    ),
}


def p(texto, estilo="corpo"):
    return Paragraph(texto, ESTILOS[estilo])


def itens(textos):
    return [p("- " + texto, "item") for texto in textos]


def codigo(texto):
    bloco = Table([[Preformatted(texto.strip("\n"), ESTILOS["codigo"])]], colWidths=[170 * mm])
    bloco.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AZUL_ESCURO),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return bloco


def aviso(titulo, texto, fundo=FUNDO_AZUL, destaque=AZUL):
    bloco = Table([[[p(titulo, "celula_forte"), Spacer(1, 4), p(texto, "celula")]]], colWidths=[170 * mm])
    bloco.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fundo),
        ("BOX", (0, 0), (-1, -1), 0.6, BORDA),
        ("LINEBEFORE", (0, 0), (0, -1), 3, destaque),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return bloco


def tabela_capa():
    dados = [[p("ETAPA", "cabecalho_tabela"),
              p("IDEIA NOVA", "cabecalho_tabela"),
              p("BRANCH", "cabecalho_tabela")]]
    etapas = [
        ("01", "Arquivos separados e duas páginas", "etapa-01-html-estatico"),
        ("02", "Alpine mostra o e-mail digitado", "etapa-02-alpine"),
        ("03", "PocketBase autentica a conta", "etapa-03-login-pocketbase"),
        ("04", "Confirmar sessão e sair", "etapa-04-sessao-e-saida"),
    ]
    for numero, conceito, branch in etapas:
        dados.append([p(numero, "celula_forte"), p(conceito, "celula"), p(branch, "celula")])
    tabela = Table(dados, colWidths=[19 * mm, 73 * mm, 78 * mm], repeatRows=1)
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
        ("GRID", (0, 0), (-1, -1), 0.45, BORDA),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return tabela


def capa(canvas, doc):
    canvas.saveState()
    largura, altura = A4
    canvas.setFillColor(AZUL_ESCURO)
    canvas.rect(0, altura - 9 * mm, largura, 9 * mm, stroke=0, fill=1)
    canvas.setFillColor(VERDE)
    canvas.rect(0, 0, 7 * mm, altura, stroke=0, fill=1)
    canvas.setFillColor(CINZA)
    canvas.setFont("Arial", 8)
    canvas.drawString(23 * mm, 12 * mm, "MATERIAL DE APOIO | DESENVOLVIMENTO WEB")
    canvas.drawRightString(largura - 20 * mm, 12 * mm, "PocketBase + Alpine.js")
    canvas.restoreState()


def pagina(canvas, doc):
    canvas.saveState()
    largura, altura = A4
    canvas.setFillColor(AZUL_ESCURO)
    canvas.setFont("Arial-Bold", 8)
    canvas.drawString(20 * mm, altura - 13 * mm, "LOGIN SIMPLES | GUIA DO ALUNO")
    canvas.setStrokeColor(BORDA)
    canvas.setLineWidth(0.6)
    canvas.line(20 * mm, altura - 16 * mm, largura - 20 * mm, altura - 16 * mm)
    canvas.line(20 * mm, 15 * mm, largura - 20 * mm, 15 * mm)
    canvas.setFillColor(CINZA)
    canvas.setFont("Arial", 8)
    canvas.drawString(20 * mm, 9 * mm, "Uma ideia nova por etapa")
    canvas.drawRightString(largura - 20 * mm, 9 * mm, str(doc.page))
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(DESTINO), pagesize=A4,
    leftMargin=20 * mm, rightMargin=20 * mm,
    topMargin=23 * mm, bottomMargin=22 * mm,
    title="Guia do aluno: login com PocketBase e Alpine.js",
    author="Material de apoio para alunos",
)
historia = []

# 1. Capa
historia += [
    Spacer(1, 17 * mm),
    p("CADERNO DE APOIO | PROJETO GUIADO", "sobretitulo"),
    p("Login simples com<br/>PocketBase e Alpine.js", "capa"),
    p("Construa duas páginas, entenda cada tecnologia e depois repita o projeto sem acompanhar o professor.", "subcapa"),
    Spacer(1, 5 * mm),
    aviso("A pergunta do projeto", "Como saber se quem abriu a segunda página realmente informou uma conta válida? Um link não responde a isso. Vamos avançar até a confirmação no servidor.", FUNDO_AZUL, VERDE),
    Spacer(1, 8 * mm),
    p("Quatro etapas, uma ideia nova por vez", "secao"),
    tabela_capa(),
    Spacer(1, 9 * mm),
    aviso("Como estudar", "Leia a explicação, digite o trecho de código, faça o experimento e responda à pergunta de cada etapa. As branches mostram o resultado esperado quando você precisar comparar.", FUNDO, AZUL),
    p("Público: alunos iniciantes em HTML, CSS e JavaScript.", "pequeno"),
    PageBreak(),
]

# 2. Contexto e mapa
historia += [
    p("Entenda o problema antes do código", "titulo"),
    p("Uma escola quer uma tela de entrada e uma área do aluno. O navegador desenha as telas; o PocketBase guarda as contas e decide se e-mail e senha correspondem a um usuário cadastrado.", "corpo"),
    codigo("aluno -> login.html -> Alpine.js -> PocketBase\n                              <- resposta\n         -> logado.html (após sucesso)"),
    p("Quem faz o quê?", "secao"),
    *itens([
        "<b>HTML</b> organiza títulos, campos, botões e links.",
        "<b>CSS</b> define aparência e espaçamento.",
        "<b>JavaScript</b> executa as ações programadas.",
        "<b>Alpine.js</b> liga valores do JavaScript aos elementos HTML.",
        "<b>PocketBase</b> confere as credenciais no servidor e emite a sessão.",
    ]),
    p("Três ideias que parecem iguais, mas não são", "secao"),
    *itens([
        "<b>Navegar</b>: abrir outro arquivo por um link. Qualquer pessoa pode fazê-lo.",
        "<b>Reagir</b>: atualizar o texto da página quando algo é digitado. Isso ocorre no navegador.",
        "<b>Autenticar</b>: pedir ao servidor para verificar uma conta.",
    ]),
    aviso("O que você vai produzir", "Desde o começo haverá login.html, logado.html, css/estilo.css, js/login.js e js/logado.js. O arquivo js/pocketbase.js será criado na etapa 3.", FUNDO_AZUL, AZUL),
    p("Depois da explicação do professor, use as páginas 11 e 12 para reconstruir tudo sozinho.", "pequeno"),
    PageBreak(),
]

# 3. Ambiente
historia += [
    p("Prepare seu ambiente", "titulo"),
    p("Você precisa de um editor, navegador, Python para servir os arquivos e PocketBase para as etapas 3 e 4. As bibliotecas Alpine.js e SDK do PocketBase são carregadas por CDN; mantenha internet ativa.", "corpo"),
    p("1. Crie a pasta do projeto", "secao"),
    codigo("login-simples/\n  login.html\n  logado.html\n  css/estilo.css\n  js/login.js\n  js/logado.js"),
    p("2. Sirva os arquivos no navegador", "secao"),
    p("Abra um terminal dentro de login-simples e execute:", "corpo"),
    codigo("py -m http.server 5500\n# alternativa: python -m http.server 5500"),
    p("Acesse http://127.0.0.1:5500/login.html. Não feche esse terminal enquanto estiver trabalhando.", "corpo"),
    p("3. Prepare o PocketBase antes da etapa 3", "secao"),
    *itens([
        "Baixe e extraia o PocketBase pelo site oficial: pocketbase.io.",
        "Em outro terminal, na pasta do executável, rode o comando abaixo.",
        "Abra http://127.0.0.1:8090/_/ e crie o administrador.",
        "Crie uma coleção do tipo Auth chamada users e um aluno fictício com e-mail e senha.",
    ]),
    codigo(r".\pocketbase.exe serve"),
    aviso("Dois servidores", "A interface usa a porta 5500. O PocketBase usa a porta 8090. O navegador chama o PocketBase quando o aluno envia o formulário.", FUNDO_AZUL, VERDE),
    PageBreak(),
]

# 4. Etapa 1 HTML
historia += [
    p("Etapa 1 | Monte as duas páginas", "titulo"),
    p("Branch de referência: etapa-01-html-estatico", "pequeno"),
    p("Crie os cinco arquivos mostrados na página anterior. Nesta etapa, os JS podem conter apenas um comentário. Isso reserva o lugar do comportamento sem inventar uma função desnecessária.", "corpo"),
    p("Comece por login.html", "secao"),
    codigo('''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Login dos alunos</title>
  <link rel="stylesheet" href="css/estilo.css">
  <script defer src="js/login.js"></script>
</head>
<body>
  <main class="cartao">
    <h1>Entrar</h1>
    <label for="email">E-mail</label>
    <input id="email" type="email">
    <label for="senha">Senha</label>
    <input id="senha" type="password">
    <button type="button" disabled>Entrar (em breve)</button>
    <p><a href="logado.html">Conhecer a segunda página</a></p>
  </main>
</body>
</html>'''),
    p("Em logado.html, use a mesma estrutura head. Troque o título e o conteúdo de main por uma mensagem: 'Você chegou por um link; ainda não existe login'. Acrescente um link de volta para login.html e carregue js/logado.js.", "corpo"),
    aviso("Experimento", "Abra logado.html sem preencher os campos. Explique por que isso foi possível. O botão está desativado; foi o link que abriu a página.", FUNDO_LARANJA, LARANJA),
    PageBreak(),
]

# 5. Etapa 1 CSS e caminhos
historia += [
    p("Etapa 1 | Dê forma e entenda os caminhos", "titulo"),
    p("Escreva em css/estilo.css um estilo pequeno. Você pode ampliar as cores e espaçamentos depois, sem alterar o funcionamento do login.", "corpo"),
    codigo(''':root {
  font-family: Arial, sans-serif;
  color: #1f2937;
  background: #f3f4f6;
}
* { box-sizing: border-box; }
body {
  min-height: 100vh;
  margin: 0;
  display: grid;
  place-items: center;
}
.cartao {
  width: min(100%, 380px);
  padding: 32px;
  background: white;
  border: 1px solid #e5e7eb;
}
label { display: block; margin-top: 16px; }
input { width: 100%; padding: 10px; }
button { margin-top: 20px; }
'''),
    p("No HTML, o caminho css/estilo.css começa na mesma pasta do HTML. O navegador procura a pasta css e depois o arquivo estilo.css. O mesmo raciocínio vale para js/login.js.", "corpo"),
    p("Confira sua etapa", "secao"),
    *itens([
        "As duas páginas têm conteúdo e estilos.",
        "Mudar a cor em css/estilo.css altera as duas páginas.",
        "O botão Entrar não faz nada; o link abre a segunda página.",
        "js/login.js e js/logado.js existem, mas ainda não executam ações.",
    ]),
    aviso("Pergunta de compreensão", "Se você apagar o link e mantiver os campos, alguém consegue chegar à segunda página digitando e-mail e senha? Por quê?", FUNDO_AZUL, VERDE),
    PageBreak(),
]

# 6. Etapa 2
historia += [
    p("Etapa 2 | Veja Alpine.js reagir", "titulo"),
    p("Branch de referência: etapa-02-alpine", "pequeno"),
    p("Alpine.js vai copiar para a tela o e-mail enquanto você digita. Não há envio nem autenticação. O botão continua desativado.", "corpo"),
    p("1. Carregue a biblioteca depois do seu JS", "secao"),
    codigo('''<script defer src="js/login.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.17.4/dist/cdn.min.js"></script>'''),
    p("A ordem importa: sua função precisa existir quando Alpine iniciar.", "pequeno"),
    p("2. Acrescente os atributos ao HTML", "secao"),
    codigo('''<main class="cartao" x-data="formulario()" x-cloak>
  <label for="email">E-mail</label>
  <input id="email" type="email" x-model="email">
  <p x-show="email">E-mail digitado:
    <strong x-text="email"></strong>
  </p>
  <!-- Mantenha o campo de senha e o botão desativado. -->
</main>'''),
    p("3. Escreva js/login.js", "secao"),
    codigo("function formulario() {\n  return { email: '' };\n}"),
    p("x-data cria o estado; x-model atualiza email; x-text exibe esse valor; x-show esconde o parágrafo quando ele está vazio. Em CSS, adicione [x-cloak] { display: none !important; } para evitar texto incompleto antes de Alpine iniciar.", "corpo"),
    aviso("Experimente", "Digite e apague um e-mail. A tela muda imediatamente. Verifique que logado.html ainda pode ser aberta pelo link e que nenhuma senha foi enviada.", FUNDO_AZUL, VERDE),
    PageBreak(),
]

# 7. Etapa 3: serviço e HTML
historia += [
    p("Etapa 3 | Conecte o PocketBase", "titulo"),
    p("Branch de referência: etapa-03-login-pocketbase", "pequeno"),
    p("Só agora o botão Entrar ganha uma ação. Antes, confirme que o PocketBase está rodando e que a coleção Auth users contém um aluno.", "corpo"),
    p("1. Crie js/pocketbase.js", "secao"),
    codigo("window.pb = new PocketBase('http://127.0.0.1:8090');"),
    p("2. Em login.html, carregue os scripts nesta ordem", "secao"),
    codigo('''<script defer src="https://cdn.jsdelivr.net/npm/pocketbase@0.28.1/dist/pocketbase.umd.js"></script>
<script defer src="js/pocketbase.js"></script>
<script defer src="js/login.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.17.4/dist/cdn.min.js"></script>'''),
    p("O SDK define PocketBase; o arquivo de configuração cria window.pb; js/login.js define a função; Alpine lê x-data por último.", "corpo"),
    p("3. Transforme os campos em formulário", "secao"),
    codigo('''<main class="cartao" x-data="loginComPocketBase()">
  <form @submit.prevent="entrar">
    <input type="email" x-model="email" required>
    <input type="password" x-model="senha" required>
    <p x-show="erro" x-text="erro" role="alert"></p>
    <button type="submit" :disabled="carregando">
      <span x-text="carregando ? 'Entrando...' : 'Entrar'"></span>
    </button>
  </form>
</main>'''),
    p("Mantenha as labels dos dois campos. @submit.prevent executa entrar() e evita o recarregamento automático da página.", "corpo"),
    PageBreak(),
]

# 8. Etapa 3: lógica
historia += [
    p("Etapa 3 | Faça o login real", "titulo"),
    p("Substitua o conteúdo de js/login.js. A função devolve o estado inicial e a ação de entrar.", "corpo"),
    codigo('''function loginComPocketBase() {
  return {
    email: '', senha: '', erro: '', carregando: false,
    async entrar() {
      this.erro = '';
      this.carregando = true;
      try {
        await window.pb.collection('users')
          .authWithPassword(this.email, this.senha);
        window.location.href = 'logado.html';
      } catch (erro) {
        this.erro = 'Confira seus dados e o PocketBase.';
      } finally {
        this.carregando = false;
      }
    },
  };
}'''),
    p("Leia o caminho de execução", "secao"),
    *itens([
        "async/await espera o servidor responder antes de abrir outra página.",
        "authWithPassword envia e-mail e senha para a coleção Auth users.",
        "try é o caminho do sucesso; catch trata erro; finally encerra a espera nos dois casos.",
        "O SDK guarda o token de autenticação no navegador após o sucesso.",
    ]),
    aviso("Experimento", "Tente uma senha errada: continue na tela de login. Tente a correta: abra logado.html. Depois abra logado.html diretamente em outra janela; nesta etapa ela ainda não confirma a sessão.", FUNDO_AZUL, VERDE),
    p("O que significa token?", "secao"),
    p("É uma credencial emitida pelo servidor depois do login. Em pedidos posteriores, o SDK a envia ao PocketBase. Guardar um token no navegador não prova, sozinho, que a sessão ainda será aceita pelo servidor.", "corpo"),
    PageBreak(),
]

# 9. Etapa 4: lógica
historia += [
    p("Etapa 4 | Confirme a sessão", "titulo"),
    p("Branch de referência: etapa-04-sessao-e-saida; versão final: main", "pequeno"),
    p("Agora a segunda página pergunta ao PocketBase se a sessão ainda vale. Só depois mostra o usuário.", "corpo"),
    p("Em js/logado.js, crie a função da página", "secao"),
    codigo('''function paginaLogada() {
  return {
    usuario: null,
    verificando: true,
    async init() {
      if (!window.pb.authStore.isValid) {
        window.location.replace('login.html');
        return;
      }
      try {
        await window.pb.collection('users').authRefresh();
        this.usuario = window.pb.authStore.record;
      } catch (erro) {
        window.pb.authStore.clear();
        window.location.replace('login.html');
      } finally {
        this.verificando = false;
      }
    },
    sair() {
      window.pb.authStore.clear();
      window.location.replace('login.html');
    },
  };
}'''),
    p("init() é chamado quando Alpine inicia este componente. isValid faz apenas uma checagem local do prazo do token; authRefresh consulta o servidor. clear() apaga o estado de login do SDK.", "corpo"),
    PageBreak(),
]

# 10. Etapa 4: página e limite de proteção
historia += [
    p("Etapa 4 | Mostre o usuário e permita sair", "titulo"),
    p("Em logado.html, carregue os scripts na ordem: SDK do PocketBase, js/pocketbase.js, js/logado.js e Alpine.js. Use as mesmas URLs da etapa 3.", "corpo"),
    p("No corpo da página", "secao"),
    codigo('''<main class="cartao" x-data="paginaLogada()" x-cloak>
  <p x-show="verificando">Verificando login...</p>
  <section x-show="usuario">
    <h1>Área do aluno</h1>
    <p>Você entrou com:</p>
    <strong x-text="usuario && usuario.email"></strong>
    <button type="button" @click="sair">Sair</button>
  </section>
</main>'''),
    p("Enquanto verificando é verdadeiro, a página informa que está esperando. usuario começa vazio; após authRefresh, recebe o registro confirmado pelo servidor.", "corpo"),
    p("Onde os dados privados são protegidos?", "secao"),
    p("Qualquer pessoa pode baixar HTML, CSS e JS. O redirecionamento melhora o uso da página, mas dados privados precisam de regras de API no PocketBase. Em uma coleção com registros privados, uma regra de leitura para contas autenticadas pode ser:", "corpo"),
    codigo('@request.auth.id != ""'),
    aviso("Faça o teste", "Entre, atualize logado.html, clique em Sair e tente abrir a página diretamente. Depois repita em uma janela anônima. Explique em cada caso o que o navegador sabe e o que o servidor confirma.", FUNDO_LARANJA, LARANJA),
    PageBreak(),
]

# 11. Reconstrução independente
historia += [
    p("Agora reconstrua sem olhar o código pronto", "titulo"),
    p("Feche as branches de referência. Em uma pasta vazia, use este roteiro. Só consulte a branch correspondente depois de tentar localizar o problema.", "corpo"),
    p("Lista de construção", "secao"),
    *itens([
        "1. Crie login.html, logado.html, css/estilo.css, js/login.js e js/logado.js.",
        "2. Ligue o CSS e os JS ao HTML. Faça o link entre as páginas. Deixe Entrar desativado.",
        "3. Sirva os arquivos pela porta 5500. Observe os estilos nas duas páginas.",
        "4. Carregue Alpine.js, defina formulario() em js/login.js e mostre o e-mail digitado com x-model e x-text.",
        "5. Inicie o PocketBase, crie users do tipo Auth e cadastre um aluno fictício.",
        "6. Crie js/pocketbase.js. Carregue SDK, configuração, JS da página e Alpine nessa ordem.",
        "7. Ative o formulário e implemente authWithPassword com try/catch/finally.",
        "8. Em logado.html, carregue os scripts e confirme a sessão com authRefresh antes de mostrar o e-mail.",
        "9. Implemente Sair com authStore.clear() e retorno ao login.",
    ]),
    p("Critérios para dizer que terminou", "secao"),
    *itens([
        "Senha incorreta mostra erro sem abrir a área do aluno.",
        "Senha correta abre a área e mostra o e-mail cadastrado.",
        "Atualizar a página confirma a sessão novamente.",
        "Sair limpa a sessão; acesso direto sem login volta ao formulário.",
        "Você consegue explicar o papel de cada arquivo sem ler comentários.",
    ]),
    aviso("Se travar", "Compare primeiro caminhos de arquivos e ordem dos scripts. Depois confira a coleção users, o endereço do PocketBase e o console do navegador.", FUNDO_AZUL, AZUL),
    PageBreak(),
]

# 12. Diagnóstico e conceitos
historia += [
    p("Diagnóstico e próximos passos", "titulo"),
    p("Quando algo falhar, investigue uma causa por vez.", "corpo"),
    *itens([
        "Sem estilos: confira o caminho css/estilo.css no link do HTML.",
        "O e-mail não aparece na etapa 2: confira x-data, x-model, x-text e se a CDN carregou.",
        "PocketBase não responde: abra http://127.0.0.1:8090/_/ e confira js/pocketbase.js.",
        "Credenciais falham: confira se users é Auth e se o aluno foi cadastrado nela.",
        "A tela fica vazia: confira erros no console e a ordem dos scripts defer.",
        "O login parece sumir: use sempre o mesmo endereço 127.0.0.1 no navegador.",
    ]),
    p("Glossário curto", "secao"),
    *itens([
        "<b>Estado</b>: valores usados pela interface, como email ou carregando.",
        "<b>API</b>: forma de um programa pedir uma ação ou dados a outro.",
        "<b>Autenticação</b>: conferir quem está tentando entrar.",
        "<b>Sessão</b>: estado de login mantido após a autenticação.",
        "<b>Token</b>: credencial emitida pelo servidor para pedidos posteriores.",
        "<b>Regra de API</b>: condição que o servidor aplica antes de devolver dados.",
    ]),
    p("Desafios depois de concluir", "secao"),
    *itens([
        "Mude a cor do cartão e identifique qual arquivo controla esse visual.",
        "Mostre um nome cadastrado no registro do aluno, além do e-mail.",
        "Crie uma coleção de exemplo e restrinja sua leitura a usuários autenticados.",
    ]),
    p("Documentação oficial", "secao"),
    p('<link href="https://alpinejs.dev/directives/model" color="#2563EB">Alpine.js: x-model</link><br/>'
      '<link href="https://pocketbase.io/docs/authentication/" color="#2563EB">PocketBase: autenticação</link><br/>'
      '<link href="https://pocketbase.io/docs/api-rules-and-filters/" color="#2563EB">PocketBase: regras de API</link>', "corpo"),
]

doc.build(historia, onFirstPage=capa, onLaterPages=pagina)
print(DESTINO)