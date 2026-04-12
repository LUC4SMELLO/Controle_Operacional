import customtkinter as ctk
from tkinter import ttk

from PIL import Image

from constants.paths import ICONS_DIR

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


class CarregamentoTrocaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2, weight=0)
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

        ctk.CTkLabel(self.header_frame, text="Carregamento Troca", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")

        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=1)


        self.toolbar_frame_1 = ctk.CTkFrame(self.main_frame, height=40, fg_color="transparent")
        self.toolbar_frame_1.grid_rowconfigure(0, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(0, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(1, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(2, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(3, weight=0)
        self.toolbar_frame_1.grid(row=1, column=0, sticky="ew")

        ctk.CTkLabel(self.toolbar_frame_1, text="Última Atualização Arquivo:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="e")
        label_ultima_atualizacao = ctk.CTkLabel(self.toolbar_frame_1, text="11/04/2026 - 19:30", font=("Segoe UI", 16), text_color=COR_TEXTO)
        label_ultima_atualizacao.grid(row=0, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

        icone_atualizar_arquivo = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "reiniciar_dark.png"),
            dark_image=Image.open(ICONS_DIR / "reiniciar_dark.png"),
            size=(23, 23)
        )

        self.botao_atualizar_arquivo = ctk.CTkButton(
            self.toolbar_frame_1,
            image=icone_atualizar_arquivo,
            text="",
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_atualizar_arquivo.grid(row=0, column=3, padx=(0, 290), pady=(15, 0), sticky="e")

        ctk.CTkFrame(self.toolbar_frame_1, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=5)


        self.container_treeview = ctk.CTkFrame(self.main_frame, height=400, fg_color="transparent")
        self.container_treeview.grid_rowconfigure(0, weight=1)
        self.container_treeview.grid_rowconfigure(1, weight=0)
        self.container_treeview.grid_columnconfigure(0, weight=1)
        self.container_treeview.grid_columnconfigure(1, weight=0)
        self.container_treeview.grid(
            row=2,
            column=0,
            sticky="we"
        )

        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview.Heading",
            font=FONTE_CABECALHO_TREE_VIEW,
            background=COR_BACKGROUND_HEADING_TREE,
            foreground=COR_FOREGROUND_HEADING_TREE,
        )
        style.map(
            "Treeview.Heading",
            background=[("active", COR_BACKGROUND_HEADING_HOVER_TREE)],
            foreground=[("active", COR_FOREGROUND_HEADING_HOVER_TREE)]
        )
        style.configure(
            "Treeview",
            font=FONTE_TEXTO_TREE_VIEW,
            rowheight=40,
        )
        style.map(
            "Treeview", 
            background=[('selected', COR_BACKGROUND_VALORES_HOVER_TREE)],
            foreground=[('selected', COR_FOREGROUND_VALORES_HOVER_TREE)]
        )

        colunas = ("cupom", "codigo_cliente", "razao_social", "rota", "tipo", "codigo_produto", "quantidade")
        self.tree = ttk.Treeview(
            self.container_treeview,
            columns=colunas,
            show="headings",
            height=10
            )
        self.tree.grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="we")

        self.tree.heading("cupom", text="Cupom", anchor="center")
        self.tree.heading("codigo_cliente", text="Código Cliente", anchor="center")
        self.tree.heading("razao_social", text="Razão Social", anchor="center")
        self.tree.heading("rota", text="Rota", anchor="center")
        self.tree.heading("tipo", text="Tipo", anchor="center")
        self.tree.heading("codigo_produto", text="Código Produto", anchor="center")
        self.tree.heading("quantidade", text="Quantidade", anchor="center")

        self.tree.column("cupom", width=90, anchor="center")
        self.tree.column("codigo_cliente", width=160, anchor="center")
        self.tree.column("razao_social", width=280, anchor="center")
        self.tree.column("rota", width=160, anchor="center")
        self.tree.column("tipo", width=110, anchor="center")
        self.tree.column("codigo_produto", width=175, anchor="center")
        self.tree.column("quantidade", width=140, anchor="center")

        scroll_x = ttk.Scrollbar(self.container_treeview, orient="horizontal", command=self.tree.xview)
        scroll_y = ttk.Scrollbar(self.container_treeview, orient="vertical", command=self.tree.yview)

        scroll_x.grid(row=1, column=0, padx=(40, 5), pady=(0, 15), sticky="we")
        scroll_y.grid(row=0, column=1, padx=(0, 290), pady=(15, 0), sticky="ns")


        self.tree.configure(
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        self.tree.bind("<MouseWheel>", lambda e: self.tree.yview_scroll(-int(e.delta / 100), "units"))
        self.tree.bind("<Shift-MouseWheel>", lambda e: self.tree.xview_scroll(-int(e.delta / 2.5), "units"))

        self.footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.footer_frame.grid_columnconfigure(0, minsize=100)
        self.footer_frame.grid(
            row=3,
            column=0,
            sticky="ew"
        )

        
        self.label_numero_total_itens = ctk.CTkLabel(
            self.footer_frame,
            text="Total: 0",
            font=("Segoe UI", 14, "bold"),
            text_color=COR_TEXTO,
            anchor="w"
        )
        self.label_numero_total_itens.grid(row=0, column=0, padx=(40, 0), sticky="w")
