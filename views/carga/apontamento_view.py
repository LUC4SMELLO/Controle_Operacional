import customtkinter as ctk
from tkcalendar import DateEntry

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

from constants.cores import COR_LINHAS, COR_FUNDO_CONTAINER_CARGAS

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


class ApontamentoView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.linhas = {}

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

        ctk.CTkLabel(self.header_frame, text="Carga", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Apontamentos", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")


        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=1)


        self.toolbar_frame_1 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_frame_1.grid_rowconfigure(0, weight=0)
        self.toolbar_frame_1.grid_rowconfigure(1, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(0, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(1, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(2, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(3, weight=0)
        self.toolbar_frame_1.grid(row=1, column=0, sticky="ew")

        ctk.CTkLabel(self.toolbar_frame_1, text="Data:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="e")

        self.entry_data = DateEntry(
            self.toolbar_frame_1,
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
        self.entry_data.grid(row=0, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

        self.botao_buscar_carga = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Buscar",
            command=self.buscar_carga,
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            )
        self.botao_buscar_carga.grid(row=0, column=2, padx=(10, 0), pady=(15, 0), sticky="w")


        ctk.CTkFrame(self.toolbar_frame_1, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=4)


        self.cargas_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.cargas_frame.grid_columnconfigure(0, weight=1)
        self.cargas_frame.grid(row=2, column=0, sticky="nsew")

        self.cargas_header = ctk.CTkFrame(self.cargas_frame, fg_color="transparent")
        self.cargas_header.grid(row=0, column=0, sticky="ew")

        self.cargas_header.grid_columnconfigure(0, minsize=120)
        self.cargas_header.grid_columnconfigure(1, minsize=20)
        self.cargas_header.grid_columnconfigure(2, minsize=120)
        self.cargas_header.grid_columnconfigure(3, minsize=120)
        self.cargas_header.grid_columnconfigure(4, minsize=120)
        self.cargas_header.grid_columnconfigure(5, minsize=120)

        ctk.CTkLabel(self.cargas_header, text="Carga", font=FONTE_LABEL).grid(row=0, column=0, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Hora Saída", font=FONTE_LABEL).grid(row=0, column=1, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Hora Chegada", font=FONTE_LABEL).grid(row=0, column=2, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="KM Inicial", font=FONTE_LABEL).grid(row=0, column=3, padx=(30, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="KM Final", font=FONTE_LABEL).grid(row=0, column=4, padx=(40, 0), pady=(25, 0))

        self.cargas_scroll = ctk.CTkScrollableFrame(
            self.cargas_frame,
            height=350
        )
        self.cargas_scroll.grid_columnconfigure(0, minsize=120)
        self.cargas_scroll.grid_columnconfigure(1, minsize=20)
        self.cargas_scroll.grid_columnconfigure(2, minsize=120)
        self.cargas_scroll.grid_columnconfigure(3, minsize=120)
        self.cargas_scroll.grid_columnconfigure(4, minsize=120)
        self.cargas_scroll.grid_columnconfigure(5, minsize=120)
        self.cargas_scroll.grid(row=1, column=0, sticky="nsew")

        self.cargas_frame.grid_rowconfigure(1, weight=1)

        self.footer_frame = ctk.CTkFrame(self.main_frame, height=100, fg_color="transparent")
        self.footer_frame.grid_rowconfigure(0, weight=0)
        self.footer_frame.grid_rowconfigure(1, weight=0)
        self.footer_frame.grid_columnconfigure(0, weight=0)
        self.footer_frame.grid_columnconfigure(1, weight=0)
        self.footer_frame.grid_columnconfigure(2, weight=1)
        self.footer_frame.grid(row=3, column=0, sticky="we")


        ctk.CTkFrame(self.footer_frame, height=2, fg_color=COR_LINHAS).grid(row=0, column=0, padx=(40, 290), pady=(10, 0), sticky="ew", columnspan=3)


        self.botao_confirmar = ctk.CTkButton(
            self.footer_frame,
            text="Confirmar",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color= COR_TEXTO_BOTAO,
        )
        self.botao_confirmar.grid(row=1, column=0, padx=(40, 0), pady=(20, 0))

        self.botao_cancelar= ctk.CTkButton(
            self.footer_frame,
            text="Cancelar",
            command=self.controller.limpar_cargas,
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
        )
        self.botao_cancelar.grid(row=1, column=1, padx=(40, 0), pady=(20, 0))


    def exibir_cargas(self, cargas):
        self.controller.limpar_cargas()

        linha_grid = 1
        for carga in cargas:

            label_carga = ctk.CTkLabel(self.cargas_scroll, text=carga["numero_carga"], font=("Segoe UI", 17), text_color=COR_TEXTO)
            label_carga.grid(row=linha_grid, column=0, padx=(25, 0), pady=(10, 0))

            entry_hora_saida = ctk.CTkEntry(self.cargas_scroll, font=FONTE_TEXTO, text_color=COR_TEXTO, width=50)
            entry_hora_saida.insert(0, carga["horario"])
            entry_hora_saida.grid(row=linha_grid, column=2, pady=(10, 0))

            entry_hora_chegada = ctk.CTkEntry(self.cargas_scroll, font=FONTE_TEXTO, text_color=COR_TEXTO, width=50)
            entry_hora_chegada.grid(row=linha_grid, column=3, padx=(30, 0), pady=(10, 0))

            entry_km_inicial = ctk.CTkEntry(self.cargas_scroll, font=FONTE_TEXTO, text_color=COR_TEXTO, width=70)
            entry_km_inicial.grid(row=linha_grid, column=4, padx=(55, 0), pady=(10, 0))

            entry_km_final = ctk.CTkEntry(self.cargas_scroll, font=FONTE_TEXTO, text_color=COR_TEXTO, width=70)
            entry_km_final.grid(row=linha_grid, column=5, padx=(55, 0), pady=(10, 0))

            # GUARDAR REFERÊNCIA
            self.linhas[carga["numero_carga"]] = {
                "hora_saida": entry_hora_saida,
                "hora_chegada": entry_hora_chegada,
                "km_inicial": entry_km_inicial,
                "km_final": entry_km_final
            }

            linha_grid += 1

    def buscar_carga(self):
        data = self.entry_data.get()

        self.controller.buscar_cargas(data)

    def salvar(self):
        for numero_carga, campos in self.linhas.items():
            km_inicial = campos["km_inicial"].get()
            hora_saida = campos["hora_saida"].get()

            if not km_inicial:
                continue

            self.controller.salvar_apontamento(
                numero_carga,
                km_inicial,
                hora_saida
            )
