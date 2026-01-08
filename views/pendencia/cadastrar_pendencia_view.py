import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
from tkcalendar import DateEntry

from views.dialogs.pesquisa_produto_view import TelaPesquisaProdutoView

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
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


class CadastrarPendenciaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Pendência & Troca", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=40, y=15)

        ctk.CTkLabel(self, text="Cadastrar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).place(x=40, y=65)

        ctk.CTkFrame(self, width=500, height=2, fg_color=COR_LINHAS).place(x=40, y=105)

        ctk.CTkLabel(self, text="Data:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=135, y=130)

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
        self.entry_data.place(x=184, y=130)
        
        ctk.CTkLabel(self, text="Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=127, y=165)
        self.entry_carga = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_carga.place(x=184, y=165)


        ctk.CTkLabel(self, text="Código Cliente:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=55, y=200)
        self.entry_codigo_cliente = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_cliente.place(x=184, y=200)


        ctk.CTkLabel(self, text="Tipo:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=138, y=235)
        self.entry_tipo = ctk.CTkComboBox(self, font=FONTE_TEXTO, values=["Pendência", "Troca"], width=150, height=30, corner_radius=2)
        self.entry_tipo.set("")
        self.entry_tipo.place(x=184, y=235)

        ctk.CTkLabel(self, text="Responsável:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=77, y=270)
        self.entry_responsavel = ctk.CTkEntry(self, font=FONTE_TEXTO, width=150, height=30, corner_radius=2)
        self.entry_responsavel.place(x=184, y=270)

        ctk.CTkFrame(self, width=500, height=2, fg_color=COR_LINHAS).place(x=40, y=325)

        ctk.CTkLabel(self, text="Código Produto:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=45, y=350)
        self.entry_codigo_produto = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_produto.place(x=184, y=350)

        icone_lupa = ctk.CTkImage(
            light_image=Image.open("assets/icons/lupa_light.png"),
            dark_image=Image.open("assets/icons/lupa_dark.png"),
            size=(23, 23)
        )

        self.botao_buscar = ctk.CTkButton(
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
        self.botao_buscar.place(x=295, y=350)

        ctk.CTkLabel(self, text="Quantidade:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=79, y=385)
        self.entry_quantidade = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_quantidade.place(x=184, y=385)

        ctk.CTkFrame(self, width=500, height=2, fg_color=COR_LINHAS).place(x=40, y=440)

        self.botao_confirmar = ctk.CTkButton(
            self,
            text="Cadastrar",
            command=self.controller.confirmar_cadastro_pendencia,
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color= COR_TEXTO_BOTAO,
        )
        self.botao_confirmar.place(x=200, y=465)

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
        self.botao_cancelar.place(x=382, y=465)

    def abrir_tela_pesquisa_produto(self):
        TelaPesquisaProdutoView(self, self.entry_codigo_produto, self.entry_quantidade)



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
