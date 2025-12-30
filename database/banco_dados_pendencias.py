import sqlite3

from constants.banco_dados import BANCO_DADOS_PENDENCIAS, TABELA_PENDENCIAS


def conectar_banco_de_dados_pendencias():
    return sqlite3.connect(BANCO_DADOS_PENDENCIAS)


def criar_tabela_pendencias():

    conexao = conectar_banco_de_dados_pendencias()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_PENDENCIAS} (
    cupom INTEGER PRIMARY KEY,
    data VARCHAR(10),
    carga VARCHAR(8),
    codigo_cliente VARCHAR(200),
    tipo VARCHAR(10),
    responsavel VARCHAR(50),
    codigo_produto VARCHAR(10),
    quantidade VARCHAR(10)
    )
    """
    )
    
    conexao.commit()
    conexao.close()
