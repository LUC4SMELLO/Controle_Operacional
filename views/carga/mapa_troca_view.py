import customtkinter as ctk
from tkinter import ttk

from PIL import Image

from constants.paths import ICONS_DIR, REPORTS_IMAGES_DIR

from views.dialogs.exibir_mensagem import exibir_mensagem

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_TEXTO,
    FONTE_CABECALHO_TREE_VIEW,
    FONTE_TEXTO_TREE_VIEW,
    FONTE_PEQUENA,
    FONTE_BOTAO_PRINCIPAL,
    FONTE_BOTAO_SECUNDARIO
)

from constants.cores import (
    COR_BOTAO,
    HOVER_BOTAO,
    COR_TEXTO,
    COR_TEXTO_BOTAO,
    COR_LINHAS,
    COR_FUNDO_CONTAINER_CARGAS,
    COR_FUNDO_FRAME_CARGAS,
    COR_BACKGROUND_HEADING_TREE,
    COR_FOREGROUND_HEADING_TREE,
    COR_BACKGROUND_HEADING_HOVER_TREE,
    COR_FOREGROUND_HEADING_HOVER_TREE,
    COR_BACKGROUND_VALORES_HOVER_TREE,
    COR_FOREGROUND_VALORES_HOVER_TREE

)

from constants.cores import (
    COR_BOTAO,
    HOVER_BOTAO,
    COR_TEXTO,
    COR_TEXTO_BOTAO
)


class MapaTrocaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.imagens_originais = []
        self.imagens_tk = []
        self.zoom = 1.0

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2, weight=0)
        self.main_frame.grid_rowconfigure(3, weight=0)
        self.main_frame.grid_rowconfigure(4, weight=1)
        self.main_frame.grid_rowconfigure(5, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_rowconfigure(1, weight=1)
        self.header_frame.grid_rowconfigure(2, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.header_frame, text="Carga", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Mapa de Troca", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")

        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=1)

        self.toolbar_frame_1 = ctk.CTkFrame(self.main_frame, fg_color="#D42222")
        self.toolbar_frame_1.grid_rowconfigure(0, weight=0)
        self.toolbar_frame_1.grid_rowconfigure(1, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(0, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(1, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(2, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(3, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(4, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(5, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(6, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(7, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(8, weight=0)
        self.toolbar_frame_1.grid(row=1, column=0, sticky="we")


        ctk.CTkLabel(self.toolbar_frame_1, text="Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0))
        self.entry_numero_carga = ctk.CTkEntry(self.toolbar_frame_1, font=FONTE_TEXTO, text_color=COR_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_numero_carga.grid(row=0, column=1, padx=(10, 0), pady=(15, 0))

        self.botao_buscar = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Buscar",
            command=self.buscar_mapa,
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_buscar.grid(row=0, column=2, padx=(10, 0), pady=(15, 0))


        self.botao_imprimir = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Imprimir",
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
            )
        self.botao_imprimir.grid(row=0, column=8, padx=(10, 290), pady=(15, 0), sticky="w")

        ctk.CTkFrame(self.toolbar_frame_1, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=9)



        self.visualizar_frame = ctk.CTkFrame(self.main_frame, fg_color="#810151")
        self.visualizar_frame.grid_rowconfigure(0, weight=1)
        self.visualizar_frame.grid_columnconfigure(0, weight=0)
        self.visualizar_frame.grid_columnconfigure(1, weight=0)
        self.visualizar_frame.grid_columnconfigure(2, weight=1)
        self.visualizar_frame.grid(row=4, column=0, padx=(40, 290), sticky="nsew")



        self.canvas = ctk.CTkCanvas(
            self.visualizar_frame,
            bg="#C2C2C2",
            highlightthickness=0,
            bd=0
        )
        self.canvas.grid(row=0, column=0, pady=(30, 30), sticky="nsew", columnspan=3)

        scroll_x = ttk.Scrollbar(self.canvas, orient="horizontal", command=self.canvas.xview)
        scroll_y = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        self.canvas.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(-int(e.delta / 100), "units"))
        self.canvas.bind("<Shift-MouseWheel>", lambda e: self.canvas.xview_scroll(-int(e.delta / 2.5), "units"))
        self.canvas.bind("<Control-MouseWheel>", self.controller.zoom_mousewheel)


    def buscar_mapa(self):

        self.controller.limpar_imagem_mapa()

        resultado = self.controller.exibir_mapa()

        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])

        if not resultado["sucesso"]:
            return "break"
        
        self.canvas.delete("all")
        self.imagens_tk.clear()

        for nome in ["mapa.png"]:
            caminho = REPORTS_IMAGES_DIR / nome
            if caminho.exists():
                self.imagens_originais.append(Image.open(caminho))

        self.zoom = 0.6

        self.controller.redesenhar_imagens()

        return "break"

