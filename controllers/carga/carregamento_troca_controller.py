class CarregamentoTrocaController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def atualizar_numero_total_itens(self):
        total_itens = len(self.view.tree.get_children())
        self.view.label_numero_total_itens.configure(text=f"Total: {total_itens}")