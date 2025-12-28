import customtkinter as ctk
from tkcalendar import DateEntry

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_TEXTO
from constants.textos import FONTE_PEQUENA
from constants.textos import FONTE_BOTAO_PRINCIPAL
from constants.textos import FONTE_BOTAO_SECUNDARIO

from constants.cores import COR_LINHAS

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


class TelaPendenciaTroca(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Pendência & Troca", font=FONTE_TITULO).place(x=15, y=15)

        ctk.CTkLabel(self, text="Data:", font=FONTE_SUBTITULO).place(x=125, y=60)

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
            date_pattern = 'dd/mm/yyyy'
            )
        self.entry_data.place(x=175, y=60)
        
        ctk.CTkLabel(self, text="Carga:", font=FONTE_SUBTITULO).place(x=117, y=95)
        self.entry_carga = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_carga.place(x=175, y=95)


        ctk.CTkLabel(self, text="Código Cliente:", font=FONTE_SUBTITULO).place(x=45, y=130)
        self.entry_codigo_cliente = ctk.CTkEntry(self, font=FONTE_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_codigo_cliente.place(x=175, y=130)


        ctk.CTkLabel(self, text="Tipo:", font=FONTE_SUBTITULO).place(x=128, y=165)
        self.entry_tipo = ctk.CTkComboBox(self, font=FONTE_TEXTO, values=["Pendência", "Troca"], corner_radius=2)
        self.entry_tipo.place(x=175, y=165)

        ctk.CTkLabel(self, text="Responsável:", font=FONTE_SUBTITULO).place(x=67, y=200)
        self.entry_responsavel = ctk.CTkEntry(self, font=FONTE_TEXTO, width=141, height=30, corner_radius=2)
        self.entry_responsavel.place(x=175, y=200)


        

