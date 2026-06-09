from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import locale
from datetime import datetime

from constants.paths import REPORTS_IMAGES_DIR
from constants.paths import IMAGES_DIR


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

def gerar_imagem_mapa_troca_frente(informacoes_escala: dict, informacoes_pendencias: dict):
        
    # Criar imagem branca
    largura = 1190
    altura = 1684

    img = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(img)

    # =========================
    # FUNÇÕES AUXILIARES
    # =========================

    def desenhar_carregamento_troca():
        pass

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
            f"{informacoes_escala['numero_carga']} - {numero_carga_1}",
            fill="black",
            font=fonte
        )

        linha(60, y_caixa + 40, 595, y_caixa + 40)

        draw.text(
            (95, y_caixa + 45),
            "CÓDIGO",
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
            "QUANT",
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
            f"{informacoes_escala['numero_carga']} - {numero_carga_2}",
            fill="black",
            font=fonte
        )

        linha(595, y_caixa + 40, 1130, y_caixa + 40)

        draw.text(
            (640, y_caixa + 45),
            "CÓDIGO ",
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
            "QUANT",
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
        fonte_menor = ImageFont.truetype("arial.ttf", 14)
        fonte_label = ImageFont.truetype("arialbd.ttf", 18)
        fonte_label_menor = ImageFont.truetype("arialbd.ttf", 14)
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
    imagem_logo = Image.open(IMAGES_DIR / "logo_dbcambui_2.png")
    imagem_logo = imagem_logo.resize((70, 70))
    img.paste(imagem_logo, (95, 50), imagem_logo)

    # Título
    draw.text((450, 70), "GUIA DE ENTREGA", fill="black", font=fonte_titulo)

    # Dados superiores
    draw.text((945, 70), "Nº Carga:", fill="black", font=fonte_label)
    draw.text((1035, 72), text=informacoes_escala["numero_carga"], fill="black", font=fonte)


    draw.text((95, 120), "Motorista:", fill="black", font=fonte_label)
    draw.text((190, 122), text=informacoes_escala["nome_motorista"], fill="black", font=fonte)
    draw.text((400, 120), "Veículo:", fill="black", font=fonte_label)
    draw.text((480, 122), text=informacoes_escala["numero_veiculo"], fill="black", font=fonte)

    draw.text((550, 120), text=informacoes_escala["nome_rota"], fill="black", font=fonte_label)

    if "segunda" in informacoes_escala["data_por_extenso"]:
        draw.text((845, 120), text=informacoes_escala["data_por_extenso"], fill="black", font=fonte)

    elif "quarta" in informacoes_escala["data_por_extenso"] or "quinta" in informacoes_escala["data_por_extenso"]:
        draw.text((862, 120), text=informacoes_escala["data_por_extenso"], fill="black", font=fonte)

    elif "terça" in informacoes_escala["data_por_extenso"] or "sexta" in informacoes_escala["data_por_extenso"]:
        draw.text((872, 120), text=informacoes_escala["data_por_extenso"], fill="black", font=fonte)

    # =========================
    # INFORMAÇÕES
    # =========================

    draw.text((95, 175), "Horário Saída:", fill="black", font=fonte_label)
    linha(225, 192, 370, 192)
    draw.text((400, 175), "Horário Chegada:", fill="black", font=fonte_label)
    linha(560, 192, 705, 192)

    draw.text((730, 175), "Segundo Ajudante:", fill="black", font=fonte_label)
    linha(901, 192, 986, 192)
    draw.text((938, 172), ":", fill="black", font=fonte_label)
    linha(1008, 192, 1096, 192)
    draw.text((1048, 172), ":", fill="black", font=fonte_label)

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
    draw.text((255, 270), "CARREGADO", fill="black", font=fonte_label)
    draw.text((390, 270), "RETORNADO", fill="black", font=fonte_label)
    draw.text((587, 270), "VENDIDO", fill="black", font=fonte_label)

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
    linha(380, 305, 380, 545)
    linha(510, 305, 510, 545)
    linha(745, 305, 745, 545)
    linha(745, 305, 745, 545)

    draw.text((795, 270), "DEVOLUÇÃO DE MERCADORIA", fill="black", font=fonte_label)
    draw.text((800, 310), "DESCRIÇÃO", fill="black", font=fonte_label)
    draw.text((961, 310), "QUANTIDADE", fill="black", font=fonte_label)

    y=305
    for i in range(9):
        linha(755, y, 1096, y)
        y += 30
    linha(755, 305, 755, 545)
    linha(941, 305, 941, 545)
    linha(1096, 305, 1096, 545)


    # =========================
    # TROCA DE MERCADORIAS
    # =========================
    if informacoes_pendencias:
        y_atual = 580
        texto_secao = "MAPA DE CARREGAMENTO DE TROCAS E PENDÊNCIAS"
        
        # 1. Título da Seção
        draw.text((290, y_atual), texto_secao, fill="black", font=fonte_titulo)
        bbox_titulo = draw.textbbox((290, y_atual), texto_secao, font=fonte_titulo)
        altura_titulo = bbox_titulo[3] - bbox_titulo[1]
        
        # Avança o Y após o título (título + margem)
        y_atual += altura_titulo + 15  

        # 2. Tabela 1: Itens das Pendências (Cabeçalho)
        y_cabecalho_itens = y_atual
        colunas_itens = {
            "CÓDIGO": 80, "DESCRIÇÃO": 225, "QUANTIDADE": 500, 
            "TIPO": 700, "VALOR UNITÁRIO": 830, "VALOR TOTAL": 980
        }
        for texto_col, x_col in colunas_itens.items():
            draw.text((x_col, y_cabecalho_itens), texto_col, fill="black", font=fonte_label_menor)
        
        # Linhas dos Itens
        y_atual += 18  
        for cod_cliente, dados in informacoes_pendencias.items():
            for pendencia in dados["pendencias"]:
                # Alinhamento do Tipo (substitui o IF por cálculo ou largura estimada)
                x_tipo = 685 if "Pendência" in str(pendencia["tipo"]) else 698
                
                draw.text((100, y_atual), str(pendencia["cupom"]), fill="black", font=fonte_menor)
                draw.text((170, y_atual), str(pendencia["descricao"]), fill="black", font=fonte_menor)
                draw.text((535, y_atual), str(pendencia["quantidade"]), fill="black", font=fonte_menor)
                draw.text((x_tipo, y_atual), str(pendencia["tipo"]), fill="black", font=fonte_menor)
                
                y_atual += 20
        
        # Desenha o primeiro retângulo baseado no Y real alcançado
        retangulo(60, y_cabecalho_itens - 5, 1130, y_atual + 5)

        # 3. Tabela 2: Resumo de Clientes
        y_atual += 25  # Espaçamento entre as duas tabelas
        texto_subsecao = "CLIENTES COM TROCAS OU PENDÊNCIAS NESTE MAPA"
        draw.text((280, y_atual), texto_subsecao, fill="black", font=fonte_titulo)
        
        y_atual += 35  # Espaçamento após o subtítulo
        y_cabecalho_clientes = y_atual
        colunas_clientes = {"CÓDIGO": 80, "RAZÃO SOCIAL": 300, "TOTAL": 620}
        for texto_col, x_col in colunas_clientes.items():
            draw.text((x_col, y_cabecalho_clientes), texto_col, fill="black", font=fonte_label_menor)
            
        # Linhas dos Clientes
        y_atual += 18  
        for cod_cliente, dados in informacoes_pendencias.items():
            draw.text((90, y_atual), str(cod_cliente), fill="black", font=fonte_menor)
            draw.text((190, y_atual), str(dados["razao_social"]), fill="black", font=fonte_menor)
            
            # Conta a quantidade de cupons usando a lógica que criamos antes
            qtd_cupons = len({p["cupom"] for p in dados["pendencias"]})
            draw.text((630, y_atual), f"{qtd_cupons}", fill="black", font=fonte_menor)
            
            y_atual += 20
            
        # Desenha o segundo retângulo perfeitamente alinhado dinamicamente
        retangulo(60, y_cabecalho_clientes - 5, 1130, y_atual + 5)
        
        # Atualiza a variável global/escopo do Y dinâmico para os próximos blocos da página
        y_proxima_secao = y_atual + 30
        
    else:
        draw.text((290, 580), "ESTE MAPA NÃO POSSUI TROCAS OU PENDÊNCIAS", fill="black", font=fonte_titulo)
        y_proxima_secao = 620




    # =========================
    #        RODAPÉ
    # =========================

    retangulo(60, 1595, 1130, 1620)

    draw.text((95, 1598), "Ajudante 1:", fill="black", font=fonte_label)
    draw.text((200, 1600), informacoes_escala["nome_ajudante_1"] if informacoes_escala["nome_ajudante_1"] else "", fill="black", font=fonte)
    draw.text((700, 1598), "Ajudante 2:", fill="black", font=fonte_label)
    draw.text((805, 1600), informacoes_escala["nome_ajudante_2"] if informacoes_escala["nome_ajudante_2"] else "", fill="black", font=fonte)

    # =========================
    # CUPONS
    # =========================

    draw.text((320, y_proxima_secao), "CUPONS PARA PREENCHER EM CASO DE TROCA", fill="black", font=fonte_titulo)

    y_inicial = y_proxima_secao + 30
    altura_pagina = 1590

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
        REPORTS_IMAGES_DIR / "mapa_frente.png"
    )



