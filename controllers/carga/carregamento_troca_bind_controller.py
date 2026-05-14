class CarregamentoTrocaBindController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None
    
    def set_view(self, view):
        self.view = view
    
    def focar_proximo(self, entry_atual):
        try:
            indice_atual = self.view.entradas_carga.index(entry_atual)
            
            proximo_indice = indice_atual + 1
            
            if proximo_indice < len(self.view.entradas_carga):
                proxima_entry = self.view.entradas_carga[proximo_indice]
                proxima_entry.focus()
            else:

                pass
        except ValueError:
            pass
