from datetime import datetime

from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from constants.banco_dados import (
    BANCO_DADOS_CLIENTES,
    TABELA_CLIENTES,
    BANCO_DADOS_PRODUTOS,
    TABELA_PRODUTOS,
    TABELA_PENDENCIAS
)


class RelatorioModel:
    def __init__(self):
        pass

    def buscar_pendencias(
            self,
            cupom="",
            data_inicio="",
            data_fim="",
            carga="",
            codigo_cliente="",
            tipo="",
            codigo_produto=""
        ):
        
        """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

        conexao = None

        try:
            conexao = conectar_banco_de_dados_pendencias()
            cursor = conexao.cursor()

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_CLIENTES}' AS clientes")

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_PRODUTOS}' AS produtos")

            consulta_sql = f"""
            SELECT
            pen.cupom,
            pen.data,
            pen.carga,
            cli.vendedor,
            pen.codigo_cliente,
            cli.razao_social,
            pen.tipo,
            pen.responsavel,
            pen.codigo_produto,
            pro.descricao,
            pen.quantidade
            FROM {TABELA_PENDENCIAS} AS pen
            LEFT JOIN clientes.{TABELA_CLIENTES} AS cli ON pen.codigo_cliente = cli.codigo
            LEFT JOIN produtos.{TABELA_PRODUTOS} AS pro ON pen.codigo_produto = pro.codigo
            WHERE 1=1
            """

            parametros = []

            if cupom:
                consulta_sql += " AND pen.cupom LIKE ?"
                parametros.append(cupom + "%")
            
            
            if data_inicio and data_fim:
        
                objeto_data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
                objeto_data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

                data_inicio_formatada = objeto_data_inicio.strftime("%Y-%m-%d")
                data_fim_formatada = objeto_data_fim.strftime("%Y-%m-%d")
                
                consulta_sql += f" AND pen.data BETWEEN ? AND ?"
                
                parametros.extend([data_inicio_formatada, data_fim_formatada])


            if carga:
                consulta_sql += " AND pen.carga LIKE ?"
                parametros.append(carga + "%")

            if codigo_cliente:
                consulta_sql += " AND pen.codigo_cliente LIKE ?"
                parametros.append(codigo_cliente + "%")

            if tipo not in ["Pendência", "Troca"]:
                tipo = ""
            if tipo:
                consulta_sql += " AND pen.tipo LIKE ?"
                parametros.append(tipo + "%")

            if codigo_produto:
                consulta_sql += " AND pen.codigo_produto LIKE ?"
                parametros.append(codigo_produto + "%")


            cursor.execute(consulta_sql, parametros)
            resultado = cursor.fetchall()
            conexao.close()

            return resultado
        
        except Exception:
            return []
            
        
        finally:
            if conexao:
                conexao.close()

