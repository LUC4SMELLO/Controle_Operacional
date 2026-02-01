def validar_veiculo(dados: dict):
    obrigatorios = [
        "codigo", "placa"
    ]

    if dados["codigo_motorista"]:
        obrigatorios.insert(0, "codigo_motorista")

    for campo in obrigatorios:
        valor = dados.get(campo)
        if not valor or str(valor).strip() == "":
            return {
                "sucesso": False, 
                "titulo": "Erro",
                "mensagem": f"O campo '{campo.replace('_', ' ').replace('co', 'có').replace('cao', 'ção').title()}' é obrigatório!",
                "icone": "cancel"
            }
    
    if dados["codigo_motorista"]:
        try:
            if int(dados["codigo_motorista"]) <= 0:
                raise ValueError
        except ValueError:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "Código do motorista inválido.",
                "icone": "cancel"
            }
        
    return {
        "sucesso": True,
        "titulo": "Sucesso",
        "mensagem": "Veículo Cadastrado.",
        "icone": "check"
    }