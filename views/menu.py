import customtkinter as ctk
from PIL import Image

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_BOTAO

from constants.cores import COR_LINHAS


class TelaMenu(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Menu", font=FONTE_TITULO).place(x=15, y=15)

        ctk.CTkFrame(self, width=2, height=1280, fg_color=COR_LINHAS).place(x=250, relx=0, relheight=1)

        self.switch_alternar_modo = ctk.CTkSwitch(self, text="Tema", font=FONTE_SUBTITULO,command=self.controller.alternar_modo_aparencia)
        self.switch_alternar_modo.place(relx=1, x=-5, y=15, anchor="ne")

        self.botao_escala = ctk.CTkButton(self, text="Escala", font=FONTE_BOTAO,)
        self.botao_escala.place(x=10, y=100)

        self.botao_pendencia = ctk.CTkButton(self, text="Pendência", font=FONTE_BOTAO,)
        self.botao_pendencia.place(x=10, y=130)

        self.botao_troca = ctk.CTkButton(self, text="Troca", font=FONTE_BOTAO,) 
        self.botao_troca.place(x=10, y=160)

        self.botao_relatorio_entrega = ctk.CTkButton(self, text="Relátorio Entrega", font=FONTE_BOTAO,)
        self.botao_relatorio_entrega.place(x=10, y=190)
        


