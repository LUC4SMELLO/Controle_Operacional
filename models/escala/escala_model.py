from database.banco_dados_funcionarios import conectar_banco_de_dados_funcionarios
from constants.banco_dados import TABELA_FUNCIONARIOS

from database.banco_dados_veiculos import conectar_banco_de_dados_veiculos
from constants.banco_dados import BANCO_DADOS_VEICULOS, TABELA_VEICULOS


class EscalaModel:
    def __init__(self):
        pass
    
    def buscar_informacoes_funcionario(self, codigo):

        try:
            conexao = conectar_banco_de_dados_funcionarios()
            cursor = conexao.cursor()

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_VEICULOS}' AS veiculos")

            cursor.execute(
            f"""
            SELECT
            fun.nome,
            fun.funcao,
            fun.cpf,
            fun.rg,
            vei.codigo,
            vei.placa
            FROM {TABELA_FUNCIONARIOS} AS fun
            LEFT JOIN veiculos.{TABELA_VEICULOS} AS vei ON fun.codigo = vei.codigo_motorista
            WHERE fun.codigo = ?
            """, (codigo,)
            )

            resultado = cursor.fetchone()

            return resultado
        
        finally:
            conexao.close()

