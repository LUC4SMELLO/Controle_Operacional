from datetime import datetime

from validators.apontamento_validator import validar_apontamento


class ApontamentoController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def buscar_cargas(self, data):
        try:
            objeto_data = datetime.strptime(data, "%d/%m/%Y")
            data = objeto_data.strftime("%Y-%m-%d")
        except Exception:
            data = "."


        cargas = self.model.buscar_escalas_por_data(data)
        self.view.exibir_cargas(cargas)

    def limpar_cargas(self):
        for widget in self.view.cargas_scroll.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        self.view.linhas.clear()

    def coletar_dados(self):
        dados = []
        for numero_carga, campos in self.view.linhas.items():
            km_inicial = campos["km_inicial"].get()
            km_final = campos["km_final"].get()
            hora_saida = campos["hora_saida"].get()
            hora_chegada = campos["hora_chegada"].get()

            dados.append({
                "numero_carga": numero_carga, 
                "km_inicial": km_inicial,
                "km_final": km_final,
                "hora_saida": hora_saida,
                "hora_chegada": hora_chegada
                })

        return dados

    def salvar_apontamento(self):
        dados = self.coletar_dados()

        resultado = validar_apontamento(dados)
        if not resultado["sucesso"]:
            return resultado

        try:
            for linha in dados:
                self.model.salvar_apontamento(linha)
            self.limpar_cargas()
            return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Apontamento Salvo!",
                "icone": "check"
            }
        except Exception as e:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {e}",
                "icone": "cancel"
            }