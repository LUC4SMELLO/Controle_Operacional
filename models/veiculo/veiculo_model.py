from database.banco_dados_veiculos import conectar_banco_de_dados_veiculos
from constants.banco_dados import TABELA_VEICULOS

class VeiculoModel:
    def __init__(self):
        pass

    def cadastrar_veiculo(self, dados):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_veiculos()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_VEICULOS} (
                codigo,
                placa,
                codigo_motorista
                )
                VALUES (?, ?, ?)
                """,
                (
                    dados["codigo"],
                    dados["placa"],
                    dados["codigo_motorista"]
                )
            )

            conexao.commit()

        except Exception:
            return []

        finally:
            if conexao:
                conexao.close()

    def editar_veiculo(self, dados):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_veiculos()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                UPDATE {TABELA_VEICULOS}
                SET placa = ?,
                codigo_motorista = ?
                WHERE codigo = ?
                """, 
                    (   
                        dados["placa"],
                        dados["codigo_motorista"],
                        dados["codigo"],
                    )
            )

            conexao.commit()

        except Exception:
            return []
        
        finally:
            if conexao:
                conexao.close()

    def excluir_veiculo(self, codigo):
        
        conexao = None

        try:
            conexao = conectar_banco_de_dados_veiculos()
            cursor = conexao.cursor()

            cursor.execute(
            f"""
            DELETE FROM {TABELA_VEICULOS}
            WHERE codigo = ?
            """, (codigo,)
            )

            conexao.commit()

        except Exception:
            return []

        finally:
            if conexao:
                conexao.close()

    def buscar_veiculo(self, codigo):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_veiculos()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT
                codigo,
                placa,
                codigo_motorista
                FROM {TABELA_VEICULOS}
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