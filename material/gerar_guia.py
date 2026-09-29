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
              p("CONCEITO PRINCIPAL", "cabecalho_tabela"),
              p("BRANCH", "cabecalho_tabela")]]
    etapas = [
        ("01", "HTML e navegação entre páginas", "etapa-01-html-estatico"),
        ("02", "Formulário reativo, sem autenticação", "etapa-02-alpine"),
        ("03", "Login real com PocketBase", "etapa-03-login-pocketbase"),
        ("04", "Confirmar sessão e sair", "etapa-04-sessao-e-saida"),
        ("05", "Organizar os arquivos", "etapa-05-arquivos-organizados"),
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
    title="Guia passo a passo: login com PocketBase e Alpine.js",
    author="Material de apoio para alunos",
)
historia = []

# Capa
historia += [
    Spacer(1, 19 * mm),
    p("CADERNO DE APOIO | PROJETO GUIADO", "sobretitulo"),
    p("Login simples com<br/>PocketBase e Alpine.js", "capa"),
    p("Duas páginas, um formulário e uma autenticação. Vamos construir cada ideia em uma etapa.", "subcapa"),
    Spacer(1, 5 * mm),
    aviso(
        "O que vamos construir",
        "O navegador mostra as páginas. Alpine.js lê os campos e responde aos eventos. PocketBase confere a conta do aluno no servidor.",
        FUNDO_AZUL, VERDE,
    ),
    Spacer(1, 7 * mm),
    p("As cinco etapas", "secao"),
    tabela_capa(),
    Spacer(1, 8 * mm),
    aviso(
        "Como usar este guia",
        "Abra a branch de cada etapa, leia os comentários nos arquivos e faça os experimentos. Cada branch mostra o código completo daquele momento da aula.",
        FUNDO, AZUL,
    ),
    p("Público: alunos iniciantes em HTML, CSS e JavaScript.", "pequeno"),
    PageBreak(),
]

# 2. Visão geral e preparação
historia += [
    p("Antes de começar", "titulo"),
    p("O aluno informa e-mail e senha. A página envia esses valores ao PocketBase. Se o servidor aceitar a conta, o navegador abre a área do aluno.", "corpo"),
    codigo("aluno -> login.html -> Alpine.js -> PocketBase -> logado.html"),
    Spacer(1, 5),
    p("Papel de cada tecnologia", "secao"),
]
linhas = [
    [p("TECNOLOGIA", "cabecalho_tabela"), p("PAPEL", "cabecalho_tabela")],
    [p("HTML", "celula_forte"), p("Cria as duas páginas, os campos e os botões.", "celula")],
    [p("CSS", "celula_forte"), p("Define aparência e espaçamento.", "celula")],
    [p("Alpine.js", "celula_forte"), p("Liga valores dos campos ao JavaScript e responde aos eventos.", "celula")],
    [p("PocketBase", "celula_forte"), p("Guarda contas e valida as credenciais no servidor.", "celula")],
]
tabela = Table(linhas, colWidths=[37 * mm, 133 * mm])
tabela.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
    ("GRID", (0, 0), (-1, -1), 0.45, BORDA),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
historia += [
    tabela, Spacer(1, 7),
    p("Prepare o PocketBase", "secao"),
    *itens([
        "Baixe o PocketBase para seu sistema e extraia o executável.",
        "Inicie o servidor com o comando abaixo.",
        "Abra http://127.0.0.1:8090/_/ e crie uma conta de administrador.",
        "Crie uma coleção do tipo Auth chamada users e cadastre um aluno com e-mail e senha.",
    ]),
    codigo(r".\pocketbase.exe serve"),
    Spacer(1, 6),
    p("Abra as páginas", "secao"),
    p("Mantenha o PocketBase rodando. Em outro terminal, na pasta do projeto:", "corpo"),
    codigo("py -m http.server 5500\nhttp://127.0.0.1:5500/login.html"),
    Spacer(1, 6),
    aviso(
        "Use o mesmo endereço",
        "Neste projeto, use 127.0.0.1 no navegador e em js/pocketbase.js. localhost e 127.0.0.1 podem ter armazenamentos de login separados.",
        FUNDO, LARANJA,
    ),
    PageBreak(),
]

