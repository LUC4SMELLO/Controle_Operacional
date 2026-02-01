import customtkinter as ctk
import os

from views.escala.editar_escala_view import EditarEscalaView
from views.pendencia.cadastrar_pendencia_view import CadastrarPendenciaView
from views.pendencia.editar_pendencia_view import EditarPendenciaView
from views.pendencia.excluir_pendencia_view import ExcluirPendenciaView
from views.relatorio.relatorio_pendencia_view import RelatorioPendenciaView
from views.funcionario.cadastrar_funcionario_view import CadastrarFuncionarioView
from views.funcionario.editar_funcionario_view import EditarFuncionarioView
from views.funcionario.excluir_funcionario_view import ExcluirFuncionarioView
from views.veiculo.cadastrar_veiculo_view import CadastrarVeiculoView


from controllers.escala.escala_controller import EscalaController
from controllers.pendencia.pendencia_controller import PendenciaController
from controllers.relatorio.relatorio_controller import RelatorioController
from controllers.funcionario.funcionario_controller import FuncionarioController
from controllers.veiculo.veiculo_controller import VeiculoController

from models.escala.escala_model import EscalaModel
from models.pendencia.pendencia_model import PendenciaModel
from models.relatorio.relatorio_model import RelatorioModel
from models.funcionario.funcionario_model import FuncionarioModel
from models.veiculo.veiculo_model import VeiculoModel


from constants.paths import ARCHIVES_DIR

from scripts.formatar_arquivo_clientes import formatar_arquivo_clientes
from database.banco_dados_clientes import sincronizar_csv_com_banco_dados_clientes

from scripts.formatar_arquivo_produtos import formatar_arquivo_produtos
from database.banco_dados_produtos import sincronizar_csv_com_banco_dados_produtos


class MenuController:
    def __init__(self, janela):
        self.janela = janela
        self.view = None
        self.tela_atual = None

    def set_view(self, view):
        self.view = view

    def alternar_modo_aparencia(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def atualizar_todos_os_bancos_dados(self):

        if ARCHIVES_DIR.exists():
            
            formatar_arquivo_clientes()
            sincronizar_csv_com_banco_dados_clientes()
            print("Banco dados clientes atualizado.")


            formatar_arquivo_produtos()
            sincronizar_csv_com_banco_dados_produtos()
            print("Banco dados produtos atualizado.")

    def definir_tela_atual(self, nova_tela=None):
        if self.tela_atual:
            self.tela_atual.destroy()
            self.tela_atual = None

        if nova_tela is None:
            return

        self.tela_atual = nova_tela
        self.tela_atual.place(x=255, y=0, relwidth=1, relheight=1)
        self.tela_atual.lift()

    def mostrar_opcoes_escala(self):
        self.definir_tela_atual(None)
        self.view.mostrar_opcoes_escala()

    def mostrar_opcoes_pendencia_troca(self):
        self.definir_tela_atual(None)
        self.view.mostrar_opcoes_pendencia_troca()

    def mostrar_opcoes_relatorios(self):
        self.definir_tela_atual(None)
        self.view.mostrar_opcoes_relatorios()

    def mostrar_opcoes_funcionarios(self):
        self.definir_tela_atual(None)
        self.view.mostrar_opcoes_funcionarios()

    def mostrar_opcoes_veiculos(self):
        self.definir_tela_atual(None)
        self.view.mostrar_opcoes_veiculos()

    def mostrar_tela_editar_escala(self):

        model = EscalaModel()

        controller = EscalaController(model)

        tela_editar_escala = EditarEscalaView(self.janela, controller)

        controller.set_view(tela_editar_escala)
        controller.exibir_data_atual()

        self.definir_tela_atual(tela_editar_escala)

    def mostrar_tela_cadastrar_pendencia(self):

        model = PendenciaModel()

        controller = PendenciaController(model)

        tela_cadastrar_pendencia = CadastrarPendenciaView(self.janela, controller)

        controller.set_view(tela_cadastrar_pendencia)
        controller.configurar_binds("cadastrar")

        self.definir_tela_atual(tela_cadastrar_pendencia)

    def mostrar_tela_editar_pendencia(self):

        model = PendenciaModel()

        controller = PendenciaController(model)

        tela_editar_pendencia = EditarPendenciaView(self.janela, controller)

        controller.set_view(tela_editar_pendencia)
        controller.configurar_binds("editar")

        self.definir_tela_atual(tela_editar_pendencia)

    def mostrar_tela_excluir_pendencia(self):

        model = PendenciaModel()

        controller = PendenciaController(model)

        tela_excluir_pendencia = ExcluirPendenciaView(self.janela, controller)

        controller.set_view(tela_excluir_pendencia)
        controller.configurar_binds("excluir")

        self.definir_tela_atual(tela_excluir_pendencia)

    def mostrar_tela_relatorio_pendencia(self):

        model = RelatorioModel()

        controller = RelatorioController(model)

        tela_relatorio_pendencia = RelatorioPendenciaView(self.janela, controller)

        controller.set_view(tela_relatorio_pendencia)

        self.definir_tela_atual(tela_relatorio_pendencia)

    def mostrar_tela_cadastrar_funcionario(self):

        model = FuncionarioModel()

        controller = FuncionarioController(model)

        tela_cadastrar_funcionario = CadastrarFuncionarioView(self.janela, controller)

        controller.set_view(tela_cadastrar_funcionario)
        controller.configurar_binds("cadastrar")

        self.definir_tela_atual(tela_cadastrar_funcionario)

    def mostrar_tela_editar_funcionario(self):

        model = FuncionarioModel()

        controller = FuncionarioController(model)

        tela_editar_funcionario = EditarFuncionarioView(self.janela, controller)

        controller.set_view(tela_editar_funcionario)
        controller.configurar_binds("editar")

        self.definir_tela_atual(tela_editar_funcionario)

    def mostrar_tela_excluir_funcionario(self):

        model = FuncionarioModel()

        controller = FuncionarioController(model)

        tela_excluir_funcionario = ExcluirFuncionarioView(self.janela, controller)

        controller.set_view(tela_excluir_funcionario)
        controller.configurar_binds("excluir")

        self.definir_tela_atual(tela_excluir_funcionario)

    def mostrar_tela_cadastrar_veiculo(self):

        model = VeiculoModel()

        controller = VeiculoController(model)

        tela_cadastrar_veiculo = CadastrarVeiculoView(self.janela, controller)

        controller.set_view(tela_cadastrar_veiculo)
        # controller.configurar_binds("cadastrar")

        self.definir_tela_atual(tela_cadastrar_veiculo)
