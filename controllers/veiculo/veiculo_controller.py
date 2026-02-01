import customtkinter as ctk

from validators.veiculo_validator import validar_veiculo


class VeiculoController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view

    def configurar_binds(self, view):

        if view == "cadastrar":
            self.view.entry_codigo.focus_set()

            fluxo_entrys = [
                (self.view.entry_codigo, self.view.entry_placa),
                (self.view.entry_placa, self.view.entry_codigo_motorista),
                (self.view.entry_codigo_motorista, self.view.botao_confirmar),
            ]
        else:
            self.view.entry_codigo.focus_set()

            fluxo_entrys = [
                (self.view.entry_codigo, self.view.botao_buscar_veiculo),
                (self.view.botao_buscar_veiculo, self.view.entry_placa),
                (self.view.entry_placa, self.view.entry_codigo_motorista),
                (self.view.entry_codigo_motorista, self.view.botao_confirmar),
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

    def coletar_dados(self):
        dados = {
            "codigo": self.view.entry_codigo.get().strip(),
            "placa": self.view.entry_placa.get().strip(),
            "codigo_motorista": self.view.entry_codigo_motorista.get().strip()
        }

        return dados
    
    def confirmar_cadastro_veiculo(self):

        dados = self.coletar_dados()

        resultado = validar_veiculo(dados)
        if not resultado["sucesso"]:
            self.view.entry_codigo.focus_set()
            return resultado
        
        try:
            self.model.cadastrar_veiculo(dados)
            self.limpar_formulario()
            return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Veículo Cadastrado!",
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

        campo_bloqueaveis = [
            self.view.entry_codigo, self.view.entry_placa,
            self.view.entry_codigo_motorista
        ]

        for campo in campo_bloqueaveis:
            campo.configure(state="normal")

        self.view.entry_codigo.focus_set()

        self.view.entry_codigo.delete(0, ctk.END)
        self.view.entry_placa.delete(0, ctk.END)
        self.view.entry_codigo_motorista.delete(0, ctk.END)
        
        