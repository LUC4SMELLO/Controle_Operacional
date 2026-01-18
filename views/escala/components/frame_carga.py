import customtkinter as ctk
from constants.textos import FONTE_TEXTO, FONTE_LABEL
from constants.cores import COR_TEXTO
from constants.rotas import ROTAS


class FrameCarga(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=85, border_width=2, border_color="#4a4d50")


        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=2)
        self.grid_columnconfigure(5, weight=1)


        # Número Carga
        self.label_numero_carga = ctk.CTkLabel(self, text="7191001", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_numero_carga.grid(row=2, column=1, padx=10)


        # Códigos
        self.entry_cod_motorista = ctk.CTkEntry(self, width=50)
        self.entry_cod_motorista.grid(row=1, column=2, padx=10, pady=3)

        self.entry_cod_ajudante_1 = ctk.CTkEntry(self, width=50)
        self.entry_cod_ajudante_1.grid(row=2, column=2)

        self.entry_cod_ajudante_2 = ctk.CTkEntry(self, width=50)
        self.entry_cod_ajudante_2.grid(row=3, column=2, pady=3)

        # Nomes
        self.label_nome_motorista = ctk.CTkLabel(self, text="Motorista")
        self.label_nome_motorista.grid(row=1, column=3, sticky="w", padx=2, pady=2)

        self.label_nome_ajudante_1 = ctk.CTkLabel(self, text="Ajudante 1")
        self.label_nome_ajudante_1.grid(row=2, column=3, sticky="w", padx=2, pady=1)

        self.label_nome_ajdudante_2 = ctk.CTkLabel(self, text="Ajudante 2")
        self.label_nome_ajdudante_2.grid(row=3, column=3, sticky="w", padx=2, pady=2)

        # Rota
        nome_rotas = [r[1] for r in ROTAS.values()]
        self.entry_rota = ctk.CTkComboBox(self, values=nome_rotas, width=250)
        self.entry_rota.grid(row=2, column=4, padx=(40, 0))

        # Observação
        self.entry_observacao = ctk.CTkEntry(self, width=280)
        self.entry_observacao.grid(row=2, column=5, sticky="w")
