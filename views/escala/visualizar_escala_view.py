import customtkinter as ctk
from PIL import Image

from constants.paths import ICONS_DIR

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_TEXTO,
    FONTE_PEQUENA,
    FONTE_BOTAO_PRINCIPAL,
    FONTE_BOTAO_SECUNDARIO,
)

from constants.cores import COR_FUNDO_CONTAINER_CARGAS, COR_LINHAS

from constants.cores import COR_BOTAO, HOVER_BOTAO, COR_TEXTO, COR_TEXTO_BOTAO

class VisualizarEscalaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="VISUALIZAR ESCALA").grid(row=0, column=0, padx=(50, 0), pady=(50, 0))
