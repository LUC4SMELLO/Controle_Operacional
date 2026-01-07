import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from PIL import Image
from tkcalendar import DateEntry


from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_TREE_VIEW,
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

        ctk.CTkLabel(self, text="Relatórios", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=40, y=15)

        ctk.CTkLabel(self, text="Pendência", font=FONTE_SUBTITULO, text_color=COR_TEXTO).place(x=40, y=65)

        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=105)


        ctk.CTkLabel(self, text="Cupom:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=110, y=130)
        self.entry_cupom = ctk.CTkEntry(self, font=FONTE_TEXTO, width=62, height=30, corner_radius=2)
        self.entry_cupom.place(x=177, y=130)

        ctk.CTkLabel(self, text="Data:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=296, y=130)

        self.entry_data = DateEntry(
            self,
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
        self.entry_data.delete(0, ctk.END)
        self.entry_data.place(x=346, y=130)

        ctk.CTkLabel(self, text="Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=515, y=130)
        self.entry_carga = ctk.CTkEntry(self, font=FONTE_TEXTO, width=70, height=30, corner_radius=2)
        self.entry_carga.place(x=570, y=130)

        ctk.CTkLabel(self, text="Tipo:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=755, y=130)
        self.entry_tipo = ctk.CTkComboBox(self, font=FONTE_TEXTO, values=["", "Pendência", "Troca"], width=110, height=30, corner_radius=2)
        self.entry_tipo.set("")
        self.entry_tipo.place(x=801, y=130)



        ctk.CTkLabel(self, text="Código Produto:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=40, y=180)
        self.entry_codigo_produto = ctk.CTkEntry(self, font=FONTE_TEXTO, width=62, height=30, corner_radius=2)
        self.entry_codigo_produto.place(x=177, y=180)

        ctk.CTkLabel(self, text="Quantidade:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=75, y=230)
        self.entry_quantidade = ctk.CTkEntry(self, font=FONTE_TEXTO, width=62, height=30, corner_radius=2)
        self.entry_quantidade.place(x=177, y=230)

        ctk.CTkLabel(self, text="Código Cliente:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=256, y=180)
        self.entry_codigo_cliente = ctk.CTkEntry(self, font=FONTE_TEXTO, width=65, height=30, corner_radius=2)
        self.entry_codigo_cliente.place(x=385, y=180)

        ctk.CTkLabel(self, text="Responsável:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=465, y=180)
        self.entry_responsavel = ctk.CTkEntry(self, font=FONTE_TEXTO, width=150, height=30, corner_radius=2)
        self.entry_responsavel.place(x=570, y=180)

        self.botao_buscar_pendencia = ctk.CTkButton(
            self,
            text="Buscar",
            command=self.controller.mostrar_pendencias,
            width=110,
            height=35,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_buscar_pendencia.place(x=801, y=180)

        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=270)






        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview.Heading",
            font=FONTE_TREE_VIEW,
            background="#343638",
            foreground="#FFFFFF",
        )
        

        colunas = ("cupom", "data", "carga", "codigo_cliente", "tipo", "responsavel", "codigo_produto", "quantidade")
        self.tree = ttk.Treeview(
            self,
            columns=colunas,
            show="headings",
            height=12
            )
        self.tree.place(x=40, y=310, width=935, height=350)

        scroll_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)

        scroll_x.place(x=40, y=660, width=935)
        scroll_y.place(x=975, y=310, height=350)

        self.tree.configure(
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )


        self.tree.heading("cupom", text="Cupom", anchor="center")
        self.tree.heading("data", text="Data", anchor="center")
        self.tree.heading("carga", text="Carga", anchor="center")
        self.tree.heading("codigo_cliente", text="Código Cliente", anchor="center")
        # self.tree.heading("razao_social", text="Razão Social", anchor="center")
        # self.tree.heading("vendedor", text="Vendedor", anchor="center")
        self.tree.heading("tipo", text="Tipo", anchor="center")
        self.tree.heading("responsavel", text="Responsável", anchor="center")
        self.tree.heading("codigo_produto", text="Código Produto", anchor="center")
        self.tree.heading("quantidade", text="Quantidade", anchor="center")

        self.tree.column("cupom", width=70, anchor="center")
        self.tree.column("data", width=80, anchor="center")
        self.tree.column("carga",width=70, anchor="center")
        self.tree.column("codigo_cliente", width=135, anchor="center")
        # self.tree.column("razao_social", width=150, anchor="center")
        # self.tree.column("vendedor", width=90, anchor="center")
        self.tree.column("tipo", width=70, anchor="center")
        self.tree.column("responsavel", width=150, anchor="center")
        self.tree.column("codigo_produto", width= 140, anchor="center")
        self.tree.column("quantidade", width=125, anchor="center")

        self.tree.bind("<MouseWheel>", lambda e: self.tree.yview_scroll(-int(e.delta / 100), "units"))
        self.tree.bind("<Shift-MouseWheel>", lambda e: self.tree.xview_scroll(-int(e.delta / 2.5), "units"))

    def exibir_mensagem(self, titulo, mensagem, icone="info"):
        CTkMessagebox(
            title=titulo,
            message=mensagem,
            icon=icone,
            width=320,
            height=50,
            font=FONTE_TEXTO,
            text_color=COR_TEXTO,
            button_color=COR_BOTAO,
            button_text_color=COR_TEXTO_BOTAO,
            button_hover_color=HOVER_BOTAO,
            option_1="Ok"
            )
