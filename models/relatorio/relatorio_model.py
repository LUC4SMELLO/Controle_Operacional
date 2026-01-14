from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from constants.banco_dados import BANCO_DADOS_CLIENTES, TABELA_CLIENTES, TABELA_PENDENCIAS

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
            pen.quantidade
            FROM {TABELA_PENDENCIAS} AS pen
            LEFT JOIN clientes.{TABELA_CLIENTES} AS cli ON pen.codigo_cliente = cli.codigo
            WHERE 1=1
            """

            parametros = []

            if cupom:
                consulta_sql += " AND pen.cupom LIKE ?"
                parametros.append(cupom + "%")
            
            
            if data_inicio and data_fim:
        
                formato_iso = "substr(pen.data, 7, 4) || '-' || substr(pen.data, 4, 2) || '-' || substr(pen.data, 1, 2)"
                
                consulta_sql += f" AND {formato_iso} BETWEEN ? AND ?"
                
                inicio_iso = f"{data_inicio[6:10]}-{data_inicio[3:5]}-{data_inicio[0:2]}"
                fim_iso = f"{data_fim[6:10]}-{data_fim[3:5]}-{data_fim[0:2]}"
                
                parametros.extend([inicio_iso, fim_iso])


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

