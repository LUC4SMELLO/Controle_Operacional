import customtkinter as ctk
from PIL import Image

from constants.paths import ICONS_DIR

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

        self.label_data = ctk.CTkLabel(self, text="", font=("Segoe UI", 14, "bold"), text_color=COR_TEXTO)
        self.label_data.place(x=915, y=120)

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
        self.botao_segunda_feira.place(x=40, y=120)

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
        self.botao_terca_feira.place(x=120, y=120)

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
        self.botao_quarta_feira.place(x=200, y=120)

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
        self.botao_quinta_feira.place(x=280, y=120)

        ctk.CTkLabel(self, text="Número de Cargas:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=40, y=165)
        self.entry_numero_cargas = ctk.CTkEntry(self, font=FONTE_TEXTO, width=30, height=30, corner_radius=2)
        self.entry_numero_cargas.place(x=200, y=165)

        self.botao_utilizar_cargas = ctk.CTkButton(
            self,
            text="Utilizar",
            command=self.controller.criar_cargas,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_utilizar_cargas.place(x=240, y=165)

        self.botao_salvar_escala = ctk.CTkButton(
            self,
            text="Salvar",
            command=self.controller.coletar_dados,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_salvar_escala.place(x=760, y=120)

        self.botao_limpar_escala = ctk.CTkButton(
            self,
            text="Limpar",
            command=self.controller.limpar_cargas,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_limpar_escala.place(x=640, y=120)

        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=210)


        ctk.CTkLabel(self, text="Carga", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=90, y=240)
        ctk.CTkLabel(self, text="Cód", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=185, y=240)
        ctk.CTkLabel(self, text="Nome", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=270, y=240)
        ctk.CTkLabel(self, text="Rota", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=510, y=240)
        ctk.CTkLabel(self, text="Observação", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=750, y=240)



        self.container_cargas = ctk.CTkScrollableFrame(
            self,
            width=950,
            height=350
            )
        self.container_cargas.place(x=40, y=270)
        self.container_cargas._scrollbar.grid_remove()
        
        self.frames_cargas = []  # guarda todas as cargas



        self.icone_mais = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "mais_dark.png"),
            dark_image=Image.open(ICONS_DIR / "mais_dark.png"),
            size=(16, 16)
        )

        self.botao_adicionar_carga = ctk.CTkButton(
            self,
            image=self.icone_mais,
            text="",
            command=self.controller.adicionar_carga_separada,
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_adicionar_carga.place(x=965, y=640)


        self.icone_menos = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "menos_dark.png"),
            dark_image=Image.open(ICONS_DIR / "menos_dark.png"),
            size=(16, 16)
        )

        self.botao_remover_ultima_carga = ctk.CTkButton(
            self,
            image=self.icone_menos,
            text="",
            command=self.controller.remover_ultima_carga,
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_remover_ultima_carga.place(x=915, y=640)
