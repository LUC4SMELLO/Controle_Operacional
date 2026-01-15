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
    FONTE_BOTAO_SECUNDARIO,
)

from constants.cores import COR_LINHAS

from constants.cores import COR_BOTAO, HOVER_BOTAO, COR_TEXTO, COR_TEXTO_BOTAO


class EditarEscalaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Escala", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=40, y=15)

        ctk.CTkLabel(self, text="Editar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).place(x=40, y=65)

        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=105)

        self.label_data = ctk.CTkLabel(self, text="15/01/2026", font=("Segoe UI", 14, "bold"), text_color=COR_TEXTO)
        self.label_data.place(x=915, y=130)

        self.botao_segunda_feira = ctk.CTkButton(
            self,
            text="Segunda",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_segunda_feira.place(x=40, y=130)

        self.botao_terca_feira = ctk.CTkButton(
            self,
            text="Terça",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_terca_feira.place(x=120, y=130)

        self.botao_quarta_feira = ctk.CTkButton(
            self,
            text="Quarta",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_quarta_feira.place(x=200, y=130)

        self.botao_quinta_feira = ctk.CTkButton(
            self,
            text="Quinta",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_quinta_feira.place(x=280, y=130)

        ctk.CTkLabel(self, text="Número de Cargas:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=40, y=180)
        self.entry_numero_cargas = ctk.CTkEntry(self, font=FONTE_TEXTO, width=30, height=30, corner_radius=2)
        self.entry_numero_cargas.place(x=200, y=180)

        self.botao_utilizar_cargas = ctk.CTkButton(
            self,
            text="Utilizar",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_utilizar_cargas.place(x=240, y=180)

        self.botao_salvar_escala = ctk.CTkButton(
            self,
            text="Salvar",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_salvar_escala.place(x=760, y=130)

        self.botao_limpar_escala = ctk.CTkButton(
            self,
            text="Limpar",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_limpar_escala.place(x=640, y=130)



        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=235)