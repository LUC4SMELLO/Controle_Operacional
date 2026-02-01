import customtkinter as ctk

from constants.textos import FONTE_TITULO
from constants.textos import FONTE_SUBTITULO
from constants.textos import FONTE_BOTAO_PRINCIPAL
from constants.textos import FONTE_BOTAO_SECUNDARIO

from constants.cores import COR_LINHAS

from constants.cores import (COR_BOTAO, HOVER_BOTAO, COR_TEXTO, COR_TEXTO_BOTAO)


class MenuView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.controller.atualizar_todos_os_bancos_dados()


        ctk.CTkLabel(self, text="Menu", font=FONTE_TITULO, text_color=COR_TEXTO).place(x=15, y=15)

        ctk.CTkFrame(self, width=5, height=1280, fg_color=COR_LINHAS).place(
            x=250, relx=0, relheight=1
        )

        self.switch_alternar_modo = ctk.CTkSwitch(
            self,
            text="Tema",
            font=FONTE_SUBTITULO,
            text_color=COR_TEXTO,
            progress_color="#979DA2",
            command=self.controller.alternar_modo_aparencia,
        )
        self.switch_alternar_modo.place(x=120, y=20)

        # BOTÕES PRINCIPAIS

        self.botao_escala = ctk.CTkButton(
            self,
            text="Escala",
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            command=self.controller.mostrar_opcoes_escala,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_escala.place(x=10, y=100)

        self.botao_pendencia_troca = ctk.CTkButton(
            self,
            text="Pendência & Troca",
            font=FONTE_BOTAO_PRINCIPAL,
            command=self.controller.mostrar_opcoes_pendencia_troca,
            width=160,
            height=38,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_pendencia_troca.place(x=10, y=140)

        self.botao_relatorios = ctk.CTkButton(
            self,
            text="Relatórios",
            font=FONTE_BOTAO_PRINCIPAL,
            command=self.controller.mostrar_opcoes_relatorios,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_relatorios.place(x=10, y=180)

        self.botao_funcionarios = ctk.CTkButton(
            self,
            text="Funcionários",
            command=self.controller.mostrar_opcoes_funcionarios,
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_funcionarios.place(x=10, y=220)

        self.botao_veiculos = ctk.CTkButton(
            self,
            text="Veículos",
            command=self.controller.mostrar_opcoes_veiculos,
            font=FONTE_BOTAO_PRINCIPAL,
            width=160,
            height=38,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_veiculos.place(x=10, y=260)

        # BOTÕES SECUNDARIOS

        self.botao_editar_escala = ctk.CTkButton(
            self,
            text="Editar",
            command=self.controller.mostrar_tela_editar_escala,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_visualizar_escala = ctk.CTkButton(
            self,
            text="Visualizar",
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_cadastrar_pendencia_troca = ctk.CTkButton(
            self,
            text="Cadastrar",
            font=FONTE_BOTAO_SECUNDARIO,
            command=self.controller.mostrar_tela_cadastrar_pendencia,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )
        self.botao_editar_pendencia_troca = ctk.CTkButton(
            self,
            text="Editar",
            font=FONTE_BOTAO_SECUNDARIO,
            command=self.controller.mostrar_tela_editar_pendencia,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO,
        )
        self.botao_excluir_pendencia_troca = ctk.CTkButton(
            self,
            text="Excluir",
            command=self.controller.mostrar_tela_excluir_pendencia,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color= COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_relatorio_pendencia = ctk.CTkButton(
            self,
            text="Pendência & Troca",
            command=self.controller.mostrar_tela_relatorio_pendencia,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_cadastrar_funcionario = ctk.CTkButton(
            self,
            text="Cadastrar",
            command=self.controller.mostrar_tela_cadastrar_funcionario,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_editar_funcionario = ctk.CTkButton(
            self,
            text="Editar",
            command=self.controller.mostrar_tela_editar_funcionario,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_excluir_funcionario = ctk.CTkButton(
            self,
            text="Excluir",
            command=self.controller.mostrar_tela_excluir_funcionario,
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_cadastrar_veiculo = ctk.CTkButton(
            self,
            text="Cadastrar",
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_editar_veiculo = ctk.CTkButton(
            self,
            text="Editar",
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

        self.botao_excluir_veiculo = ctk.CTkButton(
            self,
            text="Excluir",
            font=FONTE_BOTAO_SECUNDARIO,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            text_color=COR_TEXTO_BOTAO
        )

    def mostrar_opcoes_escala(self):
        self.botao_escala.place(x=10, y=100)
        self.botao_pendencia_troca.place(x=10, y=210)
        self.botao_relatorios.place(x=10, y=250)
        self.botao_funcionarios.place(x=10, y=290)
        self.botao_veiculos.place(x=10, y=330)

        self.botao_cadastrar_pendencia_troca.place_forget()
        self.botao_editar_pendencia_troca.place_forget()
        self.botao_excluir_pendencia_troca.place_forget()

        self.botao_relatorio_pendencia.place_forget()

        self.botao_cadastrar_funcionario.place_forget()
        self.botao_editar_funcionario.place_forget()
        self.botao_excluir_funcionario.place_forget()

        self.botao_cadastrar_veiculo.place_forget()
        self.botao_editar_veiculo.place_forget()
        self.botao_excluir_veiculo.place_forget()

        self.botao_editar_escala.place(x=50, y=140)
        self.botao_visualizar_escala.place(x=50, y=170)

    def mostrar_opcoes_pendencia_troca(self):
        self.botao_escala.place(x=10, y=100)
        self.botao_pendencia_troca.place(x=10, y=140)
        self.botao_relatorios.place(x=10, y=280)
        self.botao_funcionarios.place(x=10, y=320)
        self.botao_veiculos.place(x=10, y=360)

        self.botao_editar_escala.place_forget()
        self.botao_visualizar_escala.place_forget()

        self.botao_relatorio_pendencia.place_forget()

        self.botao_cadastrar_funcionario.place_forget()
        self.botao_editar_funcionario.place_forget()
        self.botao_excluir_funcionario.place_forget()

        self.botao_cadastrar_veiculo.place_forget()
        self.botao_editar_veiculo.place_forget()
        self.botao_excluir_veiculo.place_forget()

        self.botao_cadastrar_pendencia_troca.place(x=50, y=180)
        self.botao_editar_pendencia_troca.place(x=50, y=210)
        self.botao_excluir_pendencia_troca.place(x=50, y=240)



    def mostrar_opcoes_relatorios(self):
        self.botao_escala.place(x=10, y=100)
        self.botao_pendencia_troca.place(x=10, y=140)
        self.botao_relatorios.place(x=10, y=180)
        self.botao_funcionarios.place(x=10, y=260)
        self.botao_veiculos.place(x=10, y=300)


        self.botao_editar_escala.place_forget()
        self.botao_visualizar_escala.place_forget()

        self.botao_cadastrar_pendencia_troca.place_forget()
        self.botao_editar_pendencia_troca.place_forget()
        self.botao_excluir_pendencia_troca.place_forget()

        self.botao_cadastrar_funcionario.place_forget()
        self.botao_editar_funcionario.place_forget()
        self.botao_excluir_funcionario.place_forget()

        self.botao_cadastrar_veiculo.place_forget()
        self.botao_editar_veiculo.place_forget()
        self.botao_excluir_veiculo.place_forget()

        self.botao_relatorio_pendencia.place(x=50, y=220)

    def mostrar_opcoes_funcionarios(self):
        self.botao_escala.place(x=10, y=100)
        self.botao_pendencia_troca.place(x=10, y=140)
        self.botao_relatorios.place(x=10, y=180)
        self.botao_funcionarios.place(x=10, y=220)
        self.botao_veiculos.place(x=10, y=360)

        self.botao_editar_escala.place_forget()
        self.botao_visualizar_escala.place_forget()

        self.botao_cadastrar_pendencia_troca.place_forget()
        self.botao_editar_pendencia_troca.place_forget()
        self.botao_excluir_pendencia_troca.place_forget()

        self.botao_relatorio_pendencia.place_forget()

        self.botao_cadastrar_veiculo.place_forget()
        self.botao_editar_veiculo.place_forget()
        self.botao_excluir_veiculo.place_forget()

        self.botao_cadastrar_funcionario.place(x=50, y=260)
        self.botao_editar_funcionario.place(x=50, y=290)
        self.botao_excluir_funcionario.place(x=50, y=320)

    def mostrar_opcoes_veiculos(self):
        self.botao_escala.place(x=10, y=100)
        self.botao_pendencia_troca.place(x=10, y=140)
        self.botao_relatorios.place(x=10, y=180)
        self.botao_funcionarios.place(x=10, y=220)
        self.botao_veiculos.place(x=10, y=260)

        self.botao_editar_escala.place_forget()
        self.botao_visualizar_escala.place_forget()

        self.botao_cadastrar_pendencia_troca.place_forget()
        self.botao_editar_pendencia_troca.place_forget()
        self.botao_excluir_pendencia_troca.place_forget()

        self.botao_relatorio_pendencia.place_forget()

        self.botao_cadastrar_funcionario.place_forget()
        self.botao_editar_funcionario.place_forget()
        self.botao_excluir_funcionario.place_forget()

        self.botao_cadastrar_veiculo.place(x=50, y=300)
        self.botao_editar_veiculo.place(x=50, y=330)
        self.botao_excluir_veiculo.place(x=50, y=360)