# 3. HTML
historia += [
    p("Etapa 1 | HTML estático", "titulo"),
    p("Branch: <b>etapa-01-html-estatico</b>", "pequeno"),
    p("As duas páginas já existem. O objetivo é reconhecer os elementos HTML e entender que um link apenas navega.", "corpo"),
    p("O que observar", "secao"),
    *itens([
        "h1 identifica o título principal.",
        "label descreve um campo de input.",
        "input recebe o texto digitado.",
        "a com href aponta para outra página.",
    ]),
    codigo('<label for="email">E-mail</label>\n<input id="email" type="email">\n<a href="logado.html">Ver a segunda página</a>'),
    Spacer(1, 8),
    aviso(
        "O link não faz login",
        "Os campos são visuais nesta etapa. A página logado.html pode ser aberta diretamente, mesmo sem e-mail ou senha.",
        FUNDO_LARANJA, LARANJA,
    ),
    p("Faça você mesmo", "secao"),
    *itens([
        "Clique em Ver a segunda página sem digitar nada.",
        "Abra logado.html diretamente na barra de endereços.",
        "Altere o título h1 e observe a página no navegador.",
    ]),
    aviso(
        "Pense antes de avançar",
        "O que teria de acontecer para o programa conferir uma conta de aluno? Primeiro vamos aprender a reação do formulário; depois enviaremos dados ao servidor.",
        FUNDO, VERDE,
    ),
    PageBreak(),
]

# 4. Alpine
historia += [
    p("Etapa 2 | Formulário com Alpine.js", "titulo"),
    p("Branch: <b>etapa-02-alpine</b>", "pequeno"),
    p("Alpine.js liga os campos a variáveis. O envio chama uma função, que mostra uma mensagem na própria página. Ainda não existe autenticação.", "corpo"),
    p("Quatro atributos importantes", "secao"),
    *itens([
        "x-data define os dados e as funções desta parte do HTML.",
        "x-model acompanha o valor digitado.",
        "@submit.prevent chama enviar() sem recarregar a página.",
        "x-show e x-text mostram a mensagem apropriada.",
    ]),
    codigo('<main x-data="formulario()">\n  <form @submit.prevent="enviar">\n    <input x-model="email">\n    <p x-show="mensagem" x-text="mensagem"></p>\n  </form>\n</main>'),
    Spacer(1, 8),
    aviso(
        "O que o código faz",
        "Ele lê os campos e exibe uma confirmação local. Não compara senhas, não envia dados ao servidor e não abre a área do aluno. A senha é limpa e não aparece na mensagem.",
        FUNDO_AZUL, VERDE,
    ),
    p("Faça você mesmo", "secao"),
    *itens([
        "Envie os campos vazios e observe o erro.",
        "Use um e-mail com formato válido e uma senha qualquer.",
        "Veja a mensagem e confirme que a senha não aparece nela.",
    ]),
    aviso(
        "Conceito-chave",
        "O estado de x-data vive na página. Ele serve para controlar a interface; uma mensagem de sucesso na tela não comprova a identidade de ninguém.",
        FUNDO_LARANJA, LARANJA,
    ),
    PageBreak(),
]

# 5. PocketBase
historia += [
    p("Etapa 3 | Login com PocketBase", "titulo"),
    p("Branch: <b>etapa-03-login-pocketbase</b>", "pequeno"),
    p("Agora o formulário chama o PocketBase. A coleção users deve ser do tipo Auth e conter o aluno que você vai usar no experimento.", "corpo"),
    p("O endereço do servidor", "secao"),
    codigo("window.pb = new PocketBase('http://127.0.0.1:8090');"),
    p("O SDK é uma biblioteca que prepara as chamadas à API e mantém o estado do login no navegador.", "corpo"),
    p("A chamada de autenticação", "secao"),
    codigo("await window.pb\n  .collection('users')\n  .authWithPassword(this.email, this.senha);"),
    *itens([
        "collection('users') escolhe a coleção das contas dos alunos.",
        "authWithPassword pede ao servidor que confira e-mail e senha.",
        "await aguarda a resposta antes do redirecionamento.",
        "try/catch separa o resultado aceito do erro.",
    ]),
    p("Após o login, o SDK guarda um token e um registro de usuário. A página abre logado.html. Esta etapa ainda permite abrir logado.html diretamente sem uma confirmação adicional.", "corpo"),
    aviso(
        "Token em poucas palavras",
        "O servidor emite um token após aceitar as credenciais. O SDK o guarda no navegador e o envia em pedidos autenticados posteriores.",
        FUNDO_AZUL, AZUL,
    ),
    p("Faça você mesmo", "secao"),
    *itens([
        "Tente entrar com uma senha errada.",
        "Entre com o aluno cadastrado no painel do PocketBase.",
        "Abra logado.html em uma janela anônima e observe o limite desta etapa.",
    ]),
    PageBreak(),
]

