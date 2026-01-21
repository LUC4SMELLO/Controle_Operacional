import customtkinter as ctk
from PIL import Image

from constants.paths import ICONS_DIR

from constants.textos import FONTE_TEXTO, FONTE_LABEL
from constants.cores import COR_TEXTO, COR_BOTAO, HOVER_BOTAO
from constants.rotas import ROTAS


class FrameCarga(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, height=85, border_width=0, border_color="#4a4d50")

        self.controller = controller




        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=2)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=0)


        self.label_cod_carga = ctk.CTkLabel(self, text="", width=20, font=("Segoe UI", 14, "bold"))
        self.label_cod_carga.grid(row=1, column=0, padx=(2, 5), pady=(0, 5))

        # Número Carga
        self.label_numero_carga = ctk.CTkLabel(self, text="7191001", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_numero_carga.grid(row=2, column=1)


        # Códigos
        self.entry_cod_motorista = ctk.CTkEntry(self, width=50, border_width=0, corner_radius=0)
        self.entry_cod_motorista.grid(row=1, column=2, padx=10, pady=3)

        self.entry_cod_ajudante_1 = ctk.CTkEntry(self, width=50, border_width=0, corner_radius=0)
        self.entry_cod_ajudante_1.grid(row=2, column=2)

        self.entry_cod_ajudante_2 = ctk.CTkEntry(self, width=50, border_width=0, corner_radius=0)
        self.entry_cod_ajudante_2.grid(row=3, column=2, pady=3)

        # Nomes
        self.label_nome_motorista = ctk.CTkLabel(self, text="Motorista")
        self.label_nome_motorista.grid(row=1, column=3, sticky="w", padx=(0, 50), pady=2)

        self.label_nome_ajudante_1 = ctk.CTkLabel(self, text="Ajudante 1")
        self.label_nome_ajudante_1.grid(row=2, column=3, sticky="w", padx=(0, 50), pady=1)

        self.label_nome_ajdudante_2 = ctk.CTkLabel(self, text="Ajudante 2")
        self.label_nome_ajdudante_2.grid(row=3, column=3, sticky="w", padx=(0, 50), pady=2)

        # Rota
        nome_rotas = [r[1] for r in ROTAS.values()]
        self.entry_rota = ctk.CTkComboBox(self, values=nome_rotas, width=250, border_width=0, corner_radius=0)
        self.entry_rota.grid(row=2, column=4, padx=(40, 0))

        # Observação
        self.entry_observacao = ctk.CTkEntry(self, width=240, border_width=0, corner_radius=0)
        self.entry_observacao.grid(row=2, column=5, sticky="w")


        self.icone_lixeira = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "lixeira_dark.png"),
            dark_image=Image.open(ICONS_DIR / "lixeira_dark.png"),
            size=(20, 20)
        )

        self.botao_remover_carga = ctk.CTkButton(
            self,
            image=self.icone_lixeira,
            text="",
            command=lambda: controller.remover_carga_especifica(self),
            width=20,
            height=20,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_remover_carga.grid(row=2, column=6, padx=(0, 20))

        controller._recursive_bind_scroll(self)
