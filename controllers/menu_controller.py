import customtkinter as ctk

class MenuController:
    def __init__(self):
        self.view = None

    def set_view(self, view):
        self.view = view

    def alternar_modo_aparencia(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def mostrar_opcoes_escala(self):
        self.view.mostrar_opcoes_escala()

    def mostrar_opcoes_pendencia_troca(self):
        self.view.mostrar_opcoes_pendencia_troca()
