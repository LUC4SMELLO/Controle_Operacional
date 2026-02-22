import customtkinter as ctk
from PIL import Image
from tkcalendar import DateEntry

from views.dialogs.exibir_mensagem import exibir_mensagem

from views.dialogs.pesquisa_cliente_view import TelaPesquisaClienteView

from views.dialogs.pesquisa_produto_view import TelaPesquisaProdutoView

from constants.paths import ICONS_DIR

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_LABEL
from constants.textos import FONTE_TEXTO
from constants.textos import FONTE_PEQUENA
from constants.textos import FONTE_BOTAO_PRINCIPAL
from constants.textos import FONTE_BOTAO_SECUNDARIO

from constants.cores import COR_LINHAS

from constants.cores import (COR_BOTAO, HOVER_BOTAO, COR_TEXTO, COR_TEXTO_BOTAO)

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
class ExcluirPendenciaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        icone_lupa = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "lupa_dark.png"),
            dark_image=Image.open(ICONS_DIR / "lupa_dark.png"),
            size=(23, 23)
        )

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

        ctk.CTkLabel(self.header_frame, text="Pendência & Troca", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Excluir", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")


        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=1)

        self.edicao_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.edicao_frame.grid_rowconfigure(1, weight=0)
        self.edicao_frame.grid_rowconfigure(1, weight=0)
        self.edicao_frame.grid_rowconfigure(2, weight=0)
        self.edicao_frame.grid_rowconfigure(3, weight=0)
        self.edicao_frame.grid_columnconfigure(0, weight=0)
        self.edicao_frame.grid_columnconfigure(1, weight=0)
        self.edicao_frame.grid_columnconfigure(2, weight=0)
        self.edicao_frame.grid_columnconfigure(3, weight=1)
        self.edicao_frame.grid_columnconfigure(4, weight=0)
        self.edicao_frame.grid(row=1, column=0, sticky="ew")

        ctk.CTkLabel(self.edicao_frame, text="Cupom:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="e")
        self.entry_cupom = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_cupom.grid(row=0, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

        self.botao_buscar_cupom = ctk.CTkButton(
            self.edicao_frame,
            text="Buscar",
            command=self.buscar_cupom,
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            )
        self.botao_buscar_cupom.grid(row=0, column=2, padx=(10, 0), pady=(15, 0), sticky="w")


        ctk.CTkFrame(self.edicao_frame, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=5)


        ctk.CTkLabel(self.edicao_frame, text="Data:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=2, column=0, padx=(40, 0), pady=(15, 0), sticky="e")

        self.entry_data = DateEntry(
            self.edicao_frame,
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
            width=16
            )
        self.entry_data.grid(row=2, column=1, padx=(10, 0), pady=(15, 0), sticky="w", columnspan=2)
        
        ctk.CTkLabel(self.edicao_frame, text="Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=3, column=0, padx=(40, 0), pady=(10, 0), sticky="e")
        self.entry_carga = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_carga.grid(row=3, column=1, padx=(10, 0), pady=(10, 0), sticky="w")

        ctk.CTkLabel(self.edicao_frame, text="Código Cliente:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=4, column=0, padx=(40, 0), pady=(10, 0), sticky="e")
        self.entry_codigo_cliente = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_cliente.grid(row=4, column=1, padx=(10, 0), pady=(10, 0), sticky="w")

        self.botao_pesquisar_cliente = ctk.CTkButton(
            self.edicao_frame,
            image=icone_lupa,
            text="",
            command=self.abrir_tela_pesquisa_cliente,
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_pesquisar_cliente.grid(row=4, column=2, padx=(10, 0), pady=(10, 0), sticky="w")

        self.label_razao_social = ctk.CTkLabel(self.edicao_frame, text="", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_razao_social.grid(row=4, column=3, padx=(25, 0), pady=(10, 0), sticky="w")

        ctk.CTkLabel(self.edicao_frame, text="Tipo:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=5, column=0, padx=(40, 0), pady=(10, 0), sticky="e")
        self.entry_tipo = ctk.CTkComboBox(self.edicao_frame, font=FONTE_TEXTO, values=["Pendência", "Troca"], width=150, height=30, corner_radius=2)
        self.entry_tipo.set("")
        self.entry_tipo.grid(row=5, column=1, padx=(10, 0), pady=(10, 0), sticky="w", columnspan=2)

        ctk.CTkLabel(self.edicao_frame, text="Responsável:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=6, column=0, padx=(40, 0), pady=(10, 0), sticky="e")
        self.entry_responsavel = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=150, height=30, corner_radius=2)
        self.entry_responsavel.grid(row=6, column=1, padx=(10, 0), pady=(10, 0), sticky="w", columnspan=2)

        ctk.CTkFrame(self.edicao_frame, height=2, fg_color=COR_LINHAS).grid(row=7, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=5)

        ctk.CTkLabel(self.edicao_frame, text="Código Produto:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=8, column=0, padx=(40, 0), pady=(15, 0), sticky="e")
        self.entry_codigo_produto = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_produto.grid(row=8, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

        self.botao_pesquisar_produto = ctk.CTkButton(
            self.edicao_frame,
            image=icone_lupa,
            text="",
            command=self.abrir_tela_pesquisa_produto,
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_pesquisar_produto.grid(row=8, column=2, padx=(10, 0), pady=(15, 0), sticky="w")

        self.label_descricao_produto = ctk.CTkLabel(self.edicao_frame, text="", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_descricao_produto.grid(row=8, column=3, padx=(25, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.edicao_frame, text="Quantidade:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=9, column=0, padx=(40, 0), pady=(10, 0), sticky="e")
        self.entry_quantidade = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_quantidade.grid(row=9, column=1, padx=(10, 0), pady=(10, 0))

        ctk.CTkFrame(self.edicao_frame, height=2, fg_color=COR_LINHAS).grid(row=10, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=5)

        self.footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.footer_frame.grid_columnconfigure(0, minsize=100)
        self.footer_frame.grid_columnconfigure(1, minsize=100)
        self.footer_frame.grid_columnconfigure(2, minsize=100)
        self.footer_frame.grid_columnconfigure(3, minsize=100)
        self.footer_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=(40, 290),
        )

        self.botao_confirmar = ctk.CTkButton(
            self.footer_frame,
            text="Confirmar",
            font=FONTE_BOTAO_PRINCIPAL,
            command=self.confirmar,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color= COR_TEXTO_BOTAO,
        )
        self.botao_confirmar.grid(row=0, column=2, padx=(10, 0), pady=(25, 0))

        self.botao_cancelar= ctk.CTkButton(
            self.footer_frame,
            text="Cancelar",
            font=FONTE_BOTAO_PRINCIPAL,
            command=self.controller.limpar_formulario,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
        )
        self.botao_cancelar.grid(row=0, column=3, padx=(10, 0), pady=(25, 0))

    def confirmar(self):

        resposta = exibir_mensagem(
            titulo="Confirmar Exclusão",
            mensagem="Tem certeza que deseja excluir esta pendência?",
            icone="warning",
            opcao_1="Não",
            opcao_2="Sim"
            )
        
        if resposta != "Sim":
            self.controller.limpar_formulario()
            return "break"
        
        resultado = self.controller.confirmar_exclusao_pendencia()

        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])
        return "break"
    
    def buscar_cupom(self):
        resultado = self.controller.buscar_e_exibir_informacoes_pendencia(tipo_view="excluir")

        if resultado["sucesso"]:
            return

        self.entry_cupom.focus_set()
        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])
        return "break"

    def abrir_tela_pesquisa_cliente(self):
        TelaPesquisaClienteView(self, self.entry_codigo_cliente, self.entry_tipo, self.label_razao_social)

    def abrir_tela_pesquisa_produto(self):
        TelaPesquisaProdutoView(self, self.entry_codigo_produto, self.entry_quantidade, self.label_descricao_produto)
