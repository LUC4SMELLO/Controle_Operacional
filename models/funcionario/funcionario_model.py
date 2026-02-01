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
                    dados["rg"],
                ),
            )

            conexao.commit()

        except Exception:
            return []

        finally:
            if conexao:
                conexao.close()

    def editar_funcionario(self, dados):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_funcionarios()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                UPDATE {TABELA_FUNCIONARIOS} 
                SET nome = ?,
                cpf = ?,
                rg = ?,
                funcao = ?
                WHERE codigo = ?
                """,
                (
                    dados["nome_completo"],
                    dados["cpf"],
                    dados["rg"],
                    dados["funcao"],
                    dados["codigo"]
                )
            )

            conexao.commit()

        except Exception:
            return []

        finally:
            if conexao:
                conexao.close()

    def excluir_funcionario(self, codigo):
        
        conexao = None

        try:
            conexao = conectar_banco_de_dados_funcionarios()
            cursor = conexao.cursor()

            cursor.execute(
            f"""
            DELETE FROM {TABELA_FUNCIONARIOS}
            WHERE codigo = ?
            """, (codigo,)
            )

            conexao.commit()

        except Exception:
            return []

        finally:
            if conexao:
                conexao.close()
    
    def buscar_funcionario(self, codigo):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_funcionarios()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT
                codigo,
                nome,
                cpf,
                rg,
                funcao
                FROM {TABELA_FUNCIONARIOS}
                WHERE codigo = ?
                """,
                (codigo,),
            )

            resultado = cursor.fetchone()

            return resultado
        
        except Exception:
            return []

        finally:
            if conexao:
                conexao.close()
