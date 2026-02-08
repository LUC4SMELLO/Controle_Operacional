from datetime import datetime


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

        print(data)

        cargas = self.model.buscar_escalas_por_data(data)
        self.view.exibir_cargas(cargas)
