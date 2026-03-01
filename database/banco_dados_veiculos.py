import sqlite3

from constants.banco_dados import BANCO_DADOS_VEICULOS, TABELA_VEICULOS


def conectar_banco_de_dados_veiculos():
    return sqlite3.connect(BANCO_DADOS_VEICULOS)


def criar_tabela_veiculos():
    
    conexao = conectar_banco_de_dados_veiculos()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_VEICULOS} (
    codigo INTEGER PRIMARY KEY,
    placa VARCHAR(10),
    km VARCHAR(8),
    codigo_motorista VARCHAR(5)
    )
    """
    )

    conexao.commit()
    conexao.close()
