import sqlite3

from constants.banco_dados import BANCO_DADOS_ESCALA, TABELA_ESCALA


def conectar_banco_de_dados_escala():
    return sqlite3.connect(BANCO_DADOS_ESCALA)


def criar_tabela_escala():

    conexao = conectar_banco_de_dados_escala()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_ESCALA} (
    data VARCHAR(10),
    data_saida VARCHAR(10),
    numero_carga VARCHAR(10),
    codigo_motorista VARCHAR(100),
    codigo_ajudante_1 VARCHAR(100),
    codigo_ajudante_2 VARCHAR(100),
    nome_rota VARCHAR(50),
    numero_rota VARCHAR(50),
    observacao VARCHAR(250),
    numero_caminhao VARCHAR(10),
    dia_semana VARCHAR(100),
    horario VARCHAR(10),
    PRIMARY KEY (numero_carga, data)

    )
    """
    )

    conexao.commit()
    conexao.close()
