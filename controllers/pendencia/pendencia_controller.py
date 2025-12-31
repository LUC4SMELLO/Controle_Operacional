import customtkinter as ctk
from datetime import date


class PendenciaController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view
    
    def configurar_binds(self, view):


        if view == "cadastrar":
            self.view.entry_carga.focus_set()

            fluxo_entrys = [
                (self.view.entry_carga, self.view.entry_codigo_cliente),
                (self.view.entry_codigo_cliente, self.view.entry_tipo),
                (self.view.entry_tipo, self.view.entry_responsavel),
                (self.view.entry_responsavel, self.view.entry_codigo_produto),
                (self.view.entry_codigo_produto, self.view.entry_quantidade),
                (self.view.entry_quantidade, self.view.botao_confirmar)
            ]
        else:
            self.view.entry_cupom.focus_set()

            fluxo_entrys = [
                (self.view.entry_cupom, self.view.botao_buscar_cupom),
                (self.view.botao_buscar_cupom, self.view.entry_carga),
                (self.view.entry_carga, self.view.entry_codigo_cliente),
                (self.view.entry_codigo_cliente, self.view.entry_tipo),
                (self.view.entry_tipo, self.view.entry_responsavel),
                (self.view.entry_responsavel, self.view.entry_codigo_produto),
                (self.view.entry_codigo_produto, self.view.entry_quantidade),
                (self.view.entry_quantidade, self.view.botao_confirmar)
            ]

        for widget_atual, proximo_widget in fluxo_entrys:
            widget_atual.bind("<Return>", lambda event, nxt=proximo_widget: self.focar_proximo(nxt))

    def focar_proximo(self, proximo_widget):
        proximo_widget.focus_set()
        return "break"
    

    def confirmar_cadastro_pendencia(self):

        dados = {
            "data": self.view.entry_data.get(),
            "carga": self.view.entry_carga.get(),
            "codigo_cliente": self.view.entry_codigo_cliente.get(),
            "tipo": self.view.entry_tipo.get(),
            "responsavel": self.view.entry_responsavel.get(),
            "codigo_produto": self.view.entry_codigo_produto.get(),
            "quantidade": self.view.entry_quantidade.get()
        }

    
        for campo, valor in dados.items():
            if not valor or valor.strip() == "":
                self.view.exibir_mensagem("Erro", f"O campo '{campo.replace('_', ' ').replace("co", "có").replace("sa", "sá").title()}' é obrigatório!", icone="cancel")
                return
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.exibir_mensagem("Erro", "O valor do campo 'Tipo' está incorreto.", icone="cancel")
            return

        if int(dados["quantidade"]) <= 0:
            self.view.exibir_mensagem("Erro", "A quantidade deve ser maior que zero.", icone="cancel")
            return

        try:
            self.model.cadastrar_pendencia(dados)
            self.limpar_formulario()
            self.view.exibir_mensagem("Sucesso", "Pendência Cadastrada!", icone="check")
        except Exception as e:
            self.view.exibir_mensagem("Erro", f"Falha no banco: {e}", icone="cancel")


    def confirmar_edicao_pendencia(self):

        dados = {
            "cupom": self.view.entry_cupom.get(),
            "data": self.view.entry_data.get(),
            "carga": self.view.entry_carga.get(),
            "codigo_cliente": self.view.entry_codigo_cliente.get(),
            "tipo": self.view.entry_tipo.get(),
            "responsavel": self.view.entry_responsavel.get(),
            "codigo_produto": self.view.entry_codigo_produto.get(),
            "quantidade": self.view.entry_quantidade.get()
        }

    
        for campo, valor in dados.items():
            if not valor or valor.strip() == "":
                self.view.exibir_mensagem("Erro", f"O campo '{campo.replace('_', ' ').replace("co", "có").replace("sa", "sá").title()}' é obrigatório!", icone="cancel")
                return
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.exibir_mensagem("Erro", "O valor do campo 'Tipo' está incorreto.", icone="cancel")
            return

        if int(dados["quantidade"]) <= 0:
            self.view.exibir_mensagem("Erro", "A quantidade deve ser maior que zero.", icone="cancel")
            return

        try:
            self.model.editar_pendencia(dados)
            self.limpar_formulario()
            self.view.exibir_mensagem("Sucesso", "Pendência Editada!", icone="check")
        except Exception as e:
            self.view.exibir_mensagem("Erro", f"Falha no banco: {e}", icone="cancel")

    def confirmar_exclusao_pendencia(self):
        dados = {
            "cupom": self.view.entry_cupom.get(),
            "data": self.view.entry_data.get(),
            "carga": self.view.entry_carga.get(),
            "codigo_cliente": self.view.entry_codigo_cliente.get(),
            "tipo": self.view.entry_tipo.get(),
            "responsavel": self.view.entry_responsavel.get(),
            "codigo_produto": self.view.entry_codigo_produto.get(),
            "quantidade": self.view.entry_quantidade.get()
        }

        if not self.view.entry_cupom.get():
            self.view.exibir_mensagem("Erro", "O campo 'Cupom' deve estar preenchido.", icone="cancel")
            return
        
        for campo, valor in dados.items():
            if not valor or valor.strip() == "":
                self.view.exibir_mensagem("Erro", f"O campo '{campo.replace('_', ' ').replace("co", "có").replace("sa", "sá").title()}' é obrigatório!", icone="cancel")
                return
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.exibir_mensagem("Erro", "O valor do campo 'Tipo' está incorreto.", icone="cancel")
            return

        if int(dados["quantidade"]) <= 0:
            self.view.exibir_mensagem("Erro", "A quantidade deve ser maior que zero.", icone="cancel")
            return

        try:
            self.model.excluir_pendencia(dados["cupom"])
            self.limpar_formulario()
            self.view.exibir_mensagem("Sucesso", "Pendência Excluída!", icone="check")
        except Exception as e:
            self.view.exibir_mensagem("Erro", f"Falha no banco: {e}", icone="cancel")


    def buscar_e_exibir_informacoes_pendencia(self):


        if not self.view.entry_cupom.get():
            self.view.exibir_mensagem("Erro", "O campo 'Cupom' deve estar preenchido.", icone="cancel")
            return

        
        resultado = self.model.buscar_pendencia(self.view.entry_cupom.get())

        if not resultado:
            self.view.exibir_mensagem("Aviso", "Cupom não encontrado.", icone="warning")
            return

        self.limpar_formulario()

        self.view.entry_cupom.insert(0, resultado[0])
        self.view.entry_data.set_date(resultado[1])
        self.view.entry_carga.insert(0, resultado[2])
        self.view.entry_codigo_cliente.insert(0, resultado[3])
        self.view.entry_tipo.set(resultado[4])
        self.view.entry_responsavel.insert(0, resultado[5])
        self.view.entry_codigo_produto.insert(0, resultado[6])
        self.view.entry_quantidade.insert(0, resultado[7])



    def limpar_formulario(self):
        data_atual = date.today()
        data_formatada = data_atual.strftime('%d/%m/%Y')

        try:
            self.view.entry_cupom.focus_set()
            self.view.entry_cupom.delete(0, ctk.END)
        except Exception:
            self.view.entry_carga.focus_set()

        finally:

            self.view.entry_data.set_date(data_formatada)
            self.view.entry_carga.delete(0, ctk.END)
            self.view.entry_codigo_cliente.delete(0, ctk.END)
            self.view.entry_tipo.set("")
            self.view.entry_responsavel.delete(0, ctk.END)
            self.view.entry_codigo_produto.delete(0, ctk.END)
            self.view.entry_quantidade.delete(0, ctk.END)

