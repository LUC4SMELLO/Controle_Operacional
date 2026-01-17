import sqlite3
import csv

from constants.banco_dados import BANCO_DADOS_PRODUTOS, TABELA_PRODUTOS

from constants.caminho_arquivos import CAMINHO_ARQUIVO_PRODUTOS_FORMATADOS


def conectar_banco_de_dados_produtos():
    return sqlite3.connect(BANCO_DADOS_PRODUTOS)


def criar_tabela_produtos():

    conexao = conectar_banco_de_dados_produtos()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_PRODUTOS} (
    codigo INTEGER PRIMARY KEY,
    descricao VARCHAR(250)
    )
    """
    )

    conexao.commit()
    conexao.close()
    

def sincronizar_csv_com_banco_dados_produtos():

    conexao = conectar_banco_de_dados_produtos()
    cursor = conexao.cursor()

    try:
        with open(CAMINHO_ARQUIVO_PRODUTOS_FORMATADOS, mode="r", encoding="utf-8-sig") as arquivo:

            leitor_csv = csv.DictReader(arquivo, delimiter=";")
            
            dados = []
            for linha in leitor_csv:
                dados.append((
                    linha["codigo"],
                    linha["descricao"]
                ))

            cursor.executemany(
                f"""
                INSERT OR REPLACE INTO {TABELA_PRODUTOS} 
                (codigo, descricao)
                VALUES (?, ?)
                """, dados)

        conexao.commit()
        print(f"Sincronização concluída: {len(dados)} produtos processados.")
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")
    finally:
        conexao.close()
