import customtkinter as ctk

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_BOTAO_PRINCIPAL
from constants.textos import FONTE_BOTAO_SECUNDARIO

from constants.cores import COR_LINHAS, COR_FUNDO_MENU_LATERAL

from constants.cores import COR_BOTAO, HOVER_BOTAO, COR_TEXTO, COR_TEXTO_BOTAO


class MenuView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.controller.atualizar_todos_os_bancos_dados()

        # MENU
        self.menu_frame = ctk.CTkFrame(self, width=240, fg_color=COR_FUNDO_MENU_LATERAL, corner_radius=0)
        self.menu_frame.pack(side="left", fill="both")

        # HEADER
        self.header_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        self.header_frame.pack(side="top", fill="x")

        ctk.CTkLabel(
            self.header_frame, text="Menu", font=FONTE_TITULO, text_color=COR_TEXTO
        ).pack(side="left", padx=(15, 0), pady=(15, 0), anchor="w")

        self.switch_alternar_modo = ctk.CTkSwitch(
            self.header_frame,
            text="Tema",
            font=FONTE_SUBTITULO,
            text_color=COR_TEXTO,
            progress_color="#979DA2",
            command=self.controller.alternar_modo_aparencia,
        )
        self.switch_alternar_modo.pack(side="right", padx=(50, 12), pady=(20, 0))


        # ----------------------------
        #      BOTÕES PRINCIPAIS
        # ----------------------------


        self.botao_escala = self.criar_botao(
            master=self.menu_frame,
            text="Escala",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("escala"),
        )
        self.botao_escala.pack(side="top", padx=10, pady=(20, 1), anchor="w")

        self.botao_carga = self.criar_botao(
            master=self.menu_frame,
            text="Carga",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("carga"),
        )
        self.botao_carga.pack(side="top", padx=10, pady=1, anchor="w")

        self.botao_pendencia_troca = self.criar_botao(
            master=self.menu_frame,
            text="Pendência & Troca",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("pendencia"),
        )
        self.botao_pendencia_troca.pack(side="top", padx=10, pady=1, anchor="w")

        self.botao_relatorios = self.criar_botao(
            master=self.menu_frame,
            text="Relatórios",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("relatorios"),
        )
        self.botao_relatorios.pack(side="top", padx=10, pady=1, anchor="w")

        self.botao_funcionarios = self.criar_botao(
            master=self.menu_frame,
            text="Funcionários",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("funcionarios"),
        )
        self.botao_funcionarios.pack(side="top", padx=10, pady=1, anchor="w")

        self.botao_veiculos = self.criar_botao(
            master=self.menu_frame,
            text="Veículos",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("veiculos"),
        )
        self.botao_veiculos.pack(side="top", padx=10, pady=1, anchor="w")


        # ----------------------------
        #           SUBMENUS
        # ----------------------------


        self.submenus = {
            "escala": [
                ("Editar", self.controller.mostrar_tela_editar_escala),
                ("Visualizar", None),
            ],
            "carga": [
                ("Mapa de Troca", None),
                ("Carregamento Troca", None),
                ("Km Caminhões", None),
            ],
            "pendencia": [
                ("Cadastrar", self.controller.mostrar_tela_cadastrar_pendencia),
                ("Editar", self.controller.mostrar_tela_editar_pendencia),
                ("Excluir", self.controller.mostrar_tela_excluir_pendencia),
            ],
            "relatorios": [
                ("Pendência & Troca", self.controller.mostrar_tela_relatorio_pendencia)
            ],
            "funcionarios": [
                ("Cadastrar", self.controller.mostrar_tela_cadastrar_funcionario),
                ("Editar", self.controller.mostrar_tela_editar_funcionario),
                ("Excluir", self.controller.mostrar_tela_excluir_funcionario),
            ],
            "veiculos": [
                ("Cadastrar", self.controller.mostrar_tela_cadastrar_veiculo),
                ("Editar", self.controller.mostrar_tela_editar_veiculo),
                ("Excluir", self.controller.mostrar_tela_excluir_veiculo),
            ],
        }

    def mostrar_submenu(self, nome):
        self.controller.definir_tela_atual(None)

        # SE O FRAME JÁ EXISTE, DESTRUÍ-LO PARA FECHAR/LIMPAR
        if hasattr(self, "submenu_frame"):
            # SE CLICOU NO MESMO BOTÃO QUE JÁ ESTÁ ABERTO, FECHA E RETORNA
            if self.submenu_frame.master_button == nome:
                self.submenu_frame.destroy()
                del self.submenu_frame
                return
            self.submenu_frame.destroy()

        self.submenu_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        self.submenu_frame.master_button = nome # MARCA DE QUEM É ESSE SUBMENU

        # MAPEAR QUAL BOTÃO FOI CLICADO PARA INSERIR O FRAME ABAIXO DELE
        botoes = {
            "escala": self.botao_escala,
            "carga": self.botao_carga,
            "pendencia": self.botao_pendencia_troca,
            "relatorios": self.botao_relatorios,
            "funcionarios": self.botao_funcionarios,
            "veiculos": self.botao_veiculos,
        }

        alvo = botoes[nome]

        # RENDERIZAR OS SUB-BOTÕES
        for texto, comando in self.submenus[nome]:
            botao = self.criar_botao(
                master=self.submenu_frame,
                text=texto,
                font=FONTE_BOTAO_SECUNDARIO,
                width=140,
                command=comando,
            )
            botao.pack(padx=(40, 10), pady=1, anchor="w")

        # INSERE O FRAME LOGO APÓS O BOTÃO CORRESPONDENTE
        self.submenu_frame.pack(after=alvo, fill="x", pady=(0, 5))

    def criar_botao(self, master, **kwargs):
        return ctk.CTkButton(
            master,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
            **kwargs
        )
