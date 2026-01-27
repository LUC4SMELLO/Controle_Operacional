from database.banco_dados_funcionarios import conectar_banco_de_dados_funcionarios

from constants.banco_dados import TABELA_FUNCIONARIOS, BANCO_DADOS_VEICULOS, TABELA_VEICULOS


def listar_funcionarios_banco_dados():

    try:
        conexao = conectar_banco_de_dados_funcionarios()
        cursor = conexao.cursor()

        cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_VEICULOS}' AS veiculos")

        cursor.execute(f"""
        SELECT
        fun.codigo,
        fun.nome,
        fun.funcao,
        vei.codigo
        FROM {TABELA_FUNCIONARIOS} AS fun
        LEFT JOIN veiculos.{TABELA_VEICULOS} AS vei ON fun.codigo = vei.codigo_motorista
        """)

        resultado = cursor.fetchall()

        return list(resultado)
    
    finally:
        conexao.close()
