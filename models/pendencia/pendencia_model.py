from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias
from constants.banco_dados import TABELA_PENDENCIAS

from database.banco_dados_clientes import conectar_banco_de_dados_clientes
from constants.banco_dados import TABELA_CLIENTES, BANCO_DADOS_CLIENTES

from database.banco_dados_produtos import conectar_banco_de_dados_produtos
from constants.banco_dados import TABELA_PRODUTOS, BANCO_DADOS_PRODUTOS


class PendenciaModel:
    def __init__(self):
        pass

    def cadastrar_pendencia(self, dados):
    
        conexao = conectar_banco_de_dados_pendencias()
        cursor = conexao.cursor()
        
        cursor.execute(
            f"""
            INSERT INTO {TABELA_PENDENCIAS} (
            data,
            carga,
            codigo_cliente,
            tipo,
            responsavel,
            codigo_produto,
            quantidade
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    dados["data"],
                    dados["carga"],
                    dados["codigo_cliente"],
                    dados["tipo"],
                    dados["responsavel"],
                    dados["codigo_produto"],
                    dados["quantidade"]
                )
            )
        
        conexao.commit()
        conexao.close()

    def editar_pendencia(self, dados):

        conexao = conectar_banco_de_dados_pendencias()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            UPDATE {TABELA_PENDENCIAS}
            SET data = ?,
            carga = ?,
            codigo_cliente = ?,
            tipo = ?,
            responsavel = ?,
            codigo_produto = ?,
            quantidade = ?
            WHERE cupom = ?
            """,
                (
                    dados["data"],
                    dados["carga"],
                    dados["codigo_cliente"],
                    dados["tipo"],
                    dados["responsavel"],
                    dados["codigo_produto"],
                    dados["quantidade"],
                    dados["cupom"]
                )
            )

        conexao.commit()
        conexao.close()

    def excluir_pendencia(self, cupom):

        conexao = conectar_banco_de_dados_pendencias()
        cursor = conexao.cursor()
        
        cursor.execute(
        f"""
        DELETE FROM {TABELA_PENDENCIAS}
        WHERE cupom = ?
        """, (cupom,)
        )

        conexao.commit()
        conexao.close()


    def buscar_pendencia(self, cupom):

        try:
            conexao = conectar_banco_de_dados_pendencias()
            cursor = conexao.cursor()

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_CLIENTES}' AS clientes")

            cursor.execute(f"ATTACH DATABASE '{BANCO_DADOS_PRODUTOS}' AS produtos")


            cursor.execute(f"""
            SELECT
            pen.cupom,
            pen.data,
            pen.carga,
            pen.codigo_cliente,
            cli.razao_social,
            pen.tipo,
            pen.responsavel,
            pen.codigo_produto,
            pro.descricao,
            pen.quantidade
            FROM {TABELA_PENDENCIAS} AS pen
            JOIN clientes.{TABELA_CLIENTES} AS cli ON pen.codigo_cliente = cli.codigo
            JOIN produtos.{TABELA_PRODUTOS} AS pro ON pen.codigo_produto = pro.codigo
            WHERE pen.cupom = ?
            """, (cupom,)
            )

            resultado = cursor.fetchone()

            return resultado
        
        finally:
            conexao.close()

    
    def buscar_cliente(self, codigo_cliente):

        conexao = conectar_banco_de_dados_clientes()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        SELECT
        razao_social
        FROM {TABELA_CLIENTES}
        WHERE codigo = ?
        """, (codigo_cliente,)
        )

        resultado = cursor.fetchone()

        conexao.close()

        return resultado
    

    def buscar_produto(self, codigo_produto):

        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        SELECT
        descricao
        FROM {TABELA_PRODUTOS}
        WHERE codigo = ?
        """, (codigo_produto,)
        )

        resultado = cursor.fetchone()

        conexao.close()

        return resultado

