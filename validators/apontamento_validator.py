from datetime import time
import re


def validar_apontamento(dados: dict):
    padrao = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

    obrigatorios = [
        "hora_saida", "hora_chegada",
        "km_inicial", "km_final",
    ]

    for linha in dados:
        numero_carga = linha.get("numero_carga")
        hora_saida = linha.get("hora_saida")
        hora_chegada = linha.get("hora_chegada")
        km_inicial = str(linha.get("km_inicial")).replace(",", "").replace(".", "")
        km_final = str(linha.get("km_final")).replace(",", "").replace(".", "")

        for campo in obrigatorios:

            valor = linha.get(campo)
            if not valor or str(valor).strip() == "":
                return {
                    "sucesso": False,
                    "titulo": "Erro",
                    "mensagem": f"O campo '{campo.replace('_', ' ').replace('sai', 'saí').title()}' da carga {numero_carga} é obrigatório!",
                    "icone": "cancel"
                }

        if not re.fullmatch(padrao, hora_saida):
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"O campo 'Hora Saída' da carga {numero_carga} é inválido.",
                "icone": "cancel"
            }
        
        if not re.fullmatch(padrao, hora_chegada):
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"O campo 'Hora Chegada' da carga {numero_carga} é inválido.",
                "icone": "cancel"
            }
        
        if time.fromisoformat(hora_saida) > time.fromisoformat(hora_chegada):
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"A hora de saída não pode ser posterior à hora de chegada, carga {numero_carga}.",
                "icone": "cancel"
            }

        if int(km_final) < int(km_inicial):
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"O km final tem que ser maior que o km inicial, carga {numero_carga}.",
                "icone": "cancel"
            }

    return {
        "sucesso": True,
        "titulo": "Sucesso",
        "mensagem": "Informações válidas.",
        "icone": "check"
    }


        