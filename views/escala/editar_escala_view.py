import customtkinter as ctk
from PIL import Image

from views.dialogs.exibir_mensagem import exibir_mensagem

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


class EditarEscalaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        ctk.CTkLabel(self, text="Escala", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=40, y=15)

        ctk.CTkLabel(self, text="Editar", font=FONTE_SUBTITULO, text_color=COR_TEXTO).place(x=40, y=65)

        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=105)

        self.label_data = ctk.CTkLabel(self, text="15/01/2026", font=("Segoe UI", 14, "bold"), text_color=COR_TEXTO)
        self.label_data.place(x=915, y=120)

        self.botao_segunda_feira = ctk.CTkButton(
            self,
            text="Segunda",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_segunda_feira.place(x=40, y=120)

        self.botao_terca_feira = ctk.CTkButton(
            self,
            text="Terça",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_terca_feira.place(x=120, y=120)

        self.botao_quarta_feira = ctk.CTkButton(
            self,
            text="Quarta",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_quarta_feira.place(x=200, y=120)

        self.botao_quinta_feira = ctk.CTkButton(
            self,
            text="Quinta",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=70,
            height=30,
        )
        self.botao_quinta_feira.place(x=280, y=120)

        ctk.CTkLabel(self, text="Número de Cargas:", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=40, y=165)
        self.entry_numero_cargas = ctk.CTkEntry(self, font=FONTE_TEXTO, width=30, height=30, corner_radius=2)
        self.entry_numero_cargas.place(x=200, y=165)

        self.botao_utilizar_cargas = ctk.CTkButton(
            self,
            text="Utilizar",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_utilizar_cargas.place(x=240, y=165)

        self.botao_salvar_escala = ctk.CTkButton(
            self,
            text="Salvar",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_salvar_escala.place(x=760, y=120)

        self.botao_limpar_escala = ctk.CTkButton(
            self,
            text="Limpar",
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO_BOTAO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            width=110,
            height=30
        )
        self.botao_limpar_escala.place(x=640, y=120)



        ctk.CTkFrame(self, width=950, height=2, fg_color=COR_LINHAS).place(x=40, y=210)



        ctk.CTkLabel(self, text="Carga", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=55, y=240)
        ctk.CTkLabel(self, text="Cód", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=125, y=240)
        ctk.CTkLabel(self, text="Nome", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=220, y=240)
        ctk.CTkLabel(self, text="Rota", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=460, y=240)
        ctk.CTkLabel(self, text="Observação", font=FONTE_LABEL, text_color=COR_TEXTO).place(x=665, y=240)


        self.frame_carga = ctk.CTkFrame(self, width=950, height=85, border_color="#4a4d50", border_width=2)
        self.frame_carga.place(x=40, y=270)



        self.label_carga = ctk.CTkLabel(self.frame_carga, text="7191601", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_carga.place(x=15, y=28)

        self.entry_codigo_motorista = ctk.CTkEntry(self.frame_carga, font=FONTE_TEXTO, text_color=COR_TEXTO, width=40, height=26, border_width=1, corner_radius=1)
        self.entry_codigo_motorista.place(x=80, y=4)

        self.entry_codigo_ajudante_1 = ctk.CTkEntry(self.frame_carga, font=FONTE_TEXTO, text_color=COR_TEXTO, width=40, height=26, border_width=1, corner_radius=1)
        self.entry_codigo_ajudante_1.place(x=80, y=29)

        self.entry_codigo_ajudante_2 = ctk.CTkEntry(self.frame_carga, font=FONTE_TEXTO, text_color=COR_TEXTO, width=40, height=26, border_width=1, corner_radius=1)
        self.entry_codigo_ajudante_2.place(x=80, y=54)


        self.label_nome_motorista = ctk.CTkLabel(self.frame_carga, text="Marcos Aparecido de Oliveira", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_nome_motorista.place(x=135, y=3)

        self.label_nome_ajudante_1 = ctk.CTkLabel(self.frame_carga, text="Wesley Michel do Nascimento", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_nome_ajudante_1.place(x=135, y=28)

        self.label_nome_ajudante_2 = ctk.CTkLabel(self.frame_carga, text="Tomas de Oliveira Rangel", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_nome_ajudante_2.place(x=135, y=53)


        ctk.CTkFrame(self.frame_carga, width=3, height=80, fg_color="#FFFFFF").place(x=325, y=2)


        self.label_rota = ctk.CTkLabel(self.frame_carga, text="EXTREMA (SEG) JD.EUROPA/P.ALTA", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_rota.place(x=335, y=30)

        icone_lupa = ctk.CTkImage(
            light_image=Image.open("assets/icons/lupa_dark.png"),
            dark_image=Image.open("assets/icons/lupa_dark.png"),
            size=(20, 20)
        )
        self.botao_pesquisar_rota = ctk.CTkButton(
            self.frame_carga,
            image=icone_lupa,
            text="",
            width=14,
            height=14,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_pesquisar_rota.place(x=560, y=30)


        ctk.CTkFrame(self.frame_carga, width=3, height=80, fg_color="#FFFFFF").place(x=605, y=2)


        self.label_observacao = ctk.CTkLabel(self.frame_carga, text="Rota", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_observacao.place(x=655, y=30)


        ctk.CTkFrame(self.frame_carga, width=3, height=80, fg_color="#FFFFFF").place(x=730, y=2)

        ctk.CTkFrame(self.frame_carga, width=216, height=3, fg_color="#FFFFFF").place(x=732, y=30)

        self.label_horario_saida = ctk.CTkLabel(self.frame_carga, text="07:30", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_horario_saida.place(x=820, y=2)

        self.label_numero_caminhao = ctk.CTkLabel(self.frame_carga, text="Caminhão: 19", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_numero_caminhao.place(x=740, y=40)

        self.label_placa_caminhao = ctk.CTkLabel(self.frame_carga, text="Placa: TDS1D07", font=FONTE_TEXTO, text_color=COR_TEXTO)
        self.label_placa_caminhao.place(x=835, y=40)
