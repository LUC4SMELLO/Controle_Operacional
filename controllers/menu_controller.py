import customtkinter as ctk

from views.pendencia_troca_view import TelaPendenciaTroca
from controllers.pendencia_troca_controller import PendenciaTrocaController


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

    def mostrar_tela_pendencia_troca(self):
        
        from views.janela import janela

        controller = PendenciaTrocaController()

        tela_pendencia = TelaPendenciaTroca(janela, controller)

        controller.set_view(tela_pendencia)
        
        tela_pendencia.place(x=255, y=0, relwidth=1, relheight=1)
    
        tela_pendencia.lift()
