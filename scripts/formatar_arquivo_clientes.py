import pandas as pd

from constants.arquivos import CAMINHO_ARQUIVO_CLIENTES_CTA, CAMINHO_ARQUIVO_CLIENTES_FORMATADOS


def formatar_arquivo_clientes():

    df_clientes = pd.read_csv(CAMINHO_ARQUIVO_CLIENTES_CTA, encoding="windows-1252", sep=";")

    df_clientes = df_clientes[
        [
            "CODIGO",
            "RAZÃO",
            "FANTASIA",
            "CIDADE",
            "VENDEDOR",
            "ESTATUS",
            "SEMANA",
            "ROTA",
        ]
    ]

    df_clientes.rename(
        columns={
            "CODIGO": "codigo",
            "RAZÃO": "razao",
            "FANTASIA": "fantasia",
            "CIDADE": "cidade",
            "VENDEDOR": "vendedor",
            "ESTATUS": "estatus",
            "SEMANA": "semana",
            "ROTA": "rota",
        },
        inplace=True
    )

    df_clientes = df_clientes.apply(
        lambda coluna: coluna.str.strip() if coluna.dtype == "object" else coluna
    )

    df_clientes = df_clientes[df_clientes["estatus"] == "ATIVO"]

    df_clientes["vendedor"] = df_clientes["vendedor"].str.extract(r"(\d+)").astype("Int64")



    df_clientes.to_csv(CAMINHO_ARQUIVO_CLIENTES_FORMATADOS, sep=";", index=False)
