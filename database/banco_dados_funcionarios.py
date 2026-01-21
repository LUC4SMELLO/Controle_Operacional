import sqlite3

from constants.banco_dados import BANCO_DADOS_FUNCIONARIOS, TABELA_FUNCIONARIOS


def conectar_banco_de_dados_funcionarios():
    return sqlite3.connect(BANCO_DADOS_FUNCIONARIOS)


def criar_tabela_funcionarios():

    conexao = conectar_banco_de_dados_funcionarios()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_FUNCIONARIOS} (
    codigo INTEGER PRIMARY KEY,
    nome VARCHAR(250),
    funcao VARCHAR(100),
    cpf VARCHAR(50),
    rg VARCHAR(50),
    )
    """
    )

    conexao.commit()
    conexao.close()
