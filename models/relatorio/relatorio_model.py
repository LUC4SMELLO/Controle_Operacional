from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from constants.banco_dados import TABELA_PENDENCIAS

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


        conexao = conectar_banco_de_dados_pendencias()
        cursor = conexao.cursor()

        consulta_sql = f"""
        SELECT
        cupom,
        data,
        carga,
        codigo_cliente,
        tipo,
        responsavel,
        codigo_produto,
        quantidade
        FROM {TABELA_PENDENCIAS}
        WHERE 1=1
        """

        parametros = []

        if cupom:
            consulta_sql += " AND cupom LIKE ?"
            parametros.append("%" + cupom + "%")
        
        
        if data_inicio and data_fim:
    
            formato_iso = "substr(data, 7, 4) || '-' || substr(data, 4, 2) || '-' || substr(data, 1, 2)"
            
            consulta_sql += f" AND {formato_iso} BETWEEN ? AND ?"
            
            inicio_iso = f"{data_inicio[6:10]}-{data_inicio[3:5]}-{data_inicio[0:2]}"
            fim_iso = f"{data_fim[6:10]}-{data_fim[3:5]}-{data_fim[0:2]}"
            
            parametros.extend([inicio_iso, fim_iso])


        if carga:
            consulta_sql += " AND carga LIKE ?"
            parametros.append("%" + carga + "%")

        if codigo_cliente:
            consulta_sql += " AND codigo_cliente LIKE ?"
            parametros.append("%" + codigo_cliente + "%")

        if tipo not in ["Pendência", "Troca"]:
            tipo = ""
        if tipo:
            consulta_sql += " AND tipo LIKE ?"
            parametros.append("%" + tipo + "%")

        if codigo_produto:
            consulta_sql += " AND codigo_produto LIKE ?"
            parametros.append("%" + codigo_produto + "%")


        cursor.execute(consulta_sql, parametros)
        resultado = cursor.fetchall()
        conexao.close()

        return resultado

