from database.banco_dados_escala import conectar_banco_de_dados_escala
from constants.banco_dados import TABELA_ESCALA

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
