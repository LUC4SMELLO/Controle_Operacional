import sqlite3

from constants.banco_dados import BANCO_DADOS_CLIENTES, TABELA_CLIENTES


def conectar_banco_de_dados_clientes():
    return sqlite3.connect(BANCO_DADOS_CLIENTES)


def criar_tabela_clientes():

    conexao = conectar_banco_de_dados_clientes()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_CLIENTES} (
    codigo INTEGER PRIMARY KEY,
    razao_social VARCHAR(250),
    nome_fantasia VARCHAR(250),
    cidade VARCHAR(100),
    vendedor INTEGER,
    dia_semana VARCHAR(10),
    rota VARCHAR(10)
    )
    """
    )

    conexao.commit()
    conexao.close()
