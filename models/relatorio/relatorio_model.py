from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from constants.banco_dados import TABELA_PENDENCIAS

class RelatorioModel:
    def __init__(self):
        pass

    def buscar_pendencias(
            self,
            cupom="",
            data="",
            carga="",
            codigo_cliente="",
            tipo="",
            responsavel="",
            codigo_produto="",
            quantidade=""
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
        
        if data:
            consulta_sql += " AND data LIKE ?"
            parametros.append("%" + data + "%")

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

        if responsavel:
            consulta_sql += " AND responsavel LIKE ?"
            parametros.append("%" + responsavel + "%")

        if codigo_produto:
            consulta_sql += " AND codigo_produto LIKE ?"
            parametros.append("%" + codigo_produto + "%")

        if quantidade:
            consulta_sql += " AND quantidade LIKE ?"
            parametros.append("%" + quantidade + "%")


        cursor.execute(consulta_sql, parametros)
        resultado = cursor.fetchall()
        conexao.close()

        return resultado

