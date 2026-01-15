import customtkinter as ctk
from PIL import Image
from tkcalendar import DateEntry

from views.dialogs.exibir_mensagem import exibir_mensagem

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_TEXTO,
    FONTE_PEQUENA,
    FONTE_BOTAO_PRINCIPAL,
    FONTE_BOTAO_SECUNDARIO
)

from constants.cores import COR_LINHAS

from constants.cores import (
    COR_BOTAO,
    HOVER_BOTAO,
    COR_TEXTO,
    COR_TEXTO_BOTAO
)


class EditarEscalaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller


        ctk.CTkLabel(self, text="Escala", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=40, y=15)

        ctk.CTkLabel(self, text="Editar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).place(x=40, y=65)

        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=105)