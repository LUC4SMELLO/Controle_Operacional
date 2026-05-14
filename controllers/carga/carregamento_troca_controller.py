from controllers.carga.carregamento_troca_bind_controller import CarregamentoTrocaBindController


class CarregamentoTrocaController:
    def __init__(self, model):
        self.model = model
        self.view = None

        self.binds = CarregamentoTrocaBindController(self)

    def set_view(self, view):
        self.view = view

        self.binds.set_view(view)

    def atualizar_numero_total_itens(self):
        total_itens = len(self.view.tree.get_children())
        self.view.label_numero_total_itens.configure(text=f"Total: {total_itens}")

    def buscar_pendencias(self):

        pendencias = self.model.buscar_pendencias()
        if pendencias:
            return pendencias
        else:
            return False

    def limpar_pendencias(self):
        for widget in self.view.pendencias_scroll.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        self.view.linhas.clear()
