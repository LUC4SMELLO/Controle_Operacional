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
                    horario,
                    codigo_motorista,
                    nome_motorista,
                    codigo_ajudante_1,
                    nome_ajudante_1,
                    codigo_ajudante_2,
                    nome_ajudante_2,
                    rota,
                    observacao
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(numero_carga)
                DO UPDATE SET
                    horario     = excluded.horario,
                    codigo_motorista   = excluded.codigo_motorista,
                    nome_motorista     = excluded.nome_motorista,
                    codigo_ajudante_1  = excluded.codigo_ajudante_1,
                    nome_ajudante_1    = excluded.nome_ajudante_1,
                    codigo_ajudante_2  = excluded.codigo_ajudante_2,
                    nome_ajudante_2    = excluded.nome_ajudante_2,
                    rota        = excluded.rota,
                    observacao  = excluded.observacao
                """,
                    (
                        dados["numero_carga"],
                        dados["horario"],
                        dados["codigo_motorista"],
                        dados["nome_motorista"],
                        dados["codigo_ajudante_1"],
                        dados["nome_ajudante_1"],
                        dados["codigo_ajudante_2"],
                        dados["nome_ajudante_2"],
                        dados["rota"],
                        dados["observacao"]
                    )
                )
            
            conexao.commit()

            print(f"Salvo: {dados}")

        except Exception as e:
            print("Erro ao salvar escala temporária:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()

    def carregar_escala_temporaria(self):
        try:
            conexao = conectar_banco_de_dados_escala_temporaria()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT
                    numero_carga,
                    horario,
                    codigo_motorista,
                    nome_motorista,
                    codigo_ajudante_1,
                    nome_ajudante_1,
                    codigo_ajudante_2,
                    nome_ajudante_2,
                    rota,
                    observacao
                FROM {TABELA_ESCALA_TEMPORARIAS}
                """
            )

            colunas = [desc[0] for desc in cursor.description]
            registros = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            conexao.close()

            return registros
        
        except Exception as e:
            print("Erro ao carregar escala temporária:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()
