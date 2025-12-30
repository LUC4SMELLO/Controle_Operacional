from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from constants.banco_dados import TABELA_PENDENCIAS

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
