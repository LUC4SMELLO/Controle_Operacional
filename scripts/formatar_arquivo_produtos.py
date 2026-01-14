import pandas as pd

from constants.arquivos import (
    CAMINHO_ARQUIVO_PRODUTOS_CTA,
    CAMINHO_ARQUIVO_PRODUTOS_FORMATADOS,
)


def formatar_arquivo_produtos():

    df_produtos = pd.read_csv(
        CAMINHO_ARQUIVO_PRODUTOS_CTA,
        header=0,
        delimiter=";",
        encoding="latin1",
        index_col=False,
    )

    print(df_produtos.columns)

    df_produtos = df_produtos[
        [
            "Codigo",
            "Descrição",
            "Grupo",
        ]
    ]

    df_produtos.rename(
        columns={"Codigo": "codigo", "Descrição": "descricao", "Grupo": "grupo"},
        inplace=True,
    )

    df_produtos = df_produtos.apply(
        lambda coluna: coluna.str.strip() if coluna.dtype == "object" else coluna
    )

    df_produtos = df_produtos[df_produtos["grupo"] != "099-MATERIAL"]

    df_produtos = df_produtos[~df_produtos["codigo"].isin([120, 121, 118286])]

    df_produtos.drop(columns=["grupo"], inplace=True)



    df_produtos.to_csv(CAMINHO_ARQUIVO_PRODUTOS_FORMATADOS, sep=";", index=False)
