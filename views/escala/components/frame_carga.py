import customtkinter as ctk
from PIL import Image

from constants.paths import ICONS_DIR

from constants.textos import FONTE_TEXTO, FONTE_LABEL
from constants.cores import COR_TEXTO, COR_BOTAO, HOVER_BOTAO, COR_TEXTO_BOTAO, COR_FUNDO_FRAME_CARGAS
from constants.rotas import ROTAS


class FrameCarga(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, height=85, border_width=0, corner_radius=0, fg_color=COR_FUNDO_FRAME_CARGAS)

        self.controller = controller


        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0, minsize=60)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0, minsize=150)
        self.grid_columnconfigure(4, weight=2)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=0)

        # CÓDIGO DA CARGA
        self.label_cod_carga = ctk.CTkLabel(self, text="", width=20, font=("Segoe UI", 14, "bold"), text_color=COR_TEXTO_BOTAO)
        self.label_cod_carga.grid(row=1, column=0, padx=(2, 5), pady=(0, 5))

        # KM DO CAMINHÃO
        self.label_km_caminhao = ctk.CTkLabel(self, text="219.257", width=20, font=("Segoe UI", 14), text_color=COR_TEXTO_BOTAO)
        self.label_km_caminhao.grid(row=1, column=1)

        # NÚMERO DA CARGA
        self.label_numero_carga = ctk.CTkLabel(self, text="       ", font=FONTE_TEXTO, text_color=COR_TEXTO_BOTAO)
        self.label_numero_carga.grid(row=2, column=1, sticky="w")

        # HORÁRIO SAÍDA
        self.label_horario_saida = ctk.CTkLabel(self, text="", font=FONTE_TEXTO, text_color=COR_TEXTO_BOTAO)
        self.label_horario_saida.grid(row=3, column=1)


        # CÓDIGOS
        self.entry_cod_motorista = ctk.CTkEntry(self, font=FONTE_TEXTO, text_color=COR_TEXTO, width=50, border_width=0, corner_radius=0)
        self.entry_cod_motorista.grid(row=1, column=2, padx=10, pady=3)

        self.entry_cod_ajudante_1 = ctk.CTkEntry(self, font=FONTE_TEXTO, text_color=COR_TEXTO, width=50, border_width=0, corner_radius=0)
        self.entry_cod_ajudante_1.grid(row=2, column=2)

        self.entry_cod_ajudante_2 = ctk.CTkEntry(self, font=FONTE_TEXTO, text_color=COR_TEXTO, width=50, border_width=0, corner_radius=0)
        self.entry_cod_ajudante_2.grid(row=3, column=2, pady=3)

        # FLAGS DE CONTROLE
        self.entry_cod_motorista._enter_executado = False
        self.entry_cod_ajudante_1._enter_executado = False
        self.entry_cod_ajudante_2._enter_executado = False

        # NOMES
        self.label_nome_motorista = ctk.CTkLabel(self, text="", font=FONTE_TEXTO, text_color=COR_TEXTO_BOTAO, wraplength=158, width=160, anchor="w", justify="left")
        self.label_nome_motorista.grid(row=1, column=3, sticky="w", padx=(0, 5), pady=2)

        self.label_nome_ajudante_1 = ctk.CTkLabel(self, text="", font=FONTE_TEXTO, text_color=COR_TEXTO_BOTAO, wraplength=158, width=160, anchor="w", justify="left")
        self.label_nome_ajudante_1.grid(row=2, column=3, sticky="w", padx=(0, 5), pady=1)

        self.label_nome_ajudante_2 = ctk.CTkLabel(self, text="", font=FONTE_TEXTO, text_color=COR_TEXTO_BOTAO, wraplength=158,  width=160, anchor="w", justify="left")
        self.label_nome_ajudante_2.grid(row=3, column=3, sticky="w", padx=(0, 5), pady=2)

        # ROTA
        nome_rotas = [r[1] for r in ROTAS.values()]
        self.entry_rota = ctk.CTkComboBox(self, values=nome_rotas, font=FONTE_TEXTO, text_color=COR_TEXTO, width=250, border_width=0, corner_radius=0, command=lambda valor: self.controller.atualizar_horario_saida(valor, self))
        self.entry_rota.grid(row=2, column=4, padx=(40, 0))

        # OBSERVAÇÃO
        self.entry_observacao = ctk.CTkEntry(self, font=FONTE_TEXTO, text_color=COR_TEXTO, width=240, border_width=0, corner_radius=0)
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

        controller.scroll.recursive_bind_scroll(self)
