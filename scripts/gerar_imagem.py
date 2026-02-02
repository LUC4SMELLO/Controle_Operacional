from PIL import Image, ImageDraw, ImageFont
import locale
from datetime import datetime

LARGURA = 1600
ALTURA = 1920
FUNDO = (255, 255, 255)


ESCALA = [
    {"numero_carga": "7172801", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "EXTREMA (SEG) JD.EUROPA/P.ALTA", "motorista": "Leterie Wesley Pinheiro", "ajudante_1": "Tomas de Oliveira Rangel dos Santos", "ajudante_2": "Paulo Sérgio Viana", "caminhao": "17", "horario": "06:00", "observacao": "ROTA"},
    {"numero_carga": "7342801", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "BUENO BRANDÃO (SEG) CENTRO", "motorista": "Benedito Antônio Simão", "ajudante_1": "Ygor Ricardo da Silva", "ajudante_2": "", "caminhao": "34", "horario": "07:30", "observacao": "MERCADOS"},
    {"numero_carga": "7452802", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "POUSO ALEGRE (SUL) DISTRITO", "motorista": "Marcos Roberto Silva", "ajudante_1": "Wesley Michel do Nascimento Coutrin", "ajudante_2": "João Pedro", "caminhao": "12", "horario": "05:00", "observacao": "ROTA"},
    {"numero_carga": "7562803", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "CAMBUÍ (CENTRO) NOTURNO", "motorista": "Carlos Eduardo Lima", "ajudante_1": "Samuel Mendes", "ajudante_2": "", "caminhao": "08", "horario": "18:00", "observacao": "URGENTE"},
    {"numero_carga": "7672804", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "ITAJUBA (OESTE) VILA", "motorista": "André Luiz Souza", "ajudante_1": "Felipe Garcia", "ajudante_2": "Bruno Costa", "caminhao": "22", "horario": "06:30", "observacao": "ROTA"},
    {"numero_carga": "7782805", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "VARGINHA (NORTE) SHOPPING", "motorista": "José Aparecido Bento", "ajudante_1": "Tiago Ferreira", "ajudante_2": "", "caminhao": "45", "horario": "08:00", "observacao": "MERCADOS"},
    {"numero_carga": "7892806", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "BRAGANÇA (ESTRADA) DIST.", "motorista": "Fernando Henrique Santos", "ajudante_1": "Lucas Oliveira", "ajudante_2": "Gabriel Silva", "caminhao": "19", "horario": "04:30", "observacao": "ROTA"},
    {"numero_carga": "7902807", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "CAMANDUCAIA (VILA) SERRA", "motorista": "Roberto Carlos Justo", "ajudante_1": "Matheus Pereira", "ajudante_2": "", "caminhao": "05", "horario": "07:00", "observacao": "MERCADOS"},
    {"numero_carga": "8012808", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "SENADOR AMARAL (RURAL)", "motorista": "Gilberto Guedes", "ajudante_1": "Wellington Souza", "ajudante_2": "Igor Lemos", "caminhao": "11", "horario": "05:45", "observacao": "ROTA"},
    {"numero_carga": "8122809", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "ATIBAIA (SEG) INDUSTRIAL", "motorista": "Alexandre Magno", "ajudante_1": "Danilo Cruz", "ajudante_2": "", "caminhao": "28", "horario": "06:15", "observacao": "FABRICA"},
    {"numero_carga": "8232810", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "GONÇALVES (MONTANHA) TUR.", "motorista": "Luiz Gustavo Ramos", "ajudante_1": "Caio Vinícius", "ajudante_2": "Rafael Lima", "caminhao": "14", "horario": "07:45", "observacao": "ROTA"},
    {"numero_carga": "8342811", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "SOCORRO (LAGO) CIRCUITO", "motorista": "Marcelo Vieira", "ajudante_1": "Vinícius Júnior", "ajudante_2": "", "caminhao": "31", "horario": "09:00", "observacao": "ENTREGA"},
    {"numero_carga": "8452812", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "JOANÓPOLIS (CENTRO) CACHOEIRA", "motorista": "Renato Garcia", "ajudante_1": "Douglas Silva", "ajudante_2": "Vitor Hugo", "caminhao": "25", "horario": "06:00", "observacao": "ROTA"},
    {"numero_carga": "8562813", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "MONTE VERDE (SEG) HOTELARIA", "motorista": "Leandro Dantas", "ajudante_1": "Fabio Junior", "ajudante_2": "", "caminhao": "09", "horario": "05:30", "observacao": "ROTA"},
    {"numero_carga": "8672814", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "PIRACAIA (CENTRO) REPRESA", "motorista": "Sérgio Murilo", "ajudante_1": "Erick Prado", "ajudante_2": "Otávio Augusto", "caminhao": "37", "horario": "07:15", "observacao": "MERCADOS"},
    {"numero_carga": "8782815", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "PARAISÓPOLIS (SUL) IND.", "motorista": "Adilson Figueira", "ajudante_1": "Hugo Leonardo", "ajudante_2": "", "caminhao": "21", "horario": "06:45", "observacao": "ROTA"},
    {"numero_carga": "8892816", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "TOLEDO (MG) PERIFERIA", "motorista": "Fabiano Estevão", "ajudante_1": "Júlio César", "ajudante_2": "Breno Rocha", "caminhao": "15", "horario": "08:30", "observacao": "ROTA"},
    {"numero_carga": "8902817", "data": "28/11/2026", "data_saida": "29/11/2026", "numero_rota": "MUNHOZ (SEG) ALTO", "motorista": "Paulo Henrique", "ajudante_1": "Gustavo Henrique", "ajudante_2": "", "caminhao": "03", "horario": "06:00", "observacao": "MERCADOS"}
]


