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
            (250, 40),
            f"PÁGINA {indice_pagina}/{len(paginas)}",
            fill="white",
            font=fonte_header
        )

        # CABEÇALHO
        y = 105
        colunas = [
            ("CARGA", 0, 150),
            ("DATA / HORA", 150, 350),
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

def gerar_imagem_mapa_troca(infomacoes):
        
    # Criar imagem branca
    largura = 1190
    altura = 1684

    img = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(img)

    # =========================
    # FUNÇÕES AUXILIARES
    # =========================

    def desenhar_cupom(y_topo, numero_carga_1, numero_carga_2):

        # aumentou altura
        altura_cupom = 250

        y_caixa = y_topo

        # caixa principal
        retangulo(60, y_caixa, 1130, y_caixa + altura_cupom, 2)

        # linha central
        linha(595, y_caixa, 595, y_caixa + altura_cupom)

        # ========================================
        # LADO ESQUERDO
        # ========================================

        draw.text((95, y_caixa + 15), "COD/NOME:", fill="black", font=fonte)

        draw.text(
            (460, y_caixa + 15),
            f"Nº Carga - {numero_carga_1}",
            fill="black",
            font=fonte
        )

        linha(60, y_caixa + 40, 595, y_caixa + 40)

        draw.text(
            (95, y_caixa + 45),
            "QUANT.",
            fill="black",
            font=fonte_label
        )

        draw.text(
            (200, y_caixa + 45),
            "DESCRIÇÃO ITEM",
            fill="black",
            font=fonte_label
        )

        draw.text(
            (475, y_caixa + 45),
            "CÓDIGO",
            fill="black",
            font=fonte_label
        )

        # linhas da tabela
        y = y_caixa + 70

        for i in range(6):  # aumentou quantidade de linhas
            linha(60, y, 595, y)
            y += 25

        # linhas verticais
        linha(185, y_caixa + 40, 185, y_caixa + altura_cupom - 55)
        linha(460, y_caixa + 40, 460, y_caixa + altura_cupom - 55)

        # ========================================
        # ASSINATURA
        # ========================================

        # alinhado com COD/NOME
        linha_assinatura_y = y_caixa + 220

        draw.text(
            (95, linha_assinatura_y),
            "ASSINATURA:",
            fill="black",
            font=fonte_label
        )

        # linha maior
        linha(
            250,
            linha_assinatura_y + 15,
            560,
            linha_assinatura_y + 15,
            2
        )

        # ========================================
        # LADO DIREITO
        # ========================================

        draw.text((640, y_caixa + 15), "COD/NOME:", fill="black", font=fonte)

        draw.text(
            (1000, y_caixa + 15),
            f"Nº Carga - {numero_carga_2}",
            fill="black",
            font=fonte
        )

        linha(595, y_caixa + 40, 1130, y_caixa + 40)

        draw.text(
            (640, y_caixa + 45),
            "QUANT.",
            fill="black",
            font=fonte_label
        )

        draw.text(
            (740, y_caixa + 45),
            "DESCRIÇÃO ITEM",
            fill="black",
            font=fonte_label
        )

        draw.text(
            (1015, y_caixa + 45),
            "CÓDIGO",
            fill="black",
            font=fonte_label
        )

        y = y_caixa + 70

        for i in range(6):
            linha(595, y, 1130, y)
            y += 25

        linha(725, y_caixa + 40, 725, y_caixa + altura_cupom - 55)
        linha(1000, y_caixa + 40, 1000, y_caixa + altura_cupom - 55)

        # assinatura direita
        draw.text(
            (640, linha_assinatura_y),
            "ASSINATURA:",
            fill="black",
            font=fonte_label
        )

        linha(
            795,
            linha_assinatura_y + 15,
            1100,
            linha_assinatura_y + 15,
            2
        )

        return y_caixa + altura_cupom

    def linha(x1, y1, x2, y2, largura_linha=1):
        draw.line((x1, y1, x2, y2), fill="black", width=largura_linha)

    def retangulo(x1, y1, x2, y2, largura_linha=1):
        draw.rectangle((x1, y1, x2, y2), outline="black", width=largura_linha)

    # Fonte
    try:
        fonte = ImageFont.truetype("arial.ttf", 16)
        fonte_label = ImageFont.truetype("arialbd.ttf", 18)
        fonte_titulo = ImageFont.truetype("arialbd.ttf", 22)
    except:
        fonte = ImageFont.load_default()
        fonte_titulo = ImageFont.load_default()

    # =========================
    # BORDA EXTERNA
    # =========================

    retangulo(50, 40, 1140, 1630, 2)

    # =========================
    # CABEÇALHO
    # =========================

    retangulo(60, 50, 1130, 160, 2)

    # Logo
    draw.text((95, 80), "LOGO", fill="black", font=fonte)

    # Título
    draw.text((450, 70), "GUIA DE ENTREGA", fill="black", font=fonte_titulo)

    # Dados superiores
    draw.text((945, 70), "Nº Carga:", fill="black", font=fonte_label)
    draw.text((1035, 72), "7341001", fill="black", font=fonte)


    draw.text((95, 120), "Motorista:", fill="black", font=fonte_label)
    draw.text((190, 122), "Nome do Motorista", fill="black", font=fonte)
    draw.text((400, 120), "Veículo:", fill="black", font=fonte_label)
    draw.text((480, 122), "Número do Veículo", fill="black", font=fonte)

    draw.text((685, 120), "Nome da Rota", fill="black", font=fonte_label)

    draw.text((874, 120), "sexta-feira, 13 de maio de 2026", fill="black", font=fonte)

    # =========================
    # INFORMAÇÕES
    # =========================

    draw.text((95, 175), "Horário Saída:", fill="black", font=fonte_label)
    linha(225, 192, 370, 192)
    draw.text((400, 175), "Horário Chegada:", fill="black", font=fonte_label)
    linha(560, 192, 705, 192)

    draw.text((735, 175), "Terceiro Ajudante:", fill="black", font=fonte_label)
    linha(901, 192, 1096, 192)

    draw.text((126, 215), "Km Inicial:", fill="black", font=fonte_label)
    linha(225, 232, 370, 232)
    draw.text((468, 215), "Km Final:", fill="black", font=fonte_label)
    linha(560, 232, 705, 232)

    draw.text((760, 215), "Nº de Entregas:", fill="black", font=fonte_label)
    linha(901, 232, 1096, 232)

    # =========================
    # VASILHAMES
    # =========================

    retangulo(60, 250, 1130, 570, 2)

    draw.text((110, 270), "VASILHAMES", fill="black", font=fonte_label)
    draw.text((275, 270), "CARREGADO", fill="black", font=fonte_label)
    draw.text((440, 270), "RETORNADO", fill="black", font=fonte_label)
    draw.text((620, 270), "VENDIDO", fill="black", font=fonte_label)

    draw.text((100, 315), "KS", fill="black", font=fonte)
    draw.text((100, 345), "LS", fill="black", font=fonte)
    draw.text((100, 375), "REF", fill="black", font=fonte)
    draw.text((100, 405), "600ML PILSEN", fill="black", font=fonte)
    draw.text((100, 435), "600ML EST.GAL", fill="black", font=fonte)
    draw.text((100, 465), "600ML THZ", fill="black", font=fonte)
    draw.text((100, 495), "CILINDRO DE GÁS", fill="black", font=fonte)
    draw.text((100, 525), "CAIXA VAZIA", fill="black", font=fonte)


    y = 305
    for i in range(9):
        linha(95, y, 745, y)
        y += 30
    linha(95, 305, 95, 545)
    linha(250, 305, 250, 545)
    linha(415, 305, 415, 545)
    linha(580, 305, 580, 545)
    linha(745, 305, 745, 545)



    draw.text((861, 270), "EQUIPAMENTOS", fill="black", font=fonte_label)
    draw.text((806, 310), "CARREGADO", fill="black", font=fonte_label)
    draw.text((961, 310), "RETORNADO", fill="black", font=fonte_label)
    draw.text((791, 345), "MESA", fill="black", font=fonte)
    draw.text((791, 375), "CADEIRA", fill="black", font=fonte)
    draw.text((791, 405), "GELADEIRA", fill="black", font=fonte)

    y=305
    for i in range(9):
        linha(786, y, 1096, y)
        y += 30
    linha(786, 305, 786, 545)
    linha(941, 305, 941, 545)
    linha(1096, 305, 1096, 545)

    # =========================
    # TROCA DE MERCADORIAS
    # =========================

    texto_grande = """
    Este texto pode aumentar ou diminuir.
    Dependendo da quantidade de linhas,
    os cupons precisam descer automaticamente.
    """

    bbox = draw.multiline_textbbox(
        (60, 400),
        texto_grande,
        font=fonte,
        spacing=10
    )

    altura_texto = bbox[3]

    # =========================
    # CUPONS
    # =========================

    draw.text((320, altura_texto + 90), "CUPONS PARA PREENCHER EM CASO DE TROCA", fill="black", font=fonte_titulo)

    y_inicial = altura_texto + 120
    altura_pagina = 1600

    y_atual = y_inicial


    contador = 1
    while True:

        altura_total_cupom = 245

        # verifica se ainda cabe
        if y_atual + altura_total_cupom > altura_pagina:
            break

        fim = desenhar_cupom(
            y_atual,
            f"{contador:02}",
            f"{contador+1:02}"
        )

        y_atual = fim

        contador += 2



        # SALVA A IMAGEM
        img.save(
            REPORTS_IMAGES_DIR / "mapa.png"
        )

