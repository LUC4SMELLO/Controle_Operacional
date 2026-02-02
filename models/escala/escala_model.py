from database.banco_dados_funcionarios import conectar_banco_de_dados_funcionarios
from constants.banco_dados import TABELA_FUNCIONARIOS

from database.banco_dados_veiculos import conectar_banco_de_dados_veiculos
from constants.banco_dados import BANCO_DADOS_VEICULOS, TABELA_VEICULOS

from database.banco_dados_escala_temporaria import conectar_banco_de_dados_escala_temporaria
from constants.banco_dados import BANCO_DADOS_ESCALA_TEMPORARIAS, TABELA_ESCALA_TEMPORARIAS


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

    def salvar_escala_temporaria(self, dados):
        
        conexao = None
        
        try:
            conexao = conectar_banco_de_dados_escala_temporaria()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_ESCALA_TEMPORARIAS} (
                numero_carga,
                data,
                data_saida,
                horario,
                motorista,
                ajudante_1,
                ajudante_2,
                numero_rota,
                observacao,
                numero_caminhao
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                )
                """,
                    (
                        dados["numero_carga"],
                        dados["data"],
                        dados["data_saida"],
                        dados["horario_saida"],
                        dados["motorista"],
                        dados["ajudante_1"],
                        dados["ajudante_2"],
                        dados["rota"],
                        dados["observacao"],
                        dados["numero_caminhao"]
                    )
                )
            
            conexao.commit()

        except Exception:
            return []
        
        finally:
            if conexao:
                conexao.close()
