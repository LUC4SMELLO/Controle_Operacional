import sqlite3
from collections import defaultdict

from database.banco_dados_escala import conectar_banco_de_dados_escala
from constants.banco_dados import BANCO_DADOS_FUNCIONARIOS, TABELA_ESCALA, TABELA_FUNCIONARIOS


from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias
from constants.banco_dados import TABELA_PENDENCIAS

from constants.banco_dados import BANCO_DADOS_CLIENTES, TABELA_CLIENTES
from constants.banco_dados import BANCO_DADOS_PRODUTOS, TABELA_PRODUTOS


from services.data_service import buscar_data_por_extenso

CAMPOS_INFORMACOES = [
        "numero_carga",
        "data",
        "nome_motorista",
        "nome_ajudante_1",
        "nome_ajudante_2",
        "nome_rota",
        "numero_rota",
        "numero_veiculo"
    ]

class MapaTrocaModel:
    def __init__(self):
        pass


    def buscar_mapa(self, carga=""):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_escala()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                ATTACH DATABASE '{BANCO_DADOS_FUNCIONARIOS}' 
                AS funcionarios_db
                """
            )

            consulta = f"""
                SELECT 
                    e.numero_carga,
                    e.data,

                    m.nome  AS motorista,
                    a1.nome AS ajudante_1,
                    a2.nome AS ajudante_2,

                    e.nome_rota,
                    e.numero_rota,
                    e.numero_caminhao
                FROM {TABELA_ESCALA} AS e

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS m
                    ON m.codigo = e.codigo_motorista

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS a1
                    ON a1.codigo = e.codigo_ajudante_1

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS a2
                    ON a2.codigo = e.codigo_ajudante_2
            """

            parametros = []
            if carga:
                consulta += " WHERE e.numero_carga = ?"
                parametros.append(carga)

            cursor.execute(consulta, parametros)

            resultado = cursor.fetchall()
            if not resultado:
                return []

            informacoes = [
                dict(zip(CAMPOS_INFORMACOES, linha))
                for linha in resultado
            ]

            informacoes[0]["data_por_extenso"] = buscar_data_por_extenso(informacoes[0]["data"])


            try:
                if informacoes[0]:
                    return informacoes[0]
            except Exception:
                return []
        

        except Exception as erro:
            print("Erro ao buscar mapa: ", erro)
            return False
        
        finally:
            if conexao:
                conexao.close()

    def buscar_pendencias_carga_por_cliente(self, carga):
        conexao = None
        try:
            conexao = conectar_banco_de_dados_pendencias()
            
            # Define o row_factory para acessar as colunas pelo nome (ex: row['cupom'])
            conexao.row_factory = sqlite3.Row
            cursor = conexao.cursor()

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_CLIENTES}' AS clientes")
            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_PRODUTOS}' AS produtos")

            query = f"""
            SELECT
                pen.cupom,
                pen.codigo_cliente,
                cli.razao_social,
                pen.tipo,
                pen.responsavel,
                pen.codigo_produto,
                pro.descricao,
                pen.quantidade
            FROM {TABELA_PENDENCIAS} AS pen
            LEFT JOIN clientes.{TABELA_CLIENTES} AS cli ON pen.codigo_cliente = cli.codigo
            LEFT JOIN produtos.{TABELA_PRODUTOS} AS pro ON pen.codigo_produto = pro.codigo
            WHERE pen.carga_entregue = ?
            """

            cursor.execute(query, (carga,))
            linhas = cursor.fetchall()

            # Estrutura o dicionário agrupado por cliente
            clientes_pendencias = defaultdict(lambda: {"razao_social": "", "pendencias": []})

            for linha in linhas:
                cod_cliente = linha["codigo_cliente"]
                
                # Define a razão social apenas uma vez por cliente
                if not clientes_pendencias[cod_cliente]["razao_social"]:
                    clientes_pendencias[cod_cliente]["razao_social"] = linha["razao_social"]

                # Cria o dicionário da pendência individual
                pendencia = {
                    "cupom": linha["cupom"],
                    "tipo": linha["tipo"],
                    "responsavel": linha["responsavel"],
                    "codigo_produto": linha["codigo_produto"],
                    "descricao": linha["descricao"],
                    "quantidade": linha["quantidade"]
                }
                
                # Adiciona a pendência na lista do respectivo cliente
                clientes_pendencias[cod_cliente]["pendencias"].append(pendencia)

            # Converte de defaultdict para um dicionário comum antes de retornar
            return dict(clientes_pendencias)
        
        except Exception as erro:
            print(f"Erro ao buscar pendências: {erro}")
            return {}
        
        finally:
            if conexao:
                try:
                    cursor = conexao.cursor()
                    cursor.execute("DETACH DATABASE clientes")
                    cursor.execute("DETACH DATABASE produtos")
                except Exception:
                    pass
                finally:
                    conexao.close()