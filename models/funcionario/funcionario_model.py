from database.banco_dados_funcionarios import conectar_banco_de_dados_funcionarios
from constants.banco_dados import TABELA_FUNCIONARIOS


class FuncionarioModel:
    def __init__(self):
        pass

    def cadastrar_funcionario(self, dados):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_funcionarios()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_FUNCIONARIOS} (
                codigo,
                nome,
                funcao,
                cpf,
                rg
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                    (
                        dados["codigo"],
                        dados["nome_completo"],
                        dados["funcao"],
                        dados["cpf"],
                        dados["rg"]
                    )
                )
            
            conexao.commit()

        except Exception:
            return []
        
        finally:
            if conexao:
                conexao.close()



