import customtkinter as ctk
from PIL import Image

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_BOTAO_PRINCIPAL
from constants.textos import FONTE_BOTAO_SECUNDARIO

from constants.cores import COR_LINHAS


class TelaMenu(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Menu", font=FONTE_TITULO).place(x=15, y=15)

        ctk.CTkFrame(self, width=2, height=1280, fg_color=COR_LINHAS).place(x=250, relx=0, relheight=1)

        self.switch_alternar_modo = ctk.CTkSwitch(self, text="Tema", font=FONTE_SUBTITULO,command=self.controller.alternar_modo_aparencia)
        self.switch_alternar_modo.place(relx=1, x=-5, y=15, anchor="ne")

        # BOTÕES PRINCIPAIS

        self.botao_escala = ctk.CTkButton(self, text="Escala", font=FONTE_BOTAO_PRINCIPAL, width=160, height=38, command=self.controller.mostrar_opcoes_escala)
        self.botao_escala.place(x=10, y=100)

        self.botao_pendencia = ctk.CTkButton(self, text="Pendência & Troca", font=FONTE_BOTAO_PRINCIPAL, width=160, height=38,)
        self.botao_pendencia.place(x=10, y=140)


        # BOTÕES SECUNDARIOS

        self.botao_criar_escala = ctk.CTkButton(self, text="Editar", font=FONTE_BOTAO_SECUNDARIO)
        self.botao_visualizar_escala =ctk.CTkButton(self, text="Visualizar", font=FONTE_BOTAO_SECUNDARIO)

        self.botao_cadastrar_pendencia_troca = ctk.CTkButton(self, text="Cadastrar", font=FONTE_BOTAO_SECUNDARIO)
        self.botao_editar_pendencia_troca = ctk.CTkButton(self, text="Editar", font=FONTE_BOTAO_SECUNDARIO)
        self.botao_excluir_pendencia_troca = ctk.CTkButton(self, text="Excluir", font=FONTE_BOTAO_SECUNDARIO)

    def mostrar_opcoes_escala(self):
        self.botao_pendencia.place(x=10, y=210)

        self.botao_criar_escala.place(x=50, y=140)
        self.botao_visualizar_escala.place(x=50, y=170)