# 6. Sessão
historia += [
    p("Etapa 4 | Confirmar a sessão e sair", "titulo"),
    p("Branch: <b>etapa-04-sessao-e-saida</b>", "pequeno"),
    p("Ao abrir a área do aluno, usamos dois passos: primeiro verificamos o token salvo localmente; depois pedimos ao PocketBase para confirmá-lo.", "corpo"),
    codigo("if (!window.pb.authStore.isValid) {\n  window.location.replace('login.html');\n  return;\n}\nawait window.pb.collection('users').authRefresh();"),
    Spacer(1, 5),
    *itens([
        "isValid verifica apenas se existe um token local ainda não expirado.",
        "authRefresh faz uma chamada ao servidor e atualiza o token e o registro.",
        "Enquanto a resposta não chega, a tela diz Verificando login.",
        "Se a confirmação falhar, o código limpa o estado e volta ao login.",
    ]),
    p("Para sair, limpamos o estado salvo pelo SDK:", "corpo"),
    codigo("window.pb.authStore.clear();\nwindow.location.replace('login.html');"),
    Spacer(1, 7),
    aviso(
        "Onde fica a proteção dos dados?",
        "O navegador pode baixar os arquivos HTML e JavaScript. Para dados privados de outras coleções, configure as regras de API no PocketBase. Uma regra de leitura só para usuários autenticados é @request.auth.id != \"\".",
        FUNDO_LARANJA, LARANJA,
    ),
    p("Faça você mesmo", "secao"),
    *itens([
        "Entre e atualize a página: o servidor confirma a sessão novamente?",
        "Clique em Sair e abra logado.html diretamente.",
        "Abra uma janela anônima e tente visitar logado.html sem login.",
    ]),
    PageBreak(),
]

# 7. Organização
historia += [
    p("Etapa 5 | Organizar os arquivos", "titulo"),
    p("Branch: <b>etapa-05-arquivos-organizados</b> e versão final: <b>main</b>", "pequeno"),
    p("Movemos o CSS e o JavaScript para arquivos próprios. As funções de login e da área do aluno são as mesmas da etapa 4; só mudou onde elas estão escritas.", "corpo"),
    codigo("login.html\nlogado.html\ncss/estilo.css\njs/pocketbase.js\njs/login.js\njs/logado.js"),
    p("Responsabilidade de cada arquivo", "secao"),
    *itens([
        "login.html contém o formulário; logado.html contém a área do aluno.",
        "css/estilo.css guarda estilos usados nas duas páginas.",
        "js/pocketbase.js aponta para o servidor.",
        "js/login.js envia as credenciais.",
        "js/logado.js confirma a sessão, mostra o e-mail e permite sair.",
    ]),
    p("Por que a ordem dos scripts importa?", "secao"),
    codigo('<script defer src="...pocketbase.umd.js"></script>\n<script defer src="js/pocketbase.js"></script>\n<script defer src="js/login.js"></script>\n<script defer src="...alpine.min.js"></script>'),
    p("O navegador lê o HTML e depois executa os scripts defer na ordem escrita. O SDK precisa existir antes de js/pocketbase.js; a função da página precisa existir antes de Alpine iniciar.", "corpo"),
    aviso(
        "Volte a uma etapa",
        "Use git switch etapa-01-html-estatico para ver o primeiro exemplo. Avance uma branch por vez e use git switch main para voltar à versão final.",
        FUNDO_AZUL, VERDE,
    ),
    PageBreak(),
]

