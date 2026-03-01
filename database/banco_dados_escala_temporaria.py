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
    numero_carga VARCHAR(8) PRIMARY KEY,
    km VARCHAR(10),
    horario VARCHAR(6),
    codigo_motorista VARCHAR(6),
    nome_motorista VARCHAR(100),
    codigo_ajudante_1 VARCHAR(6),
    nome_ajudante_1 VARCHAR(100),
    codigo_ajudante_2 VARCHAR(6),
    nome_ajudante_2 VARCHAR(100),
    rota VARCHAR(10),
    observacao VARCHAR(250)
    )
    """
    )

    conexao.commit()
    conexao.close()

