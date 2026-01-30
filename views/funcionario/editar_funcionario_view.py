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


class EditarFuncionarioView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="#bb90cb")
        self.main_frame.grid_rowconfigure(0, weight=0) # HEADER
        self.main_frame.grid_rowconfigure(1, weight=0) # EDIÇÃO
        self.main_frame.grid_rowconfigure(2, weight=0) # FOOTER
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="#498ccb")
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_rowconfigure(1, weight=1)
        self.header_frame.grid_rowconfigure(2, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.header_frame, text="Funcionários", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Editar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")


        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=1)


        self.edicao_frame = ctk.CTkFrame(self.main_frame, fg_color="#e2d151")
        self.edicao_frame.grid_rowconfigure(0, weight=0)
        self.edicao_frame.grid_rowconfigure(1, weight=0)
        self.edicao_frame.grid_rowconfigure(2, weight=0)
        self.edicao_frame.grid_rowconfigure(3, weight=0)
        self.edicao_frame.grid_rowconfigure(4, weight=0)
        self.edicao_frame.grid_rowconfigure(5, weight=0)
        self.edicao_frame.grid_rowconfigure(6, weight=1)
        self.edicao_frame.grid_columnconfigure(0, weight=0)
        self.edicao_frame.grid_columnconfigure(1, weight=0)
        self.edicao_frame.grid_columnconfigure(2, weight=0)
        self.edicao_frame.grid_columnconfigure(3, weight=1)
        self.edicao_frame.grid_columnconfigure(4, weight=0)
        self.edicao_frame.grid(row=1, column=0, pady=(20, 0), sticky="ew")


        ctk.CTkLabel(self.edicao_frame, text="Código:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_codigo = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=120, height=30, corner_radius=2)
        self.entry_codigo.grid(row=0, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

        self.botao_buscar_funcionario = ctk.CTkButton(
            self.edicao_frame,
            text="Buscar",
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            )
        self.botao_buscar_funcionario.grid(row=0, column=2, padx=(10, 0), pady=(15, 0), sticky="w")


        ctk.CTkFrame(self.edicao_frame, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=4)


        ctk.CTkLabel(self.edicao_frame, text="Nome Completo:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=2, column=0, padx=(40, 0), pady=(15, 0), sticky="e")
        self.entry_nome_completo = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=350, height=30, corner_radius=2)
        self.entry_nome_completo.grid(row=2, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.edicao_frame, text="CPF:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=3, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_cpf = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=120, height=30, corner_radius=2)
        self.entry_cpf.grid(row=3, column=1, padx=(10, 0), pady=(5, 0), sticky="w")

        ctk.CTkLabel(self.edicao_frame, text="RG:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=4, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_rg = ctk.CTkEntry(self.edicao_frame, font=FONTE_TEXTO, width=120, height=30, corner_radius=2)
        self.entry_rg.grid(row=4, column=1, padx=(10, 0), pady=(5, 0), sticky="w")

            
        ctk.CTkLabel(self.edicao_frame, text="Função:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=5, column=0, padx=(40, 0), pady=(5, 0), sticky="e")
        self.entry_funcao = ctk.CTkComboBox(self.edicao_frame, font=FONTE_TEXTO, values=["Motorista", "Ajudante"], width=120, height=30, corner_radius=2)
        self.entry_funcao.set("")
        self.entry_funcao.grid(row=5, column=1, padx=(10, 0), pady=(5, 0), sticky="w")


        ctk.CTkFrame(self.edicao_frame, height=2, fg_color=COR_LINHAS).grid(row=6, column=0, padx=(40, 290), pady=(25, 0), sticky="ew", columnspan=4)
