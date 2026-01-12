import sqlite3
import csv

from constants.banco_dados import BANCO_DADOS_CLIENTES, TABELA_CLIENTES

from constants.arquivos import CAMINHO_ARQUIVO_CLIENTES_FORMATADOS


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


def sincronizar_csv_com_banco():

    conexao = conectar_banco_de_dados_clientes()
    cursor = conexao.cursor()

    try:
        with open(CAMINHO_ARQUIVO_CLIENTES_FORMATADOS, mode="r", encoding="utf-8-sig") as arquivo:

            leitor_csv = csv.DictReader(arquivo, delimiter=";")
            
            dados = []
            for linha in leitor_csv:
                dados.append((
                    linha["codigo"],
                    linha["razao"],
                    linha["fantasia"],
                    linha["cidade"],
                    linha["vendedor"],
                    linha["semana"],
                    linha["rota"]
                ))

            cursor.executemany(
                f"""
                INSERT OR REPLACE INTO {TABELA_CLIENTES} 
                (codigo, razao_social, nome_fantasia, cidade, vendedor, dia_semana, rota)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, dados)

        conexao.commit()
        print(f"Sincronização concluída: {len(dados)} clientes processados.")
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")
    finally:
        conexao.close()