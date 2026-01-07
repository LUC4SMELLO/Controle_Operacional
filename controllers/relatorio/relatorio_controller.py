import customtkinter as ctk
from datetime import date


class RelatorioController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view


    def mostrar_pendencias(self):
        
        resultado = self.model.buscar_pendencias(
            self.view.entry_cupom.get(),
            self.view.entry_data.get(),
            self.view.entry_carga.get(),
            self.view.entry_codigo_cliente.get(),
            self.view.entry_tipo.get(),
            self.view.entry_responsavel.get(),
            self.view.entry_codigo_produto.get(),
            self.view.entry_quantidade.get()
        )

        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        for linha in resultado:
            self.view.tree.insert("", ctk.END, values=linha)