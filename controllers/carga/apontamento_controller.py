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


        cargas = self.model.buscar_escalas_por_data(data)
        self.view.exibir_cargas(cargas)

    def limpar_cargas(self):
        for widget in self.view.cargas_scroll.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        self.view.linhas.clear()
