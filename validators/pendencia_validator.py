from datetime import datetime 


def validar_pendencia(dados: dict, exigir_cupom: bool = False):
    obrigatorios = [
        "data", "carga", "codigo_cliente", "tipo",
        "responsavel", "codigo_produto", "quantidade"
    ]

    if exigir_cupom:
        obrigatorios.insert(0, "cupom")


    for campo in obrigatorios:
        valor = dados.get(campo)
        if not valor or str(valor).strip() == "":
            return {
                "sucesso": False, 
                "titulo": "Erro",
                "mensagem": f"O campo '{campo.replace('_', ' ').replace('co', 'có').replace('sa', 'sá').title()}' é obrigatório!",
                "icone": "cancel"
            }
        
    try:
        datetime.strptime(dados["data"], "%Y-%m-%d")
        pass
    except ValueError:
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "A data não é inválida.",
            "icone": "cancel"
        }
        
    if dados["tipo"] not in ("Pendência", "Troca"):
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "O valor do campo 'Tipo' está incorreto.",
            "icone": "cancel"
        }

    try:
        if int(dados["quantidade"]) <= 0:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "A quantidade deve ser maior que zero.",
                "icone": "cancel"
            }
    except ValueError:
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "Quantidade inválida.",
            "icone": "cancel"
        }

    return {
            "sucesso": True,
            "titulo": "Sucesso",
            "mensagem": "Pendencia Cadastrada.",
            "icone": "check"
        }
