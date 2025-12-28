import customtkinter as ctk

from views.pendencia_troca_view import TelaPendenciaTroca
from controllers.pendencia_troca_controller import PendenciaTrocaController


class MenuController:
    def __init__(self, janela):
        self.janela = janela
        self.view = None
        self.tela_atual = None

    def set_view(self, view):
        self.view = view

    def alternar_modo_aparencia(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def definir_tela_atual(self, nova_tela=None):
        if self.tela_atual:
            self.tela_atual.destroy()
            self.tela_atual = None

        if nova_tela is None:
            return

        self.tela_atual = nova_tela
        self.tela_atual.place(x=255, y=0, relwidth=1, relheight=1)
        self.tela_atual.lift()
        print(f"Nova Tela Agora é", nova_tela)

    def mostrar_opcoes_escala(self):
        self.view.mostrar_opcoes_escala()

    def mostrar_opcoes_pendencia_troca(self):
        self.definir_tela_atual(None)
        self.view.mostrar_opcoes_pendencia_troca()

    def mostrar_tela_pendencia_troca(self):

        controller = PendenciaTrocaController()

        tela_pendencia = TelaPendenciaTroca(self.janela, controller)

        controller.set_view(tela_pendencia)
        
        self.definir_tela_atual(tela_pendencia)
