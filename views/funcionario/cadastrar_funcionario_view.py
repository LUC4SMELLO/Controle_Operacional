import customtkinter as ctk

from views.dialogs.exibir_mensagem import exibir_mensagem

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


class CadastrarFuncionarioView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0) # HEADER
        self.main_frame.grid_rowconfigure(1, weight=0) # CADASTRO
        self.main_frame.grid_rowconfigure(2, weight=0) # FOOTER
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")


        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_rowconfigure(1, weight=1)
        self.header_frame.grid_rowconfigure(2, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.header_frame, text="Funcionários", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Cadastrar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")


        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=1)


        self.cadastro_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.cadastro_frame.grid_rowconfigure(1, weight=0)
        self.cadastro_frame.grid_rowconfigure(1, weight=0)
        self.cadastro_frame.grid_rowconfigure(2, weight=0)
        self.cadastro_frame.grid_rowconfigure(3, weight=0)
        self.cadastro_frame.grid_rowconfigure(4, weight=0)
        self.cadastro_frame.grid_rowconfigure(5, weight=1)
        self.cadastro_frame.grid_columnconfigure(0, weight=0)
        self.cadastro_frame.grid_columnconfigure(1, weight=0)
        self.cadastro_frame.grid_columnconfigure(2, weight=1)
        self.cadastro_frame.grid_columnconfigure(3, weight=0)
        self.cadastro_frame.grid(row=1, column=0, pady=(20, 0), sticky="ew")

        ctk.CTkLabel(self.cadastro_frame, text="Código:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_codigo = ctk.CTkEntry(self.cadastro_frame, font=FONTE_TEXTO, width=120, height=30, corner_radius=2)
        self.entry_codigo.grid(row=0, column=1, padx=(10, 0), pady=(5, 0), sticky="w")

        ctk.CTkLabel(self.cadastro_frame, text="Nome Completo:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_nome_completo = ctk.CTkEntry(self.cadastro_frame, font=FONTE_TEXTO, width=350, height=30, corner_radius=2)
        self.entry_nome_completo.grid(row=1, column=1, padx=(10, 0), pady=(5, 0), sticky="w")

        ctk.CTkLabel(self.cadastro_frame, text="CPF:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=2, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_cpf = ctk.CTkEntry(self.cadastro_frame, font=FONTE_TEXTO, width=120, height=30, corner_radius=2)
        self.entry_cpf.grid(row=2, column=1, padx=(10, 0), pady=(5, 0), sticky="w")

        ctk.CTkLabel(self.cadastro_frame, text="RG:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=3, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_rg = ctk.CTkEntry(self.cadastro_frame, font=FONTE_TEXTO, width=120, height=30, corner_radius=2)
        self.entry_rg.grid(row=3, column=1, padx=(10, 0), pady=(5, 0), sticky="w")

            
        ctk.CTkLabel(self.cadastro_frame, text="Função:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=4, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_funcao = ctk.CTkComboBox(self.cadastro_frame, font=FONTE_TEXTO, values=["Motorista", "Ajudante"], width=120, height=30, corner_radius=2)
        self.entry_funcao.set("")
        self.entry_funcao.grid(row=4, column=1, padx=(10, 0), pady=(5, 0), sticky="w")


        ctk.CTkFrame(self.cadastro_frame, height=2, fg_color=COR_LINHAS).grid(row=5, column=0, padx=(40, 290), pady=(25, 0), sticky="ew", columnspan=4)


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
            pady=(0, 0)
        )

        self.botao_confirmar = ctk.CTkButton(
            self.footer_frame,
            text="Cadastrar",
            font=FONTE_BOTAO_PRINCIPAL,
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
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
        )
        self.botao_cancelar.grid(row=0, column=3, padx=(10, 0), pady=(25, 0))
