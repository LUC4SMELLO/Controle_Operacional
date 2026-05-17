from database.banco_dados_escala import conectar_banco_de_dados_escala
from constants.banco_dados import BANCO_DADOS_FUNCIONARIOS, TABELA_ESCALA, TABELA_FUNCIONARIOS


class MapaTrocaModel:
    def __init__(self):
        pass


    def buscar_mapa(self, carga=""):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_escala()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                ATTACH DATABASE '{BANCO_DADOS_FUNCIONARIOS}' 
                AS funcionarios_db
                """
            )

            consulta = f"""
                SELECT 
                    e.numero_carga,

                    m.nome  AS motorista,
                    a1.nome AS ajudante_1,
                    a2.nome AS ajudante_2,

                    e.nome_rota,
                    e.numero_rota,
                    e.numero_caminhao
                FROM {TABELA_ESCALA} AS e

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS m
                    ON m.codigo = e.codigo_motorista

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS a1
                    ON a1.codigo = e.codigo_ajudante_1

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS a2
                    ON a2.codigo = e.codigo_ajudante_2
            """

            parametros = []
            if carga:
                consulta += " WHERE e.numero_carga = ?"
                parametros.append(carga)

            cursor.execute(consulta, parametros)

            resultado = cursor.fetchall()

            return resultado

        except Exception as erro:
            print("Erro ao buscar mapa: ", erro)
            return False
        
        finally:
            if conexao:
                conexao.close()