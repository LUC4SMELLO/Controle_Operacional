import tkinter as ttk
import customtkinter as ctk
from PIL import Image
from tkcalendar import DateEntry

from constants.paths import ICONS_DIR, REPORTS_IMAGES_DIR

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_TEXTO,
    FONTE_PEQUENA,
    FONTE_BOTAO_PRINCIPAL,
    FONTE_BOTAO_SECUNDARIO,
)

from constants.cores import COR_LINHAS

from constants.cores import COR_BOTAO, HOVER_BOTAO, COR_TEXTO, COR_TEXTO_BOTAO


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

from views.dialogs.exibir_mensagem import exibir_mensagem


class VisualizarEscalaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        controller.set_view(self)

        self.imagens_originais = []
        self.imagens_tk = []
        self.zoom = 1.0

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0) # HEADER
        self.main_frame.grid_rowconfigure(1, weight=0) # TOOLBAR 1
        self.main_frame.grid_rowconfigure(2, weight=0) # TOOLBAR 2
        self.main_frame.grid_rowconfigure(3, weight=0) # CABEÇALHO CARGAS
        self.main_frame.grid_rowconfigure(4, weight=1) # CONTAINER CARGAS
        self.main_frame.grid_rowconfigure(5, weight=0) # FOOTER
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

        ctk.CTkLabel(self.header_frame, text="Escala", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="w")

        ctk.CTkLabel(self.header_frame, text="Visualizar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).grid(row=1, column=0, padx=(40, 0), pady=(20, 0), sticky="w")

        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=2)


        self.toolbar_frame_1 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_frame_1.grid_rowconfigure(0, weight=0)
        self.toolbar_frame_1.grid_rowconfigure(1, weight=0)
        self.toolbar_frame_1.grid_rowconfigure(2, weight=1)
        self.toolbar_frame_1.grid_columnconfigure(0, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(1, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(2, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(3, weight=0)
        self.toolbar_frame_1.grid_columnconfigure(4, weight=1)
        self.toolbar_frame_1.grid(
            row=1,
            column=0,
            sticky="ew"
        )

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
        

        self.botao_buscar_escala = ctk.CTkButton(
            self.toolbar_frame_1,
            text="Buscar",
            command=self.buscar_escala,
            width=50,
            height=30,
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            )
        self.botao_buscar_escala.grid(row=0, column=2, padx=(10, 0), pady=(15, 0), sticky="w")

        icone_menos_zoom = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "menos_zoom_dark.png"),
            dark_image=Image.open(ICONS_DIR / "menos_zoom_dark.png"),
            size=(23, 23)
        )
        self.botao_zoom_out = ctk.CTkButton(
            self.toolbar_frame_1,
            image=icone_menos_zoom,
            text="",
            command=lambda: self.controller.zoom_out(),
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_zoom_out.grid(row=0, column=3, padx=(10, 0), pady=(15, 0), sticky="w")

        icone_mais_zoom = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "mais_zoom_dark.png"),
            dark_image=Image.open(ICONS_DIR / "mais_zoom_dark.png"),
            size=(23, 23)
        )
        self.botao_zoom_in = ctk.CTkButton(
            self.toolbar_frame_1,
            image=icone_mais_zoom,
            text="",
            command=lambda: self.controller.zoom_in(),
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_zoom_in.grid(row=0, column=4, padx=(10, 0), pady=(15, 0), sticky="w")

        ctk.CTkFrame(self.toolbar_frame_1, height=2, fg_color=COR_LINHAS).grid(row=2, column=0, padx=(40, 290), pady=(15, 0), sticky="ew", columnspan=5)

        self.visualizar_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.visualizar_frame.grid_rowconfigure(0, weight=1)
        self.visualizar_frame.grid_columnconfigure(0, weight=0)
        self.visualizar_frame.grid_columnconfigure(1, weight=0)
        self.visualizar_frame.grid_columnconfigure(2, weight=1)
        self.visualizar_frame.grid(row=4, column=0, padx=(40, 290), sticky="nsew")



        self.canvas = ctk.CTkCanvas(
            self.visualizar_frame,
            bg="#FFFFFF",
            highlightthickness=0,
            bd=0
        )
        self.canvas.grid(row=0, column=0, pady=(30, 30), sticky="nsew", columnspan=3)

        scroll_x = ttk.Scrollbar(self.canvas, orient="horizontal", command=self.canvas.xview)
        scroll_y = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        self.canvas.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(-int(e.delta / 100), "units"))
        self.canvas.bind("<Shift-MouseWheel>", lambda e: self.canvas.xview_scroll(-int(e.delta / 2.5), "units"))
        self.canvas.bind("<Control-MouseWheel>", self.controller.zoom_mousewheel)

    

    def buscar_escala(self):

        self.controller.limpar_imagens_escala()

        resultado = self.controller.exibir_escala()

        exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])

        if not resultado["sucesso"]:
            return "break"
    
        self.canvas.delete("all")
        self.imagens_tk.clear()

        for nome in ["relatorio_entrega_1.png", "relatorio_entrega_2.png"]:
            caminho = REPORTS_IMAGES_DIR / nome
            if caminho.exists():
                self.imagens_originais.append(Image.open(caminho))

        self.zoom = 1.0

        self.controller.redesenhar_imagens()

        return "break"