def gerar_imagem_escala():
    img = Image.new("RGB", (LARGURA, ALTURA), FUNDO)
    draw = ImageDraw.Draw(img)

    fonte_titulo = ImageFont.truetype("arialbd.ttf", 48)
    fonte_header = ImageFont.truetype("arialbd.ttf", 28)
    fonte_texto = ImageFont.truetype("arial.ttf", 26)

    # Fundo Cinza
    draw.rectangle([0, 4, LARGURA - 0, 100], fill=(184, 184, 184))

    # Título
    draw.text(
        (LARGURA // 2, 50),
        "RELATÓRIO DE ENTREGA",
        fill="white",
        font=fonte_titulo,
        anchor="mm",
    )

    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    data_hoje = datetime.now().strftime("%d de %B de %Y")
    draw.text((1200, 40), data_hoje, fill="white", font=fonte_header)

    # Cabeçalho da tabela
    y = 105
    colunas = [
        ("CARGA", 0, 150),
        ("DATA/HORA", 150, 350),
        ("MOTORISTA / AJUDANTE", 350, 830),
        ("LOCALIDADE DA ENTREGA", 830, 1330),
        ("OBSERVAÇÃO", 1330, 1600),
    ]

    for titulo, x1, x2 in colunas:
        # Desenha o retângulo cinza
        draw.rectangle([x1, y, x2, y + 50], outline="black", fill=(147, 147, 147))

        # Calcula o centro exato da célula do cabeçalho
        meio_x = (x1 + x2) / 2
        meio_y = y + 25  # 25 é a metade da altura (50) do cabeçalho

        # Escreve o texto usando ancoragem no meio (mm)
        draw.text((meio_x, meio_y), titulo, fill="white", font=fonte_header, anchor="mm")

    y += 50


    numero_cargas = 0
    for i, item in enumerate(ESCALA):

        if numero_cargas >= 16:
            break


        altura_linha = 110
        fundo = (236, 236, 236) if i % 2 == 0 else (255, 255, 255)

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
                spacing=10
            )

        y += altura_linha
        numero_cargas += 1

    img.save("relatorio_entrega.png")
