from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias
from constants.banco_dados import TABELA_PENDENCIAS, BANCO_DADOS_CLIENTES, TABELA_CLIENTES


CAMPOS_PENDENCIA = [
        "cupom",
        "codigo_cliente",
        "razao_social",
        "codigo_produto",
        "quantidade",
    ]

class CarregamentoTrocaModel:
    def __init__(self):
        pass

    def buscar_pendencias(self):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_pendencias()
            cursor = conexao.cursor()

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_CLIENTES}' AS clientes")


            cursor.execute(
                f"""
                SELECT
                    pen.cupom,
                    pen.codigo_cliente,
                    cli.razao_social,
                    pen.codigo_produto,
                    pen.quantidade
                FROM {TABELA_PENDENCIAS} AS pen
                LEFT JOIN clientes.{TABELA_CLIENTES} AS cli ON pen.codigo_cliente = cli.codigo
                WHERE pen.situacao = ?
                """, ("Pendente",)
            )


            registros = cursor.fetchall()

            pendencias = [
                dict(zip(CAMPOS_PENDENCIA, linha))
                for linha in registros
            ]

            return pendencias
        
        except Exception as e:
            print("Erro ao buscar pendências:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()