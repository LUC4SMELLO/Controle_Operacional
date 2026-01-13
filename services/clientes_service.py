from database.banco_dados_clientes import conectar_banco_de_dados_clientes

from constants.banco_dados import TABELA_CLIENTES


def listar_clientes_banco_dados():

    try:
        conexao = conectar_banco_de_dados_clientes()
        cursor = conexao.cursor()

        cursor.execute(f"SELECT codigo, razao_social FROM {TABELA_CLIENTES}")

        resultado = cursor.fetchall()

        return dict(resultado)

    finally:
        conexao.close()
