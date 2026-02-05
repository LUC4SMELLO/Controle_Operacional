from database.banco_dados_funcionarios import conectar_banco_de_dados_funcionarios
from constants.banco_dados import BANCO_DADOS_FUNCIONARIOS, TABELA_FUNCIONARIOS

from database.banco_dados_veiculos import conectar_banco_de_dados_veiculos
from constants.banco_dados import BANCO_DADOS_VEICULOS, TABELA_VEICULOS

from database.banco_dados_escala_temporaria import conectar_banco_de_dados_escala_temporaria
from constants.banco_dados import TABELA_ESCALA_TEMPORARIAS

from database.banco_dados_escala import conectar_banco_de_dados_escala
from constants.banco_dados import TABELA_ESCALA



class EscalaModel:
    def __init__(self):
        pass


    # ----------------------------
    #        FUNCIONÁRIO 
    # ----------------------------
    

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
        
        except Exception as e:
            print("Erro ao buscar funcionário:", e)
            return False
        
        finally:
            conexao.close()


    # ----------------------------
    #      ESCALA TEMPORÁRIA
    # ----------------------------


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

            return registros
        
        except Exception as e:
            print("Erro ao carregar escala temporária:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()

    def excluir_escala_temporaria(self, numero_carga):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_escala_temporaria()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                DELETE FROM {TABELA_ESCALA_TEMPORARIAS}
                WHERE numero_carga = ?
                """, (numero_carga,)
                )
            
            conexao.commit()

        except Exception as e:
            print("Erro ao excluir escala temporária:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()

    def limpar_banco_dados_escala_temporaria(self):

        conexao = None

        try:
            conexao = conectar_banco_de_dados_escala_temporaria()
            cursor = conexao.cursor()

            cursor.execute(f"DELETE FROM {TABELA_ESCALA_TEMPORARIAS}")

            conexao.commit()

        except Exception as e:
            print("Erro ao limpar banco dados escala temporária:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()


    # ----------------------------
    #           ESCALA 
    # ----------------------------


    def salvar_escala(self, dados):
        # mesma carga + data diferente -> INSERE
        # mesma carga + mesma data -> CONFLICT

        conexao = None

        try:
            conexao = conectar_banco_de_dados_escala()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_ESCALA} (
                data,
                data_saida,
                numero_carga,
                codigo_motorista,
                codigo_ajudante_1,
                codigo_ajudante_2,
                nome_rota,
                numero_rota,
                observacao,
                numero_caminhao,
                dia_semana,
                horario
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(numero_carga, data)
                DO UPDATE SET
                    data_saida  = excluded.data_saida,
                    codigo_motorista  = excluded.codigo_motorista,
                    codigo_ajudante_1 = excluded.codigo_ajudante_1,
                    codigo_ajudante_2 = excluded.codigo_ajudante_2,
                    nome_rota   = excluded.nome_rota,
                    numero_rota = excluded.numero_rota,
                    observacao  = excluded.observacao,
                    numero_caminhao   = excluded.numero_caminhao,
                    dia_semana  = excluded.dia_semana,
                    horario     = excluded.horario
                """,
                (
                    dados["data"],
                    dados["data_saida"],
                    dados["numero_carga"],
                    dados["codigo_motorista"],
                    dados["codigo_ajudante_1"],
                    dados["codigo_ajudante_2"],
                    dados["nome_rota"],
                    dados["numero_rota"],
                    dados["observacao"],
                    dados["numero_caminhao"],
                    dados["dia_semana"],
                    dados["horario"]
                )
            )

            conexao.commit()


        except Exception as e:
            print(f"Erro ao salvar escala:", e)
            return False
        
        finally:
            if conexao:
                conexao.close()

    def buscar_escala(self, data=""):

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
                    e.data,
                    e.data_saida,
                    e.numero_carga,

                    m.nome  AS motorista,
                    a1.nome AS ajudante_1,
                    a2.nome AS ajudante_2,

                    e.nome_rota,
                    e.numero_rota,
                    e.observacao,
                    e.numero_caminhao,
                    e.dia_semana,
                    e.horario
                FROM {TABELA_ESCALA} AS e

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS m
                    ON m.codigo = e.codigo_motorista

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS a1
                    ON a1.codigo = e.codigo_ajudante_1

                LEFT JOIN funcionarios_db.{TABELA_FUNCIONARIOS} AS a2
                    ON a2.codigo = e.codigo_ajudante_2
            """
            
            parametros = []
            if data:
                consulta += " WHERE e.data = ?"
                parametros.append(data)

            cursor.execute(consulta, parametros)

            resultado = cursor.fetchall()

            return resultado
        
        except Exception as e:
            print(f"Erro ao buscar escala:", e)
            return None

        finally:
            if conexao:
                conexao.close()
