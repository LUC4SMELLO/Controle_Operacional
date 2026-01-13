from database.banco_dados_produtos import conectar_banco_de_dados_produtos

from constants.banco_dados import TABELA_PRODUTOS


def listar_produtos_banco_dados():

    try:
        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(f"SELECT codigo, descricao FROM {TABELA_PRODUTOS}")

        resultado = cursor.fetchall()

        return dict(resultado)
    
    finally:
        conexao.close()
