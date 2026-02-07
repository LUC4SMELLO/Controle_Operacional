from PIL import Image, ImageDraw, ImageFont
import locale
from datetime import datetime

from constants.paths import REPORTS_IMAGES_DIR


LARGURA = 1600
ALTURA = 1920
FUNDO = (255, 255, 255)


def paginar(lista, tamanho):
    for i in range(0, len(lista), tamanho):
        yield lista[i:i + tamanho]


def gerar_imagem_escala(escala):

    max_linhas = 16
    altura_linha = 110

    paginas = list(paginar(escala, max_linhas))

    for indice_pagina, escala_pagina in enumerate(paginas, start=1):

        img = Image.new("RGB", (LARGURA, ALTURA), FUNDO)
        draw = ImageDraw.Draw(img)

        fonte_titulo = ImageFont.truetype("arialbd.ttf", 48)
        fonte_header = ImageFont.truetype("arialbd.ttf", 28)
        fonte_texto = ImageFont.truetype("arial.ttf", 26)

        # FUNDO DO TÍTULO
        draw.rectangle([0, 4, LARGURA, 100], fill=(184, 184, 184))

        # TÍTULO
        draw.text(
            (LARGURA // 2, 50),
            "RELATÓRIO DE ENTREGA",
            fill="white",
            font=fonte_titulo,
            anchor="mm",
        )

        # DATA
        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
        objeto_data = datetime.strptime(escala[0][1], "%Y-%m-%d")
        data_formatada_extenso = objeto_data.strftime("%d de %B de %Y")

        draw.text(
            (1200, 40),
            data_formatada_extenso,
            fill="white",
            font=fonte_header
        )

        # INDICADOR DE PÁGINA
        draw.text(
            (80, 40),
            f"PÁGINA {indice_pagina}/{len(paginas)}",
            fill="white",
            font=fonte_header
        )

        # CABEÇALHO
        y = 105
        colunas = [
            ("CARGA", 0, 150),
            ("DATA/HORA", 150, 350),
            ("MOTORISTA / AJUDANTE", 350, 830),
            ("LOCALIDADE DA ENTREGA", 830, 1330),
            ("OBSERVAÇÃO", 1330, 1600),
        ]

        for titulo, x1, x2 in colunas:
            draw.rectangle([x1, y, x2, y + 50], outline="black", fill=(147, 147, 147))
            draw.text(
                ((x1 + x2) / 2, y + 25),
                titulo,
                fill="white",
                font=fonte_header,
                anchor="mm",
            )

        y += 50

        # LINHAS
        for i, item in enumerate(escala_pagina):

            item_lista = list(item)

            try:
                objeto_data = datetime.strptime(str(item_lista[1]), "%Y-%m-%d")
                item_lista[1] = objeto_data.strftime("%d/%m/%Y")
            except Exception:
                item_lista[1] = ""

            fundo = (236, 236, 236) if i % 2 == 0 else (255, 255, 255)

            dados = [
                item[2],
                f"{item_lista[1]}\n{item[11]}",
                f"{item[3]}\n{item[4] or ''}\n{item[5] or ''}",
                item[6],
                item[8],
            ]

            for j, (texto, (_, x1, x2)) in enumerate(zip(dados, colunas)):
                draw.rectangle(
                    [x1, y, x2, y + altura_linha],
                    outline="black",
                    fill=fundo
                )

                if j == 2:
                    posicao = (x1 + 10, y + altura_linha / 2)
                    ancora = "lm"
                    alinhamento = "left"
                else:
                    posicao = ((x1 + x2) / 2, y + altura_linha / 2)
                    ancora = "mm"
                    alinhamento = "center"

                draw.multiline_text(
                    posicao,
                    texto,
                    fill="black",
                    font=fonte_texto,
                    anchor=ancora,
                    align=alinhamento,
                    spacing=10,
                )

            y += altura_linha

        # SALVA A IMAGEM
        img.save(
            REPORTS_IMAGES_DIR / f"relatorio_entrega_{indice_pagina}.png"
        )
