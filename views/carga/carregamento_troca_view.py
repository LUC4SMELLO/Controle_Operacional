import customtkinter as ctk
from tkinter import ttk

from PIL import Image

from constants.paths import ICONS_DIR

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


class CarregamentoTrocaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.entradas_carga = []
        self.linhas_pendencia = []

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

        self.pendencias_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.pendencias_frame.grid_columnconfigure(0, weight=1)
        self.pendencias_frame.grid(row=1, column=0, sticky="nsew")

        self.pendencias_header = ctk.CTkFrame(self.pendencias_frame, fg_color="transparent")
        self.pendencias_header.grid(row=0, column=0, padx=(40, 290), sticky="ew")

        self.pendencias_header.grid_columnconfigure(0, minsize=100) # Cupom
        self.pendencias_header.grid_columnconfigure(1, minsize=20)
        self.pendencias_header.grid_columnconfigure(2, minsize=100) # Código Cliente
        self.pendencias_header.grid_columnconfigure(3, minsize=250) # Razão Social (Maior)
        self.pendencias_header.grid_columnconfigure(4, minsize=20)
        self.pendencias_header.grid_columnconfigure(5, minsize=120) # Código Produto
        self.pendencias_header.grid_columnconfigure(6, minsize=100) # Quantidade
        self.pendencias_header.grid_columnconfigure(7, minsize=100) # Carga

        ctk.CTkLabel(self.pendencias_header, text="Cupom", font=FONTE_LABEL, text_color=COR_TEXTO, anchor="w").grid(row=0, column=0, padx=(25, 0), pady=(25, 0), sticky="ew")
        ctk.CTkLabel(self.pendencias_header, text="Código Cliente", font=FONTE_LABEL, text_color=COR_TEXTO, anchor="w").grid(row=0, column=2, padx=(10, 0), pady=(25, 0), sticky="ew")
        ctk.CTkLabel(self.pendencias_header, text="Razão Social", font=FONTE_LABEL, text_color=COR_TEXTO, anchor="w").grid(row=0, column=3, padx=(75, 0), pady=(25, 0), sticky="ew")
        ctk.CTkLabel(self.pendencias_header, text="Código Produto", font=FONTE_LABEL, text_color=COR_TEXTO, anchor="w").grid(row=0, column=5, padx=(20, 0), pady=(25, 0), sticky="ew")
        ctk.CTkLabel(self.pendencias_header, text="Quantidade", font=FONTE_LABEL, text_color=COR_TEXTO, anchor="w").grid(row=0, column=6, padx=(30, 0), pady=(25, 0), sticky="ew")
        ctk.CTkLabel(self.pendencias_header, text="Carga", font=FONTE_LABEL, text_color=COR_TEXTO, anchor="w").grid(row=0, column=7, padx=(30, 0), pady=(25, 0), sticky="ew")

        self.pendencias_scroll = ctk.CTkScrollableFrame(
            self.pendencias_frame,
            fg_color=COR_FUNDO_CONTAINER_CARGAS,
            height=320
        )
        self.pendencias_scroll._scrollbar.grid_remove()

        self.pendencias_scroll.grid_columnconfigure(0, weight=0)
        self.pendencias_scroll.grid_columnconfigure(1, weight=1)
        self.pendencias_scroll.grid_rowconfigure(0, weight=1)
        self.pendencias_scroll.grid(row=1, column=0, padx=(40, 290), sticky="nsew")

        ctk.CTkFrame(self.pendencias_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(30, 0), sticky="ew", columnspan=1)

        self.after(500, self.buscar_pendencias)


    def exibir_pendencias(self, pendencias):

        linha_grid = 1
        for pendencia in pendencias:

            self.frame_pendencia = ctk.CTkFrame(self.pendencias_scroll, fg_color=COR_FUNDO_FRAME_CARGAS, height=45, border_width=0, corner_radius=0)
            # CONFIGURAÇÃO DE LARGURA IDÊNTICA AO HEADER
            self.frame_pendencia.grid_columnconfigure(0, minsize=100)
            self.frame_pendencia.grid_columnconfigure(1, minsize=20)
            self.frame_pendencia.grid_columnconfigure(2, minsize=100)
            self.frame_pendencia.grid_columnconfigure(3, minsize=300) # Espaço fixo para o nome
            self.frame_pendencia.grid_columnconfigure(4, minsize=20)
            self.frame_pendencia.grid_columnconfigure(5, minsize=120)
            self.frame_pendencia.grid_columnconfigure(6, minsize=100)
            self.frame_pendencia.grid_columnconfigure(7, minsize=100)

            self.frame_pendencia.grid(row=linha_grid, column=0, pady=(7, 0), sticky="we", columnspan=2)

            self.frame_pendencia.label_cupom = ctk.CTkLabel(self.frame_pendencia, text=pendencia["cupom"], font=("Segoe UI", 17), text_color=COR_TEXTO)
            self.frame_pendencia.label_cupom.grid(row=0, column=0, padx=(10, 0), pady=(0, 0), sticky="ew")

            self.frame_pendencia.label_codigo_cliente = ctk.CTkLabel(self.frame_pendencia, text=pendencia["codigo_cliente"], font=("Segoe UI", 17), text_color=COR_TEXTO)
            self.frame_pendencia.label_codigo_cliente.grid(row=0, column=2, padx=(10, 0), pady=(0, 0), sticky="ew")


            razao = pendencia["razao_social"]
            try:
                if len(razao) > 30:
                    razao = razao[:27] + "..."
            except Exception:
                razao = ""
            
            label_razao_social = ctk.CTkLabel(self.frame_pendencia, text=razao, font=FONTE_TEXTO, text_color=COR_TEXTO)
            label_razao_social.grid(row=0, column=3, padx=(10, 0), pady=(0, 0), sticky="ew")

            label_codigo_produto = ctk.CTkLabel(self.frame_pendencia, text=pendencia["codigo_produto"], font=FONTE_TEXTO, text_color=COR_TEXTO)
            label_codigo_produto.grid(row=0, column=5, padx=(10, 0), pady=(0, 0), sticky="ew")

            label_quantidade = ctk.CTkLabel(self.frame_pendencia, text=pendencia["quantidade"], font=FONTE_TEXTO, text_color=COR_TEXTO)
            label_quantidade.grid(row=0, column=6, padx=(40, 0), pady=(0, 0), sticky="ew")

            entry_carga = ctk.CTkEntry(self.frame_pendencia, font=FONTE_TEXTO, text_color=COR_TEXTO, width=80, height=25)
            entry_carga.grid(row=0, column=7, padx=(45, 0), pady=(0, 0), sticky="ew")

            self.entradas_carga.append(entry_carga)
            entry_carga.bind("<Return>", lambda event, linha=self.frame_pendencia, entry=entry_carga: self.controller.binds._on_enter(linha, entry))

            self.linhas_pendencia.append(self.frame_pendencia)

            linha_grid += 1


    def buscar_pendencias(self):
        resultado = self.controller.buscar_pendencias()
        if resultado:
            self.controller.limpar_pendencias()
            self.exibir_pendencias(resultado)
        else:
            exibir_mensagem("Aviso", "Pendências não encontradas.", "warning")
            return
