import sqlite3

from constants.banco_dados import BANCO_DADOS_APONTAMENTOS, TABELA_APONTAMENTOS


def conectar_banco_de_dados_apontamentos():
    return sqlite3.connect(BANCO_DADOS_APONTAMENTOS)


def criar_tabela_apontamentos():

    conexao = conectar_banco_de_dados_apontamentos()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_APONTAMENTOS} (
    numero_carga VARCHAR(22),
    hora_saida VARCHAR(10),
    hora_chegada VARCHAR(10),
    km_inicial VARCHAR(10),
    km_final VARCHAR(10)
    )
    """
    )
    
    conexao.commit()
    conexao.close()