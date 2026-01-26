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

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0) # HEADER
        self.main_frame.grid_rowconfigure(1, weight=0) # TOOLBAR 1
        self.main_frame.grid_rowconfigure(2, weight=0) # TOOLBAR 2
        self.main_frame.grid_rowconfigure(3, weight=0) # CABEÇALHO CARGAS
        self.main_frame.grid_rowconfigure(4, weight=1) # CONTAINER CARGAS
        self.main_frame.grid_rowconfigure(5, weight=0) # FOOTER
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")


        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_rowconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=0)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid(
            row=0,
            column=0,
            sticky="ew",
        )

        ctk.CTkLabel(self.header_frame, text="Escala", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Editar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")

        self.label_data = ctk.CTkLabel(self.header_frame, text="", font=("Segoe UI", 14, "bold"), text_color=COR_TEXTO)
        self.label_data.grid(row=1, column=1, padx=(0, 290), pady=(20, 0), sticky="e")

        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=2)

        

        self.toolbar_frame_1 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_frame_1.grid_rowconfigure(0, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(0, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(1, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(2, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(3, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(4, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(5, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(6, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(7, weight=0)
        self.toolbar_frame_1.grid(
            row=1,
            column=0,
            sticky="ew",
        )



        ctk.CTkLabel(self.toolbar_frame_1, text="Dia da Semana:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(69, 0), pady=(15, 0))
        self.botao_segunda_feira = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Segunda",
            command=lambda: self.controller.mostrar_escala_dia_semana("segunda"),
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_segunda_feira.grid(row=0, column=1, padx=(15, 5), pady=(15, 0))

        self.botao_terca_feira = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Terça",
            command=lambda: self.controller.mostrar_escala_dia_semana("terça"),
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_terca_feira.grid(row=0, column=2, padx=(0, 5), pady=(15, 0), sticky="w")

        self.botao_quarta_feira = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Quarta",
            command=lambda: self.controller.mostrar_escala_dia_semana("quarta"),
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_quarta_feira.grid(row=0, column=3, padx=(0, 5), pady=(15, 0), sticky="w")

        self.botao_quinta_feira = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Quinta",
            command=lambda: self.controller.mostrar_escala_dia_semana("quinta"),
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_quinta_feira.grid(row=0, column=4, padx=(0, 50), pady=(15, 0), sticky="w")


        self.botao_limpar_escala = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Limpar",
            command=self.controller.limpar_cargas,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_limpar_escala.grid(row=0, column=6, padx=(0, 10), pady=(15, 0))

        self.botao_salvar_escala = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Salvar",
            command=self.controller.confirmar,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_salvar_escala.grid(row=0, column=7, padx=(0, 290), pady=(15, 0))




        self.toolbar_frame_2 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_frame_2.grid_rowconfigure(0, weight=1)
        self.toolbar_frame_2.grid_rowconfigure(1, minsize=2)
        self.toolbar_frame_2.grid_columnconfigure(0, weight=0)
        self.toolbar_frame_2.grid_columnconfigure(1, weight=0)
        self.toolbar_frame_2.grid_columnconfigure(2, weight=0)
        self.toolbar_frame_2.grid_columnconfigure(3, weight=0)
        self.toolbar_frame_2.grid_columnconfigure(4, weight=0)
        self.toolbar_frame_2.grid_columnconfigure(5, weight=0)
        self.toolbar_frame_2.grid_columnconfigure(6, weight=1)
        self.toolbar_frame_2.grid(
            row=2,
            column=0,
            sticky="ew",
        )

        ctk.CTkLabel(self.toolbar_frame_2, text="Número de Cargas:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(5, 0), sticky="w")
        self.entry_numero_cargas = ctk.CTkEntry(self.toolbar_frame_2, font=FONTE_TEXTO, width=73, height=30, corner_radius=2)
        self.entry_numero_cargas.grid(row=0, column=1, padx=(15, 5), pady=(5, 0), sticky="w")

        self.botao_utilizar_cargas = ctk.CTkButton(
            self.toolbar_frame_2,
            text="Utilizar",
            command=self.controller.criar_cargas,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=105,
            height=30
        )
        self.botao_utilizar_cargas.grid(row=0, column=2, padx=(0, 5), pady=(5, 0), sticky="w")

        self.icone_mais = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "mais_dark.png"),
            dark_image=Image.open(ICONS_DIR / "mais_dark.png"),
            size=(18, 18)
        )
        self.botao_adicionar_carga = ctk.CTkButton(
            self.toolbar_frame_2,
            image=self.icone_mais,
            text="",
            command=self.controller.adicionar_carga_separada,
            width=20,
            height=30,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_adicionar_carga.grid(row=0, column=3, padx=(0, 5), pady=(5, 0), sticky="w")

        self.icone_seta_cima = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "seta_cima_dark.png"),
            dark_image=Image.open(ICONS_DIR / "seta_cima_dark.png"),
            size=(16, 16)
        )
        self.botao_ir_para_o_topo = ctk.CTkButton(
            self.toolbar_frame_2,
            image=self.icone_seta_cima,
            text="",
            command=self.controller.scroll_topo,
            width=15,
            height=30,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_ir_para_o_topo.grid(row=0, column=4, padx=(0, 5), pady=(5, 0), sticky="w")

        self.icone_seta_baixo = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "seta_baixo_dark.png"),
            dark_image=Image.open(ICONS_DIR / "seta_baixo_dark.png"),
            size=(16, 16)
        )
        self.botao_ir_para_o_final = ctk.CTkButton(
            self.toolbar_frame_2,
            image=self.icone_seta_baixo,
            text="",
            command=self.controller.scroll_final,
            width=15,
            height=30,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_ir_para_o_final.grid(row=0, column=5, padx=(0, 5), pady=(5, 0), sticky="w")

        ctk.CTkFrame(self.toolbar_frame_2, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=7)

        self.cabecalho_cargas = ctk.CTkFrame(self.main_frame)
        self.cabecalho_cargas.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=(40, 290),
            pady=(10)
        )

        # colunas do cabeçalho
        self.cabecalho_cargas.grid_columnconfigure(0, weight=0)  # Carga
        self.cabecalho_cargas.grid_columnconfigure(1, weight=0)  # Cód
        self.cabecalho_cargas.grid_columnconfigure(2, weight=3)  # Nome (mais largo)
        self.cabecalho_cargas.grid_columnconfigure(3, weight=3)  # Rota
        self.cabecalho_cargas.grid_columnconfigure(4, weight=3)  # Observação


        ctk.CTkLabel(
            self.cabecalho_cargas,
            text="Carga",
            font=FONTE_LABEL,
            text_color=COR_TEXTO
        ).grid(row=0, column=0, padx=35, sticky="w")

        ctk.CTkLabel(
            self.cabecalho_cargas,
            text="Cód",
            font=FONTE_LABEL,
            text_color=COR_TEXTO
        ).grid(row=0, column=1, padx=(0, 100), sticky="w")

        ctk.CTkLabel(
            self.cabecalho_cargas,
            text="Nome",
            font=FONTE_LABEL,
            text_color=COR_TEXTO
        ).grid(row=0, column=2, padx=10, sticky="w")

        ctk.CTkLabel(
            self.cabecalho_cargas,
            text="Rota",
            font=FONTE_LABEL,
            text_color=COR_TEXTO
        ).grid(row=0, column=3, padx=10, sticky="w")

        ctk.CTkLabel(
            self.cabecalho_cargas,
            text="Observação",
            font=FONTE_LABEL,
            text_color=COR_TEXTO
        ).grid(row=0, column=4, padx=10, sticky="w")




        self.container_cargas = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="#434548",
            height=550
        )
        self.container_cargas.grid(
            row=4,
            column=0,
            sticky="nsew",
            padx=(40, 290),
            pady=(5, 0)
        )

        self.container_cargas._scrollbar.grid_remove()
        self.frames_cargas = []


        self.footer_frame = ctk.CTkFrame(self.main_frame)
        self.footer_frame.grid_columnconfigure(0, minsize=100)
        self.footer_frame.grid_columnconfigure(1, minsize=100)
        self.footer_frame.grid_columnconfigure(2, minsize=100)
        self.footer_frame.grid_columnconfigure(3, minsize=100)
        self.footer_frame.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=(40, 290),
            pady=(10, 15)
        )

        self.label_numero_total_cargas = ctk.CTkLabel(
            self.footer_frame,
            text="Total: 0",
            font=("Segoe UI", 14, "bold"),
            text_color=COR_TEXTO,
            anchor="w"
        )
        self.label_numero_total_cargas.grid(row=0, column=0, padx=(0, 0), sticky="w")

        self.label_numero_repetidos = ctk.CTkLabel(
            self.footer_frame,
            text="Repetidos: 0",
            font=("Segoe UI", 14, "bold"),
            text_color=COR_TEXTO,
            anchor="w"
        )
        self.label_numero_repetidos.grid(row=0, column=1, padx=(0, 45), sticky="w")

        self.label_numero_total_motoristas = ctk.CTkLabel(
            self.footer_frame,
            text="Motoristas: 0",
            font=("Segoe UI", 14, "bold"),
            text_color=COR_TEXTO,
            anchor="w"
        )
        self.label_numero_total_motoristas.grid(row=0, column=2, padx=(0, 45), sticky="w")

        self.label_numero_total_ajudantes = ctk.CTkLabel(
            self.footer_frame,
            text="Ajudantes: 0",
            font=("Segoe UI", 14, "bold"),
            text_color=COR_TEXTO,
            anchor="w"
        )
        self.label_numero_total_ajudantes.grid(row=0, column=3, padx=(0, 45), sticky="w")
