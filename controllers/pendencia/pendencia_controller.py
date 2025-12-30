import customtkinter as ctk


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
                self.view.exibir_mensagem("Erro", f"O campo '{campo.replace('_', ' ').replace("co", "có").replace("sa", "sá").title()}' é obrigatório!", icone="error")
                return
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.exibir_mensagem("Erro", "O valor do campo 'Tipo' está incorreto.", icone="error")
            return

        if int(dados["quantidade"]) <= 0:
            self.view.exibir_mensagem("Erro", "A quantidade deve ser maior que zero.", icone="error")
            return

        try:
            self.model.cadastrar_pendencia(dados)
            self.view.exibir_mensagem("Sucesso", "Pendência cadastrada!", icone="info")
            self.limpar_formulario_cadastrar()
        except Exception as e:
            self.view.exibir_mensagem("Erro", f"Falha no banco: {e}", icone="error")

    def limpar_formulario_cadastrar(self):

        self.view.entry_carga.focus_set()

        self.view.entry_carga.delete(0, ctk.END)
        self.view.entry_codigo_cliente.delete(0, ctk.END)
        self.view.entry_tipo.set("")
        self.view.entry_responsavel.delete(0, ctk.END)
        self.view.entry_codigo_produto.delete(0, ctk.END)
        self.view.entry_quantidade.delete(0, ctk.END)

