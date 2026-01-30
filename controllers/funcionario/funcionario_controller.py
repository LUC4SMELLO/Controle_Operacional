import customtkinter as ctk

from validators.funcionario_validator import validar_funcionario


class FuncionarioController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view

    def configurar_binds(self, view):

        if view == "cadastrar":
            self.view.entry_codigo.focus_set()

            fluxo_entrys = [
                (self.view.entry_codigo, self.view.entry_nome_completo),
                (self.view.entry_nome_completo, self.view.entry_cpf),
                (self.view.entry_cpf, self.view.entry_rg),
                (self.view.entry_rg, self.view.entry_funcao),
                (self.view.entry_funcao, self.view.botao_confirmar)
            ]
        else:
            self.view.entry_codigo.focus_set()

            fluxo_entrys = [
                (self.view.entry_codigo, self.view.entry_nome_completo),
                (self.view.entry_nome_completo, self.view.entry_cpf),
                (self.view.entry_cpf, self.view.entry_rg),
                (self.view.entry_rg, self.view.entry_funcao),
                (self.view.entry_funcao, self.view.botao_confirmar)
            ]


        for widget_atual, proximo_widget in fluxo_entrys:
            widget_atual.bind("<Return>", lambda event, nxt=proximo_widget: nxt.focus_set())
    
            if isinstance(proximo_widget, ctk.CTkButton):
                # QUANDO O FOCO CHEGA NO BOTÃO
                proximo_widget.bind("<FocusIn>", lambda event, btn=proximo_widget: btn.configure(
                    border_width=1, 
                    border_color="#FFFFFF"
                ))
                
                # QUANDO O FOCO SAI DO BOTÃO
                proximo_widget.bind("<FocusOut>", lambda event, btn=proximo_widget: btn.configure(
                    border_width=0
                ))
                
                # BIND PARA EXECUTAR FUNÇÃO AO APERTAR ENTER NO BOTÃO FOCADO
                proximo_widget.bind("<Return>", lambda event, btn=proximo_widget: btn.invoke())

        combobox_tipo = self.view.entry_funcao
        combobox_tipo.bind("<Left>", lambda event: self.navegar_combobox(event, combobox_tipo))
        combobox_tipo.bind("<Right>", lambda event: self.navegar_combobox(event, combobox_tipo))

    
    def navegar_combobox(self, event, combobox):
        valores = combobox.cget("values")
        if not valores: return "break"
        
        try:
            indice_atual = valores.index(combobox.get())
        except ValueError:
            indice_atual = -1

        if event.keysym == "Right":
            proximo_indice = (indice_atual + 1) % len(valores)
        elif event.keysym == "Left":
            proximo_indice = (indice_atual - 1) % len(valores)
        else:
            return

        combobox.set(valores[proximo_indice])
        return "break"
    
    
    def coletar_dados(self):
        dados = {
            "codigo": self.view.entry_codigo.get(),
            "nome_completo": self.view.entry_nome_completo.get(),
            "cpf": self.view.entry_cpf.get(),
            "rg": self.view.entry_rg.get(),
            "funcao": self.view.entry_funcao.get()
        }

        return dados
    

    def confirmar_cadastro_funcionario(self):

        dados = self.coletar_dados()

        resultado = validar_funcionario(dados)
        if not resultado["sucesso"]:
            return resultado
        
        try:
            self.model.cadastrar_funcionario(dados)
            self.limpar_formulario()
            return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Funcionário Cadastrado!",
                "icone": "check"
            }
        except Exception as e:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {e}",
                "icone": "cancel"
            }

    def limpar_formulario(self):
        campos_bloqueáveis = [
            self.view.entry_codigo, self.view.entry_nome_completo,
            self.view.entry_cpf, self.view.entry_rg,
            self.view.entry_funcao
            ]

        for campo in campos_bloqueáveis:
            campo.configure(state="normal")

        self.view.entry_codigo.focus_set()

        self.view.entry_codigo.delete(0, ctk.END)
        self.view.entry_nome_completo.delete(0, ctk.END)
        self.view.entry_cpf.delete(0, ctk.END)
        self.view.entry_rg.delete(0, ctk.END)
        self.view.entry_funcao.set("")
