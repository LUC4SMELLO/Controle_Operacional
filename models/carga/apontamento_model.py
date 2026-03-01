from database.banco_dados_escala import conectar_banco_de_dados_escala
from constants.banco_dados import TABELA_ESCALA

from database.banco_dados_apontamentos import conectar_banco_de_dados_apontamentos
from constants.banco_dados import TABELA_APONTAMENTOS

CAMPOS_ESCALA = [
        "data",
        "numero_carga",
        "horario"
    ]

class ApontamentoModel:
    def __init__(self):
        pass

    def buscar_escalas_por_data(self, data):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_escala()
            cursor = conexao.cursor()

            cursor.execute(f"""
                SELECT
                    data,
                    numero_carga,
                    horario
                FROM {TABELA_ESCALA}
                WHERE data = ?
                ORDER BY numero_carga ASC
            """, (data,))

            registros = cursor.fetchall()

            cargas = [
                dict(zip(CAMPOS_ESCALA, linha))
                for linha in registros
            ]

            return cargas
        
        except Exception as e:
            print("Erro ao buscar carga:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()

    def salvar_apontamento(self, dados):

        conexao = None    

        try:
            conexao = conectar_banco_de_dados_apontamentos()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_APONTAMENTOS} (
                numero_carga,
                hora_saida,
                hora_chegada
                km_inicial,
                km_final,
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                    (
                        dados["numero_carga"],
                        dados["hora_saida"],
                        dados["hora_chegada"],
                        dados["km_inicial"],
                        dados["km_final"]
                    )
            )

            conexao.commit()

        except Exception:
            return []
        
        finally:
            if conexao:
                conexao.close()
