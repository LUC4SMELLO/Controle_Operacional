from database.banco_dados_veiculos import conectar_banco_de_dados_veiculos
from constants.banco_dados import TABELA_VEICULOS

def buscar_km_caminhao(codigo_caminhao):

    conexao = None

    try:
        conexao = conectar_banco_de_dados_veiculos()
        cursor = conexao.cursor()

        cursor.execute(f"SELECT km FROM {TABELA_VEICULOS} WHERE codigo = ?", (codigo_caminhao,))

        resultado = cursor.fetchone()

        return resultado

    finally:
        if conexao:
            conexao.close()