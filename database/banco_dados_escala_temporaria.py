import sqlite3

from constants.banco_dados import BANCO_DADOS_ESCALA_TEMPORARIAS, TABELA_ESCALA_TEMPORARIAS


def conectar_banco_de_dados_escala_temporaria():
    return sqlite3.connect(BANCO_DADOS_ESCALA_TEMPORARIAS)


def criar_tabela_escala_temporaria():

    conexao = conectar_banco_de_dados_escala_temporaria()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_ESCALA_TEMPORARIAS} (
    numero_carga VARCHAR(8),
    data VARCHAR(10),
    data_saida VARCHAR(10),
    horario VARCHAR(6),
    motorista VARCHAR(6),
    ajudante_1 VARCHAR(6),
    ajudante_2 VARCHAR(6),
    numero_rota VARCHAR(10),
    observacao VARCHAR(250),
    numero_caminhao VARCHAR(6)
    )
    """
    )

    conexao.commit()
    conexao.close()

