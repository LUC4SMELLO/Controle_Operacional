import customtkinter as ctk
from PIL import Image
from tkcalendar import DateEntry

from views.dialogs.exibir_mensagem import exibir_mensagem

from views.dialogs.pesquisa_cliente_view import TelaPesquisaClienteView

from views.dialogs.pesquisa_produto_view import TelaPesquisaProdutoView

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
class EditarPendenciaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller
        

        icone_lupa = ctk.CTkImage(
            light_image=Image.open("assets/icons/lupa_dark.png"),
            dark_image=Image.open("assets/icons/lupa_dark.png"),
            size=(23, 23)
        )

        ctk.CTkLabel(self, text="Pendência & Troca", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=40, y=15)

        ctk.CTkLabel(self, text="Editar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).place(x=40, y=65)

        ctk.CTkFrame(self, width=650, height=2, fg_color=COR_LINHAS).place(x=40, y=105)

        ctk.CTkLabel(self, text="Cupom:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=115, y=130)
        self.entry_cupom = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_cupom.place(x=184, y=130)

        self.botao_buscar_cupom = ctk.CTkButton(
            self,
            text="Buscar",
            command=self.buscar_cupom,
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            )
        self.botao_buscar_cupom.place(x=295, y=130)


        ctk.CTkFrame(self, width=650, height=2, fg_color=COR_LINHAS).place(x=40, y=180)

        ctk.CTkLabel(self, text="Data:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=135, y=210)

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
            width=16
            )
        self.entry_data.place(x=184, y=210)
        
        ctk.CTkLabel(self, text="Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=127, y=245)
        self.entry_carga = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_carga.place(x=184, y=245)


        ctk.CTkLabel(self, text="Código Cliente:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=55, y=280)
        self.entry_codigo_cliente = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_cliente.place(x=184, y=280)

        self.botao_pesquisar_cliente = ctk.CTkButton(
            self,
            image=icone_lupa,
            text="",
            command=self.abrir_tela_pesquisa_cliente,
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_pesquisar_cliente.place(x=295, y=280)

        self.label_razao_social = ctk.CTkLabel(self, text="", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_razao_social.place(x=350, y=280)


        ctk.CTkLabel(self, text="Tipo:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=138, y=315)
        self.entry_tipo = ctk.CTkComboBox(self, font=FONTE_TEXTO, values=["Pendência", "Troca"], width=150, height=30, corner_radius=2)
        self.entry_tipo.set("")
        self.entry_tipo.place(x=184, y=315)

        ctk.CTkLabel(self, text="Responsável:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=77, y=350)
        self.entry_responsavel = ctk.CTkEntry(self, font=FONTE_TEXTO, width=150, height=30, corner_radius=2)
        self.entry_responsavel.place(x=184, y=350)

        ctk.CTkFrame(self, width=650, height=2, fg_color=COR_LINHAS).place(x=40, y=405)

        ctk.CTkLabel(self, text="Código Produto:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=45, y=430)
        self.entry_codigo_produto = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_produto.place(x=184, y=430)

        self.botao_pesquisar_produto = ctk.CTkButton(
            self,
            image=icone_lupa,
            text="",
            command=self.abrir_tela_pesquisa_produto,
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_pesquisar_produto.place(x=295, y=430)

        self.label_descricao_produto = ctk.CTkLabel(self, text="", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_descricao_produto.place(x=350, y=430)

        ctk.CTkLabel(self, text="Quantidade:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=79, y=465)
        self.entry_quantidade = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_quantidade.place(x=184, y=465)

        ctk.CTkFrame(self, width=650, height=2, fg_color=COR_LINHAS).place(x=40, y=520)

        self.botao_confirmar = ctk.CTkButton(
            self,
            text="Confirmar",
            font=FONTE_BOTAO_PRINCIPAL,
            command=self.confirmar,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color= COR_TEXTO_BOTAO,
        )
        self.botao_confirmar.place(x=350, y=545)

        self.botao_cancelar= ctk.CTkButton(
            self,
            text="Cancelar",
            font=FONTE_BOTAO_PRINCIPAL,
            command=self.controller.limpar_formulario,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
        )
        self.botao_cancelar.place(x=532, y=545)

    def confirmar(self):
        resultado = self.controller.confirmar_edicao_pendencia()

        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])
        return "break"
    
    def buscar_cupom(self):
        resultado = self.controller.buscar_e_exibir_informacoes_pendencia(tipo_view="editar")

        if resultado["sucesso"]:
            return

        self.entry_cupom.focus_set()
        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])
        return "break"

    def abrir_tela_pesquisa_cliente(self):
        TelaPesquisaClienteView(self, self.entry_codigo_cliente, self.entry_tipo, self.label_razao_social)

    def abrir_tela_pesquisa_produto(self):
        TelaPesquisaProdutoView(self, self.entry_codigo_produto, self.entry_quantidade, self.label_descricao_produto)