# 8. Verificação e problemas
historia += [
    p("Verificar e resolver problemas", "titulo"),
    p("Se o login não funcionar, siga o caminho da requisição e confira uma parte por vez.", "corpo"),
    *itens([
        "O painel abre em http://127.0.0.1:8090/_/?",
        "A coleção se chama exatamente users e é do tipo Auth?",
        "O aluno foi cadastrado em users, com e-mail e senha?",
        "A página abriu por http://127.0.0.1:5500/login.html?",
        "js/pocketbase.js usa o endereço certo?",
        "Há internet para carregar Alpine.js e o SDK pelos links CDN?",
    ]),
    p("Verificação manual do fluxo", "secao"),
    *itens([
        "Senha errada: permanece no login e mostra uma mensagem.",
        "Credenciais certas: abre a área do aluno e mostra o e-mail.",
        "Atualização da área: exibe Verificando login e consulta o servidor.",
        "Sair: limpa o login e volta ao formulário.",
        "Acesso direto sem sessão: retorna ao login.",
    ]),
    p("Sintomas frequentes", "secao"),
]
linhas = [
    [p("SINTOMA", "cabecalho_tabela"), p("CAUSA PROVÁVEL", "cabecalho_tabela"), p("CONFIRA", "cabecalho_tabela")],
    [p("Não conecta", "celula"), p("PocketBase parado ou endereço diferente", "celula"), p("Terminal e js/pocketbase.js", "celula")],
    [p("Login falha", "celula"), p("Dados ou coleção incorretos", "celula"), p("Registro em users", "celula")],
    [p("Estilo não aparece", "celula"), p("Caminho do CSS incorreto", "celula"), p("css/estilo.css no HTML", "celula")],
    [p("Tela invisível", "celula"), p("Alpine ou outro script não carregou", "celula"), p("Internet e console", "celula")],
]
tabela = Table(linhas, colWidths=[45 * mm, 65 * mm, 60 * mm])
tabela.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
    ("GRID", (0, 0), (-1, -1), 0.45, BORDA),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
historia += [
    tabela, Spacer(1, 8),
    aviso(
        "Uma mudança por vez",
        "Leia a primeira mensagem vermelha no console do navegador, compare os caminhos dos arquivos e corrija um problema por vez.",
        FUNDO, AZUL,
    ),
    PageBreak(),
]

# 9. Glossário e desafios
historia += [
    p("Glossário e desafios", "titulo"),
    p("Palavras usadas no projeto", "secao"),
    *itens([
        "<b>API</b>: interface pela qual um programa pede dados ou serviços a outro.",
        "<b>Autenticação</b>: conferir quem está tentando entrar.",
        "<b>Coleção Auth</b>: coleção especial do PocketBase para contas de usuário.",
        "<b>Estado</b>: valores em uso na tela, como e-mail, erro ou mensagem.",
        "<b>Token</b>: credencial emitida pelo servidor após o login.",
        "<b>Redirecionamento</b>: abrir outra URL por link ou JavaScript.",
        "<b>Regra de API</b>: condição aplicada pelo servidor ao acesso a uma coleção.",
    ]),
    p("Desafios para continuar", "secao"),
    *itens([
        "Adicione um nome ao registro do aluno e mostre-o na área logada.",
        "Mude o texto do botão durante a espera pela autenticação.",
        "Altere a cor principal em css/estilo.css e observe as duas páginas.",
        "Crie uma coleção de exemplo e permita leitura apenas a usuários autenticados.",
    ]),
    p("Documentação oficial", "secao"),
    p(
        '<link href="https://pocketbase.io/docs/authentication/" color="#2563EB">Autenticação no PocketBase</link><br/>'
        '<link href="https://pocketbase.io/docs/api-rules-and-filters/" color="#2563EB">Regras de API do PocketBase</link><br/>'
        '<link href="https://alpinejs.dev/directives/data" color="#2563EB">x-data no Alpine.js</link>',
        "corpo",
    ),
    Spacer(1, 10),
    aviso(
        "Ao terminar",
        "Você terá visto a diferença entre uma página estática, um formulário reativo, uma autenticação no servidor e uma regra que protege dados.",
        FUNDO_AZUL, VERDE,
    ),
]

doc.build(historia, onFirstPage=capa, onLaterPages=pagina)
print(DESTINO)