from PIL import Image, ImageDraw, ImageFont
import locale
from datetime import datetime

from constants.paths import IMAGES_DIR

LARGURA = 1600
ALTURA = 2000
FUNDO = (255, 255, 255)


ESCALA = [
    {
        "numero_carga": "7172801",
        "data": "28/11/2026",
        "data_saida": "29/11/2026",
        "numero_rota": "EXTREMA (SEG) JD.EUROPA/P.ALTA",
        "motorista": "Leterie Wesley Pinheiro",
        "ajudante_1": "Tomas de Oliveira Rangel dos Santos",
        "ajudante_2": "Paulo Sérgio Viana",
        "caminhao": "17",
        "horario": "06:00",
        "observacao": "ROTA",
    },
    {
        "numero_carga": "7342801",
        "data": "28/11/2026",
        "data_saida": "29/11/2026",
        "numero_rota": "BUENO BRANDÃO (SEG) CENTRO",
        "motorista": "Benedito Antônio Simão",
        "ajudante_1": "Ygor Ricardo da Silva",
        "ajudante_2": "",
        "caminhao": "34",
        "horario": "07:30",
        "observacao": "MERCADOS",
    }
]

def gerar_imagem_escala():
    img = Image.new("RGB", (LARGURA, ALTURA), FUNDO)
    draw = ImageDraw.Draw(img)

    fonte_titulo = ImageFont.truetype("arial.ttf", 48)
    fonte_header = ImageFont.truetype("arial.ttf", 28)
    fonte_texto = ImageFont.truetype("arial.ttf", 26)

    # D.A Cambuí
    draw.rectangle([0, 20, LARGURA, 100], fill=(255, 255, 255))
    draw.text(
        (LARGURA // 2, 60),
        "DISTRIBUIDORA DE BEBIDAS CAMBUÍ LTDA - DIÁRIO DE CARGAS",
        fill="black",
        font=fonte_titulo,
        anchor="mm",
    )

    # Fundo Amarelo
    draw.rectangle([0, 100, LARGURA, 180], fill=(255, 255, 0))

    logo = Image.open(IMAGES_DIR / "logo_dbcambui_2.png").convert(
        "RGBA"
    )  # Abre e garante transparência
    logo = logo.resize((100, 100))  # Redimensiona para caber na altura do retângulo

    # Colar o Logo (Posição X=20, Y=110 para centralizar verticalmente no retângulo)
    img.paste(logo, (200, 90), logo)


    # Título
    draw.text(
        (LARGURA // 2, 140),
        "Relatório de Entrega",
        fill="red",
        font=fonte_titulo,
        anchor="mm",
    )

    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    data_hoje = datetime.now().strftime("%d de %B de %Y")
    draw.text((1100, 130), data_hoje, fill="red", font=fonte_header)

    # Cabeçalho da tabela
    y = 220
    colunas = [
        ("CARGA", 0, 120),
        ("DATA/HORA", 120, 320),
        ("MOTORISTA / AJUDANTE", 320, 800),
        ("LOCALIDADE DA ENTREGA", 800, 1300),
        ("OBSERVAÇÃO", 1300, 1600),
    ]

    for titulo, x1, x2 in colunas:
        # Desenha o retângulo cinza
        draw.rectangle([x1, y, x2, y + 50], outline="black", fill=(190, 190, 190))

        # Calcula o centro exato da célula do cabeçalho
        meio_x = (x1 + x2) / 2
        meio_y = y + 25  # 25 é a metade da altura (50) do cabeçalho

        # Escreve o texto usando ancoragem no meio (mm)
        draw.text((meio_x, meio_y), titulo, fill="white", font=fonte_header, anchor="mm")

    y += 50


    for i, item in enumerate(ESCALA):
        altura_linha = 110
        fundo = (230, 230, 230) if i % 2 == 0 else (255, 255, 255)

        dados = [
            item["numero_carga"],
            f"{item["data"]}\n{item["horario"]}",
            f"{item["motorista"]}\n{item["ajudante_1"]}\n{item["ajudante_2"]}",
            item["numero_rota"],
            item["observacao"],
        ]

        for j, (texto, (titulo, x1, x2)) in enumerate(zip(dados, colunas)):
            draw.rectangle([x1, y, x2, y + altura_linha], outline="black", fill=fundo)

            # Se for a coluna de Motorista (índice 2)
            if j == 2:
                # Alinha à esquerda com um pequeno recuo (x1 + 10)
                # anchor="lm" (Left-Middle) centraliza apenas a altura
                posicao = (x1 + 10, y + (altura_linha / 2))
                ancora = "lm"
                alinhamento_multiline = "left"
            else:
                # Mantém centralizado para as outras colunas
                posicao = ((x1 + x2) / 2, y + (altura_linha / 2))
                ancora = "mm"
                alinhamento_multiline = "center"

            draw.multiline_text(
                posicao,
                texto,
                fill="black",
                font=fonte_texto,
                anchor=ancora,
                align=alinhamento_multiline,
            )

        y += altura_linha

    img.save("relatorio_entrega.png")
