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

        combobox_tipo = self.view.entry_tipo
        combobox_tipo.bind("<Left>", lambda e: self.navegar_combobox(e, combobox_tipo))
        combobox_tipo.bind("<Right>", lambda e: self.navegar_combobox(e, combobox_tipo))

    
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
                self.view.entry_carga.focus_set()
                return {
                    "sucesso": False,
                    "titulo": "Erro",
                    "mensagem": f"O campo '{campo.replace('_', ' ').replace('co', 'có').replace('sa', 'sá').title()}' é obrigatório!",
                    "icone": "cancel"
                    }
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.entry_tipo.focus_set()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "O valor do campo 'Tipo' está incorreto.",
                "icone": "cancel"
                }

        if int(dados["quantidade"]) <= 0:
            self.view.entry_quantidade.focus_set()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "A quantidade deve ser maior que zero.",
                "icone": "cancel"
                }

        try:
            self.model.cadastrar_pendencia(dados)
            self.limpar_formulario()
            return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Pendência Cadastrada!",
                "icone": "check"
                }
        except Exception as e:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {e}",
                "icone": "cancel"
                }


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
                self.view.entry_cupom.focus_set()
                return {
                    "sucesso": False,
                    "titulo": "Erro",
                    "mensagem": f"O campo '{campo.replace('_', ' ').replace('co', 'có').replace('sa', 'sá').title()}' é obrigatório!",
                    "icone": "cancel"
                    }
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.entry_tipo.focus_set()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "O valor do campo 'Tipo' está incorreto.",
                "icone": "cancel"
                }

        if int(dados["quantidade"]) <= 0:
            self.view.entry_quantidade.focus_set()            
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "A quantidade deve ser maior que zero.",
                "icone": "cancel"
                }
        
        pendencia_existe = self.model.buscar_pendencia(dados["cupom"])
        if not pendencia_existe:
            self.limpar_formulario()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "Pendência Não Encontrada.",
                "icone": "cancel"
                }

        try:
            self.model.editar_pendencia(dados)
            self.limpar_formulario()
            return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Pendência Editada!",
                "icone": "check"
                }
        except Exception as e:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {e}",
                "icone": "cancel"
                }

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

        for campo, valor in dados.items():
            if not valor or valor.strip() == "":
                self.view.entry_cupom.focus_set()
                return {
                    "sucesso": False,
                    "titulo": "Erro",
                    "mensagem": f"O campo '{campo.replace('_', ' ').replace('co', 'có').replace('sa', 'sá').title()}' é obrigatório!",
                    "icone": "cancel"
                    }
            
        if dados["tipo"] not in ["Pendência", "Troca"]:
            self.view.entry_tipo.focus_set()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "O valor do campo 'Tipo' está incorreto.",
                "icone": "cancel"
                }

        if int(dados["quantidade"]) <= 0:
            self.view.entry_quantidade.focus_set()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "A quantidade deve ser maior que zero.",
                "icone": "cancel"
                }

        pendencia_existe = self.model.buscar_pendencia(dados["cupom"])
        if not pendencia_existe:
            self.limpar_formulario()
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "Pendência Não Encontrada.",
                "icone": "cancel"
                }

        try:
            self.model.excluir_pendencia(dados["cupom"])
            self.limpar_formulario()
            return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Pendência Excluída!",
                "icone": "check"
                }
        except Exception as e:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {e}",
                "icone": "cancel"
                }


    def buscar_e_exibir_informacoes_pendencia(self):


        if not self.view.entry_cupom.get():
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "O campo 'Cupom' deve estar preenchido.",
                "icone": "cancel"
                }

        
        resultado = self.model.buscar_pendencia(self.view.entry_cupom.get())

        if not resultado:

            self.limpar_formulario()

            return {
                "sucesso": False,
                "titulo": "Aviso",
                "mensagem": "Cupom não encontrado.",
                "icone": "warning"
                }

        self.limpar_formulario()

        self.view.entry_cupom.insert(0, resultado[0])
        self.view.entry_data.set_date(resultado[1])
        self.view.entry_carga.insert(0, resultado[2])
        self.view.entry_codigo_cliente.insert(0, resultado[3])
        self.view.entry_tipo.set(resultado[4])
        self.view.entry_responsavel.insert(0, resultado[5])
        self.view.entry_codigo_produto.insert(0, resultado[6])
        self.view.entry_quantidade.insert(0, resultado[7])

        return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Cupom encontrado",
                "icone": "warning"
                }




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

