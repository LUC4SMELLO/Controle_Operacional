import customtkinter as ctk

from constants.textos import FONTE_SUBTITULO, FONTE_LABEL, FONTE_TEXTO, FONTE_BOTAO_SECUNDARIO
from constants.cores import COR_TEXTO, COR_TEXTO_BOTAO, COR_BOTAO, HOVER_BOTAO



class TelaImprimir(ctk.CTkToplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Imprimir")
        self.geometry("500x315")
        self.resizable(False, False)
        self.grab_set()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")


        # ##############
        #   IMPRESSORA
        # ##############

        self.toolbar_1_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_1_frame.grid_rowconfigure(0, weight=1)
        self.toolbar_1_frame.grid_columnconfigure(0, weight=1)
        self.toolbar_1_frame.grid(row=1, column=0, sticky="ew")

        self.impressora_frame = ctk.CTkFrame(self.toolbar_1_frame, fg_color="transparent")
        self.impressora_frame.grid_columnconfigure(0, weight=1)
        self.impressora_frame.grid(row=0, column=0, sticky="ew", columnspan=2)

        self.impressora_header_frame = ctk.CTkFrame(self.impressora_frame, fg_color="transparent")
        self.impressora_header_frame.grid_rowconfigure(0, weight=1)
        self.impressora_header_frame.grid_columnconfigure(0, weight=1)
        self.impressora_header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.impressora_header_frame, text="Impressora", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

        self.impressora_toolbar_frame = ctk.CTkFrame(self.impressora_frame, fg_color="transparent")
        self.impressora_toolbar_frame.grid_rowconfigure(0, weight=1)
        self.impressora_toolbar_frame.grid_columnconfigure(0, weight=0)
        self.impressora_toolbar_frame.grid_columnconfigure(1, weight=1)
        self.impressora_toolbar_frame.grid_columnconfigure(2, weight=1)
        self.impressora_toolbar_frame.grid(row=1, column=0, sticky="ew")

        ctk.CTkLabel(self.impressora_toolbar_frame, text="Nome:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        entry_impressora = ctk.CTkComboBox(self.impressora_toolbar_frame, font=FONTE_TEXTO, values=["Impresora 1", "Impressora 2"], height=30, corner_radius=2)
        entry_impressora.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="ew", columnspan=2)


        # #####################
        #   INTERVALO PÁGINAS
        # #####################

        self.toolbar_2_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_2_frame.grid_rowconfigure(0, weight=1)
        self.toolbar_2_frame.grid_columnconfigure(0, weight=1)
        self.toolbar_2_frame.grid_columnconfigure(1, weight=1)
        self.toolbar_2_frame.grid(row=2, column=0, pady=(10, 0), sticky="ew")

        self.intervalo_frame = ctk.CTkFrame(self.toolbar_2_frame, fg_color="transparent")
        self.intervalo_frame.grid(row=0, column=0, sticky="nsew")

        self.intervalo_header_frame = ctk.CTkFrame(self.intervalo_frame, fg_color="transparent")
        self.intervalo_header_frame.grid_columnconfigure(0, weight=1)
        self.intervalo_header_frame.grid_columnconfigure(1, weight=0)
        self.intervalo_header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.intervalo_header_frame, text="Intervalo Páginas", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

        self.intervalo_toolbar_frame = ctk.CTkFrame(self.intervalo_frame, fg_color="transparent")
        self.intervalo_toolbar_frame.grid(row=1, column=0)

        ctk.CTkLabel(self.intervalo_toolbar_frame, text="Páginas:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        entry_paginas = ctk.CTkEntry(self.intervalo_toolbar_frame, font=FONTE_TEXTO, width=150, height=30)
        entry_paginas.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="we")


        # #####################
        #        CÓPIAS
        # #####################

        self.copia_frame = ctk.CTkFrame(self.toolbar_2_frame, fg_color="transparent")
        self.copia_frame.grid(row=0, column=1, sticky="nsew")

        self.copia_header_frame = ctk.CTkFrame(self.copia_frame, fg_color="transparent")
        self.copia_header_frame.grid_columnconfigure(0, weight=1)
        self.copia_header_frame.grid_columnconfigure(1, weight=0)
        self.copia_header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.copia_header_frame, text="Cópias", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

        self.copia_toolbar_frame = ctk.CTkFrame(self.copia_frame, fg_color="transparent")
        self.copia_toolbar_frame.grid(row=1, column=0)

        ctk.CTkLabel(self.copia_toolbar_frame, text="Número de Cópias:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        entry_copias = ctk.CTkEntry(self.copia_toolbar_frame, font=FONTE_TEXTO, width=70, height=30)
        entry_copias.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))


        # #####################
        #        DUPLEX
        # #####################

        self.toolbar_3_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_3_frame.grid_rowconfigure(0, weight=1)
        self.toolbar_3_frame.grid_columnconfigure(0, weight=1)
        self.toolbar_3_frame.grid_columnconfigure(1, weight=1)
        self.toolbar_3_frame.grid(row=3, column=0, pady=(10, 0), sticky="ew")

        self.duplex_frame = ctk.CTkFrame(self.toolbar_3_frame, fg_color="transparent")
        self.duplex_frame.grid(row=0, column=0, sticky="nsew")

        self.duplex_header_frame = ctk.CTkFrame(self.duplex_frame, fg_color="transparent")
        self.duplex_header_frame.grid_columnconfigure(0, weight=1)
        self.duplex_header_frame.grid_columnconfigure(1, weight=0)
        self.duplex_header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.duplex_header_frame, text="Duplex", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

        self.duplex_toolbar_frame = ctk.CTkFrame(self.duplex_frame, fg_color="transparent")
        self.duplex_toolbar_frame.grid(row=1, column=0)

        ctk.CTkLabel(self.duplex_toolbar_frame, text="Frente e Verso:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        check_duplex = ctk.CTkCheckBox(self.duplex_toolbar_frame, font=FONTE_TEXTO, text="", checkbox_width=30, checkbox_height=30)
        check_duplex.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))
        
        self.toolbar_4_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_4_frame.grid_rowconfigure(0, weight=1)
        self.toolbar_4_frame.grid_columnconfigure(0, weight=1)
        self.toolbar_4_frame.grid_columnconfigure(1, weight=1)
        self.toolbar_4_frame.grid(row=4, column=0, pady=(10, 0), sticky="ew")

        self.botoes_frame = ctk.CTkFrame(self.toolbar_4_frame, fg_color="transparent")
        self.botoes_frame.grid(row=0, column=0, sticky="nsew")
        
        self.botao_confirmar = ctk.CTkButton(self.botoes_frame, text="Confirmar", font=FONTE_BOTAO_SECUNDARIO, text_color=COR_TEXTO_BOTAO, fg_color=COR_BOTAO, hover_color=HOVER_BOTAO).grid(row=0, column=0, padx=(10, 0), pady=(10, 10))
        
        self.botao_cancelar = ctk.CTkButton(self.botoes_frame, text="Cancelar", font=FONTE_BOTAO_SECUNDARIO, text_color=COR_TEXTO_BOTAO, fg_color=COR_BOTAO, hover_color=HOVER_BOTAO).grid(row=0, column=1, padx=(10, 0), pady=(10, 10))
