import customtkinter as ctk


class PendenciaController:
    def __init__(self):
        self.view = None

    def set_view(self, view):
        self.view = view
    
    def configurar_binds(self, view):


        if view == "cadastrar":
            self.view.entry_carga.focus_set()

            fluxo_entrys = [
                (self.view.entry_carga, self.view.entry_codigo_cliente),
                (self.view.entry_codigo_cliente, self.view.entry_tipo),
                (self.view.entry_tipo, self.view.entry_responsavel),
                (self.view.entry_responsavel, self.view.entry_codigo_produto),
                (self.view.entry_codigo_produto, self.view.entry_quantidade),
                (self.view.entry_quantidade, self.view.botao_confirmar)
            ]
        else:
            self.view.entry_cupom.focus_set()

            fluxo_entrys = [
                (self.view.entry_cupom, self.view.botao_buscar_cupom),
                (self.view.botao_buscar_cupom, self.view.entry_carga),
                (self.view.entry_carga, self.view.entry_codigo_cliente),
                (self.view.entry_codigo_cliente, self.view.entry_tipo),
                (self.view.entry_tipo, self.view.entry_responsavel),
                (self.view.entry_responsavel, self.view.entry_codigo_produto),
                (self.view.entry_codigo_produto, self.view.entry_quantidade),
                (self.view.entry_quantidade, self.view.botao_confirmar)
            ]

        for widget_atual, proximo_widget in fluxo_entrys:
            widget_atual.bind("<Return>", lambda event, nxt=proximo_widget: self.focar_proximo(nxt))

    def focar_proximo(self, proximo_widget):
        proximo_widget.focus_set()
        return "break"