def gerar_imagem_mapa_troca_verso(clientes_pendencias: dict):

    LARGURA = 1190
    ALTURA = 1684

    X_ESQUERDA = 10
    X_DIREITA = 610

    LIMITE_ALTURA = 1600
    MARGEM_ENTRE_BLOCOS = 20

    try:
        fonte = ImageFont.truetype("arial.ttf", 16)
        fonte_label = ImageFont.truetype("arialbd.ttf", 18)
        fonte_label_menor = ImageFont.truetype("arialbd.ttf", 14)
    except Exception:
        fonte = fonte_label = fonte_label_menor = ImageFont.load_default()

    pagina_atual = 1

    def criar_pagina():
        img = Image.new("RGB", (LARGURA, ALTURA), "white")
        draw = ImageDraw.Draw(img)
        return img, draw

    img, draw = criar_pagina()

    def texto(x, y, valor, font=fonte):
        draw.text((x, y), str(valor), fill="black", font=font)

    def linha(x1, y1, x2, y2, largura_linha=1):
        draw.line((x1, y1, x2, y2), fill="black", width=largura_linha)

    def retangulo(x1, y1, x2, y2, largura_linha=1):
        draw.rectangle(
            (x1, y1, x2, y2),
            outline="black",
            width=largura_linha
        )

    def salvar_pagina(numero):
        caminho = (
            Path(REPORTS_IMAGES_DIR)
            / f"mapa_verso_{numero}.png"
        )

        img.save(caminho)

    def desenhar_bloco(x, y, codigo_cliente, dados_cliente):

        pendencias = dados_cliente["pendencias"]

        cupom = pendencias[0]["cupom"]
        responsavel = pendencias[0]["responsavel"]

        altura_bloco = 220 + (len(pendencias) * 25)
        largura_bloco = 565

        retangulo(
            x,
            y,
            x + largura_bloco,
            y + altura_bloco
        )

        # Cabeçalho
        texto(x + 10, y + 15, "CÓDIGO:", fonte_label)
        texto(x + 110, y + 17, codigo_cliente)

        texto(x + 400, y + 15, "CUPOM:", fonte_label)
        texto(x + 480, y + 17, cupom)

        texto(x + 10, y + 45, "RAZÃO SOCIAL:", fonte_label)

        razao_social = dados_cliente.get("razao_social", "")

        if len(razao_social) > 35:
            razao_social = razao_social[:35] + "..."

        texto(x + 160, y + 47, razao_social)

        linha(
            x,
            y + 75,
            x + largura_bloco,
            y + 75
        )

        # Cabeçalho
        texto(x + 10, y + 80, "CÓDIGO", fonte_label_menor)
        texto(x + 110, y + 80, "DESCRIÇÃO", fonte_label_menor)
        texto(x + 440, y + 80, "QUANT.", fonte_label_menor)

        y_produto = y + 105
        total_quantidade = 0

        for item in pendencias:

            texto(
                x + 10,
                y_produto,
                item["codigo_produto"]
            )

            texto(
                x + 110,
                y_produto,
                (item.get("descricao") or "")[:35]
            )

            texto(
                x + 450,
                y_produto,
                item["quantidade"]
            )

            total_quantidade += int(item["quantidade"])

            y_produto += 25

        linha(
            x,
            y_produto + 10,
            x + largura_bloco,
            y_produto + 10
        )

        texto(
            x + 10,
            y_produto + 15,
            "TOTAL",
            fonte_label
        )

        texto(
            x + 450,
            y_produto + 17,
            total_quantidade
        )

        linha(
            x,
            y_produto + 45,
            x + largura_bloco,
            y_produto + 45
        )

        texto(
            x + 10,
            y_produto + 55,
            "RESPONSÁVEL:",
            fonte_label
        )

        texto(
            x + 170,
            y_produto + 57,
            responsavel
        )

        texto(
            x + 10,
            y_produto + 85,
            "ASSINATURA:",
            fonte_label
        )

        linha(
            x + 170,
            y_produto + 100,
            x + 440,
            y_produto + 100
        )

        return altura_bloco

    y_esquerda = 10
    y_direita = 10

    coluna_atual = "esquerda"

    for codigo_cliente, dados_cliente in clientes_pendencias.items():

        pendencias = dados_cliente.get("pendencias", [])

        if not pendencias:
            continue

        altura_bloco = 220 + (len(pendencias) * 25)

        while True:

            if coluna_atual == "esquerda":

                if y_esquerda + altura_bloco <= LIMITE_ALTURA:

                    desenhar_bloco(
                        X_ESQUERDA,
                        y_esquerda,
                        codigo_cliente,
                        dados_cliente
                    )

                    y_esquerda += (
                        altura_bloco +
                        MARGEM_ENTRE_BLOCOS
                    )

                    break

                coluna_atual = "direita"

            if coluna_atual == "direita":

                if y_direita + altura_bloco <= LIMITE_ALTURA:

                    desenhar_bloco(
                        X_DIREITA,
                        y_direita,
                        codigo_cliente,
                        dados_cliente
                    )

                    y_direita += (
                        altura_bloco +
                        MARGEM_ENTRE_BLOCOS
                    )

                    break

                # Salva página atual
                salvar_pagina(pagina_atual)

                pagina_atual += 1

                # Nova página
                img, draw = criar_pagina()

                y_esquerda = 10
                y_direita = 10

                coluna_atual = "esquerda"

    # salva última página
    salvar_pagina(pagina_atual)