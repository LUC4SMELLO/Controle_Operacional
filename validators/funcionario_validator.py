import re

from validate_docbr import CPF


def validar_funcionario(dados: dict):
    obrigatorios = [
        "codigo", "nome_completo",
        "cpf", "rg", "funcao"
    ]

    for campo in obrigatorios:
        valor = dados.get(campo)
        if not valor or str(valor).strip() == "":
            return {
                "sucesso": False, 
                "titulo": "Erro",
                "mensagem": f"O campo '{campo.replace('_', ' ').replace('co', 'có').replace('cao', 'ção').title()}' é obrigatório!",
                "icone": "cancel"
            }
    
    if dados["funcao"] not in ("Motorista", "Ajudante"):
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "O valor do campo 'Função' está incorreto.",
            "icone": "cancel"
        }
    
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if not re.fullmatch(padrao, dados["cpf"]):
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "O formato do CPF é inválido.",
            "icone": "cancel"
        }
        
    cpf = CPF()
    if not cpf.validate(dados["cpf"]):
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "O 'CPF' é inválido.",
            "icone": "cancel"
        }
    
    return {
        "sucesso": True,
        "titulo": "Sucesso",
        "mensagem": "Funcionário Cadastrado.",
        "icone": "check"
    }
