import customtkinter as ctk

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_BOTAO_PRINCIPAL
from constants.textos import FONTE_BOTAO_SECUNDARIO

from constants.cores import COR_LINHAS


class TelaPendenciaTroca(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Pendência", font=FONTE_TITULO).place(x=15, y=15)
