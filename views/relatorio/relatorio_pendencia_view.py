import customtkinter as ctk
from tkinter import ttk
from PIL import Image
from tkcalendar import DateEntry

from views.dialogs.exibir_mensagem import exibir_mensagem

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_CABECALHO_TREE_VIEW,
    FONTE_TEXTO_TREE_VIEW,
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
    COR_TEXTO_BOTAO,
    COR_BACKGROUND_HEADING_TREE,
    COR_FOREGROUND_HEADING_TREE,
    COR_BACKGROUND_HEADING_HOVER_TREE,
    COR_FOREGROUND_HEADING_HOVER_TREE,
    COR_BACKGROUND_VALORES_HOVER_TREE,
    COR_FOREGROUND_VALORES_HOVER_TREE

)

from constants.date_entry import (
    BACKGROUND,
    FOREGROUND,
    HEADERSBACKGROUND,
    HEADERSFOREGROUND,
    NORMALBACKGROUND,
    NORMALFOREGROUND,
    WEEKENDBACKGROUND,
    WEEKENDFOREGROUND,
    SELECTBACKGROUND,
    SELECTFOREGROUND,
    BORDERCOLOR,
    BORDERWIDTH
)


class RelatorioPendenciaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0) # HEADER
        self.main_frame.grid_rowconfigure(1, weight=0) # FILTERBAR 1
        self.main_frame.grid_rowconfigure(2, weight=0) # FILTERBAR 2
        self.main_frame.grid_rowconfigure(3, weight=0) # TREEVIEW PENDÊNCIAS
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

        ctk.CTkLabel(self.header_frame, text="Relatórios", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Pendência", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")

        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=2)



        self.filterbar_frame_1 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.filterbar_frame_1.grid_rowconfigure(0, weight=1)
        self.filterbar_frame_1.grid_columnconfigure(0, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(1, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(2, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(3, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(4, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(5, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(6, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(7, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(8, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(9, weight=0)
        self.filterbar_frame_1.grid_columnconfigure(10, weight=1)
        self.filterbar_frame_1.grid_columnconfigure(11, weight=0)
        self.filterbar_frame_1.grid(
            row=1,
            column=0,
            sticky="ew",
        )

        ctk.CTkLabel(self.filterbar_frame_1, text="Período:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 5), pady=(15, 0))

        self.entry_data_inicio = DateEntry(
            self.filterbar_frame_1,
            justify = "center", 
            font = FONTE_PEQUENA,
            background = BACKGROUND,
            foreground = FOREGROUND,       
            headersbackground = HEADERSBACKGROUND, 
            headersforeground = HEADERSFOREGROUND, 
            normalbackground = NORMALBACKGROUND, 
            normalforeground = NORMALFOREGROUND, 
            weekendbackground = WEEKENDBACKGROUND,
            weekendforeground = WEEKENDFOREGROUND,
            selectbackground = SELECTBACKGROUND, 
            selectforeground = SELECTFOREGROUND, 
            bordercolor = BORDERCOLOR,      
            borderwidth = BORDERWIDTH,
            selectmode = 'day',
            date_pattern = 'dd/mm/yyyy',
            width=11
            )
        self.entry_data_inicio.delete(0, ctk.END)
        self.entry_data_inicio.grid(row=0, column=1, padx=(10, 10), pady=(15, 0))

        ctk.CTkLabel(self.filterbar_frame_1, text="a", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=2, padx=(0, 0), pady=(15, 0))
        
        self.entry_data_fim = DateEntry(
            self.filterbar_frame_1,
            justify = "center", 
            font = FONTE_PEQUENA,
            background = BACKGROUND,
            foreground = FOREGROUND,       
            headersbackground = HEADERSBACKGROUND, 
            headersforeground = HEADERSFOREGROUND, 
            normalbackground = NORMALBACKGROUND, 
            normalforeground = NORMALFOREGROUND, 
            weekendbackground = WEEKENDBACKGROUND,
            weekendforeground = WEEKENDFOREGROUND,
            selectbackground = SELECTBACKGROUND, 
            selectforeground = SELECTFOREGROUND, 
            bordercolor = BORDERCOLOR,      
            borderwidth = BORDERWIDTH,
            selectmode = 'day',
            date_pattern = 'dd/mm/yyyy',
            width=11
            )
        self.entry_data_fim.delete(0, ctk.END)
        self.entry_data_fim.grid(row=0, column=3, padx=(10, 0), pady=(15, 0))

        ctk.CTkLabel(self.filterbar_frame_1, text="Cupom:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=4, padx=(20, 0), pady=(15, 0))
        self.entry_cupom = ctk.CTkEntry(self.filterbar_frame_1, font=FONTE_TEXTO, width=62, height=30, corner_radius=2)
        self.entry_cupom.grid(row=0, column=5, padx=(10, 0), pady=(15, 0))

        ctk.CTkLabel(self.filterbar_frame_1, text="Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=6, padx=(10, 0), pady=(15, 0))
        self.entry_carga = ctk.CTkEntry(self.filterbar_frame_1, font=FONTE_TEXTO, width=70, height=30, corner_radius=2)
        self.entry_carga.grid(row=0, column=7, padx=(10, 0), pady=(15, 0))

        ctk.CTkLabel(self.filterbar_frame_1, text="Tipo:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=8, padx=(10, 0), pady=(15, 0))
        self.entry_tipo = ctk.CTkComboBox(self.filterbar_frame_1, font=FONTE_TEXTO, justify="center", values=["Ambos", "Pendência", "Troca"], width=110, height=30, corner_radius=2)
        self.entry_tipo.set("Ambos")
        self.entry_tipo.grid(row=0, column=9, padx=(10, 0), pady=(15, 0))


        self.botao_buscar_pendencia = ctk.CTkButton(
            self.filterbar_frame_1,
            text="Buscar",
            command=self.buscar,
            width=110,
            height=35,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_buscar_pendencia.grid(row=0, column=11, padx=(10, 290), pady=(15, 0))




        self.filterbar_frame_2 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.filterbar_frame_2.grid_rowconfigure(0, weight=1)
        self.filterbar_frame_2.grid_columnconfigure(0, weight=0)
        self.filterbar_frame_2.grid_columnconfigure(1, weight=0)
        self.filterbar_frame_2.grid_columnconfigure(2, weight=0)
        self.filterbar_frame_2.grid_columnconfigure(3, weight=0)
        self.filterbar_frame_2.grid_columnconfigure(4, weight=1)
        self.filterbar_frame_2.grid_columnconfigure(5, weight=0)
        self.filterbar_frame_2.grid(
            row=2,
            column=0,
            sticky="ew",
        )

        ctk.CTkLabel(self.filterbar_frame_2, text="Código Cliente:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0))
        self.entry_codigo_cliente = ctk.CTkEntry(self.filterbar_frame_2, font=FONTE_TEXTO, width=65, height=30, corner_radius=2)
        self.entry_codigo_cliente.grid(row=0, column=1, padx=(10, 0), pady=(15, 0))

        ctk.CTkLabel(self.filterbar_frame_2, text="Código Produto:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=2, padx=(10, 0), pady=(15, 0))
        self.entry_codigo_produto = ctk.CTkEntry(self.filterbar_frame_2, font=FONTE_TEXTO, width=62, height=30, corner_radius=2)
        self.entry_codigo_produto.grid(row=0, column=3, padx=(10, 0), pady=(15, 0))


        self.botao_limpar_filtros = ctk.CTkButton(
            self.filterbar_frame_2,
            text="Limpar\nFiltros",
            command=self.controller.limpar_filtros,
            width=110,
            height=35,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_limpar_filtros.grid(row=0, column=5, padx=(10, 290), pady=(15, 0))

        ctk.CTkFrame(self.filterbar_frame_2, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=6)



        self.container_treeview = ctk.CTkFrame(self.main_frame, fg_color="transparent", height=550)
        self.container_treeview.grid_rowconfigure(0, weight=1)
        self.container_treeview.grid_columnconfigure(0, weight=0)
        self.container_treeview.grid_columnconfigure(1, weight=1)
        self.container_treeview.grid_columnconfigure(2, weight=0)
        self.container_treeview.grid(
            row=3,
            column=0,
            sticky="ew"
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
        

        colunas = ("cupom", "data", "carga", "vendedor", "codigo_cliente", "razao_social", "tipo", "responsavel", "codigo_produto", "descricao", "quantidade")
        self.tree = ttk.Treeview(
            self.container_treeview,
            columns=colunas,
            show="headings",
            height=12
            )
        self.tree.grid(row=0, column=1, padx=(40, 5), pady=(15, 0))

        self.tree.heading("cupom", text="Cupom", anchor="center")
        self.tree.heading("data", text="Data", anchor="center")
        self.tree.heading("carga", text="Carga", anchor="center")
        self.tree.heading("vendedor", text="Vendedor", anchor="center")
        self.tree.heading("codigo_cliente", text="Código Cliente", anchor="center")
        self.tree.heading("razao_social", text="Razão Social", anchor="center")
        self.tree.heading("tipo", text="Tipo", anchor="center")
        self.tree.heading("responsavel", text="Responsável", anchor="center")
        self.tree.heading("codigo_produto", text="Código Produto", anchor="center")
        self.tree.heading("descricao", text="Descrição", anchor="center")
        self.tree.heading("quantidade", text="Quantidade", anchor="center")

        self.tree.column("cupom", width=90, anchor="center")
        self.tree.column("data", width=125, anchor="center")
        self.tree.column("carga",width=115, anchor="center")
        self.tree.column("vendedor", width=115, anchor="center")
        self.tree.column("codigo_cliente", width=160, anchor="center")
        self.tree.column("razao_social", width=280, anchor="center")
        self.tree.column("tipo", width=110, anchor="center")
        self.tree.column("responsavel", width=190, anchor="center")
        self.tree.column("codigo_produto", width=175, anchor="center")
        self.tree.column("descricao", width=280, anchor="center")
        self.tree.column("quantidade", width=140, anchor="center")
        
        scroll_x = ttk.Scrollbar(self.container_treeview, orient="horizontal", command=self.tree.xview)
        scroll_y = ttk.Scrollbar(self.container_treeview, orient="vertical", command=self.tree.yview)

        scroll_x.grid(row=1, column=0, padx=(40, 305), pady=(5, 0), sticky="we", columnspan=3)
        scroll_y.grid(row=0, column=2, padx=(0, 290), pady=(15, 0), sticky="ns")


        self.tree.configure(
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        self.tree.bind("<MouseWheel>", lambda e: self.tree.yview_scroll(-int(e.delta / 100), "units"))
        self.tree.bind("<Shift-MouseWheel>", lambda e: self.tree.xview_scroll(-int(e.delta / 2.5), "units"))

    def buscar(self):
        resultado = self.controller.mostrar_pendencias()

        if resultado["sucesso"]:
            return

        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])
        return