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

    def atualizar_carga_entregue(self, linha, entry_atual):

        indice_atual = self.view.linhas_pendencia.index(linha)

        cupom = self.view.linhas_pendencia[indice_atual].label_cupom.cget("text")
        carga_entregue = entry_atual.get()

        print(cupom, carga_entregue)

        self.model.atualizar_carga_entregue(cupom, carga_entregue)

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
        self.view.linhas_pendencia.clear()
