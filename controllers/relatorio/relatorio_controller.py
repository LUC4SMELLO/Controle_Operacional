import customtkinter as ctk
from datetime import date


class RelatorioController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view


    def mostrar_pendencias(self):
        
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        resultado = self.model.buscar_pendencias(
            self.view.entry_cupom.get(),
            self.view.entry_data_inicio.get(),
            self.view.entry_data_fim.get(),
            self.view.entry_carga.get(),
            self.view.entry_codigo_cliente.get(),
            self.view.entry_tipo.get(),
            self.view.entry_codigo_produto.get(),
        )

        if not resultado:
            return {
                "sucesso": False,
                "titulo": "Aviso.",
                "mensagem": "Não há pendências com esses filtros.",
                "icone": "warning"
                }
        
        for linha in resultado:
            self.view.tree.insert("", ctk.END, values=linha)

        return {
            "sucesso": True,
            "titulo": "Sucesso",
            "mensagem": "Pendência Encontradas!",
            "icone": "check"
            }
    

    def limpar_filtros(self):

        for item in self.view.tree.get_children():
            self.view.tree.delete(item)
        
        self.view.entry_cupom.delete(0, ctk.END)
        self.view.entry_data_inicio.delete(0, ctk.END)
        self.view.entry_data_fim.delete(0, ctk.END)
        self.view.entry_carga.delete(0, ctk.END)
        self.view.entry_codigo_cliente.delete(0, ctk.END)
        self.view.entry_tipo.set("Ambos")
        self.view.entry_codigo_produto.delete(0, ctk.END)

        