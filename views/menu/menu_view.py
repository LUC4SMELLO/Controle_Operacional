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

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # MENU
        self.menu_frame = ctk.CTkFrame(self, fg_color=COR_FUNDO_MENU_LATERAL, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        # HEADER
        self.header_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="we")

        ctk.CTkLabel(
            self.header_frame, text="Menu", font=FONTE_TITULO, text_color=COR_TEXTO
        ).grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        self.switch_alternar_modo = ctk.CTkSwitch(
            self.header_frame,
            text="Tema",
            font=FONTE_SUBTITULO,
            text_color=COR_TEXTO,
            button_color=("#000000", "#FFFFFF",),
            progress_color="#979DA2",
            command=self.controller.alternar_modo_aparencia,
        )
        self.switch_alternar_modo.grid(row=0, column=2, padx=(82, 5), pady=(10, 0))


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
        self.botao_escala.grid(row=1, column=0, padx=(10, 0), pady=(20, 0), sticky="w")

        self.botao_carga = self.criar_botao(
            master=self.menu_frame,
            text="Carga",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("carga"),
        )
        self.botao_carga.grid(row=2, column=0, padx=(10, 0), pady=(2, 0), sticky="w")

        self.botao_pendencia_troca = self.criar_botao(
            master=self.menu_frame,
            text="Pendência & Troca",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("pendencia"),
        )
        self.botao_pendencia_troca.grid(row=3, column=0, padx=(10, 0), pady=(2, 0), sticky="w")

        self.botao_relatorios = self.criar_botao(
            master=self.menu_frame,
            text="Relatórios",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("relatorios"),
        )
        self.botao_relatorios.grid(row=4, column=0, padx=(10, 0), pady=(2, 0), sticky="w")

        self.botao_funcionarios = self.criar_botao(
            master=self.menu_frame,
            text="Funcionários",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("funcionarios"),
        )
        self.botao_funcionarios.grid(row=5, column=0, padx=(10, 0), pady=(2, 0), sticky="w")

        self.botao_veiculos = self.criar_botao(
            master=self.menu_frame,
            text="Veículos",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=lambda: self.mostrar_submenu("veiculos"),
        )
        self.botao_veiculos.grid(row=6, column=0, padx=(10, 0), pady=(2, 0), sticky="w")


        # ----------------------------
        #           SUBMENUS
        # ----------------------------


        self.submenus = {
            "escala": [
                ("Editar", self.controller.mostrar_tela_editar_escala),
                ("Visualizar", self.controller.mostrar_tela_visualizar_escala),
            ],
            "carga": [
                ("Mapa de Troca", self.controller.mostrar_tela_mapa_troca),
                ("Carregamento Troca", self.controller.mostrar_tela_carregamento_troca),
                ("Apontamentos", self.controller.mostrar_tela_apontamento),
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

        # 1. PEGA A POSIÇÃO ATUAL DO BOTÃO ALVO NO GRID
        alvo_info = alvo.grid_info()
        linha_alvo = alvo_info["row"]
        coluna_alvo = alvo_info["column"]

        # 2. EMPURRA OS BOTÕES ABAIXO PARA DAR ESPAÇO AO SUBMENU
        # PERCORRE TODOS OS WIDGETS DENTRO DO menu_frame
        for widget in self.menu_frame.winfo_children():
            widget_info = widget.grid_info()
            # SE O WIDGET ESTIVER ABAIXO DO BOTÃO CLICADO, MOVE +1 LINHA PARA BAIXO
            if widget_info and widget_info["row"] > linha_alvo:
                widget.grid(row=widget_info["row"] + 1)

        # 3. RENDERIZAR OS SUB-BOTÕES INTERNOS
        for i, (texto, comando) in enumerate(self.submenus[nome]):
            botao = self.criar_botao(
                master=self.submenu_frame,
                text=texto,
                font=FONTE_BOTAO_SECUNDARIO,
                width=140,
                command=comando,
            )
            # ORGANIZA OS SUB-BOTÕES VERTICALMENTE DENTRO DO submenu_frame
            botao.grid(row=i, column=0, padx=(40, 10), pady=1, sticky="w")

        # 4. INSERE O FRAME LOGO ABAIXO DO BOTÃO CORRESPONDENTE
        self.submenu_frame.grid(row=linha_alvo + 1, column=coluna_alvo, pady=(0, 5), sticky="ew")


    def criar_botao(self, master, **kwargs):
        return ctk.CTkButton(
            master,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
            **kwargs
        )
