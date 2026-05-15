import customtkinter as ctk
from datetime import datetime

from validators.pendencia_validator import validar_pendencia


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
        if view == "editar":
            self.view.entry_cupom.focus_set()

            fluxo_entrys = [
                (self.view.entry_cupom, self.view.botao_buscar_cupom),
                (self.view.botao_buscar_cupom, self.view.entry_carga),
                (self.view.entry_carga, self.view.entry_codigo_cliente),
                (self.view.entry_codigo_cliente, self.view.entry_tipo),
                (self.view.entry_tipo, self.view.entry_responsavel),
                (self.view.entry_responsavel, self.view.entry_situacao),
                (self.view.entry_situacao, self.view.entry_carga_entregue),
                (self.view.entry_carga_entregue, self.view.entry_codigo_produto),
                (self.view.entry_codigo_produto, self.view.entry_quantidade),
                (self.view.entry_quantidade, self.view.botao_confirmar)
            ]
        if view == "excluir":
            self.view.entry_cupom.focus_set()

            fluxo_entrys = [
                (self.view.entry_cupom, self.view.botao_buscar_cupom),
                (self.view.botao_buscar_cupom, self.view.entry_carga),
                (self.view.entry_carga, self.view.entry_codigo_cliente),
                (self.view.entry_codigo_cliente, self.view.entry_tipo),
                (self.view.entry_tipo, self.view.entry_responsavel),
                (self.view.entry_responsavel, self.view.entry_situacao),
                (self.view.entry_situacao, self.view.entry_carga_entregue),
                (self.view.entry_carga_entregue, self.view.entry_codigo_produto),
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
        combobox_tipo.bind("<Left>", lambda event: self.navegar_combobox(event, combobox_tipo))
        combobox_tipo.bind("<Right>", lambda event: self.navegar_combobox(event, combobox_tipo))

        self.view.entry_codigo_cliente.bind("<Return>", lambda event: self.exibir_razao_social_cliente(event))
        self.view.entry_codigo_produto.bind("<Return>", lambda event: self.exibir_descricao_produto(event))

        self.view.entry_codigo_cliente.bind("<FocusOut>", lambda event: self.exibir_razao_social_cliente(event))
        self.view.entry_codigo_produto.bind("<FocusOut>", lambda event: self.exibir_descricao_produto(event))

        self.view.winfo_toplevel().bind("<Escape>", lambda event: self.limpar_formulario(event))


    
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
    
    def exibir_razao_social_cliente(self, event):
        codigo_cliente = self.view.entry_codigo_cliente.get()

        resultado = self.model.buscar_cliente(codigo_cliente)
        if not resultado:
            self.view.label_razao_social.configure(text="CLIENTE NÃO ENCONTRADO")
            return

        self.view.label_razao_social.configure(text=resultado[0])

    def exibir_descricao_produto(self, event):
        codigo_produto = self.view.entry_codigo_produto.get()

        resultado = self.model.buscar_produto(codigo_produto)
        if not resultado:
            self.view.label_descricao_produto.configure(text="PRODUTO NÃO ENCONTRADO")
            return

        self.view.label_descricao_produto.configure(text=resultado[0])

    def coletar_dados(self):
        dados = {
            "data": self.view.entry_data.get(),
            "carga": self.view.entry_carga.get(),
            "codigo_cliente": self.view.entry_codigo_cliente.get(),
            "tipo": self.view.entry_tipo.get(),
            "responsavel": self.view.entry_responsavel.get(),
            "codigo_produto": self.view.entry_codigo_produto.get(),
            "quantidade": self.view.entry_quantidade.get()
        }

        if hasattr(self.view, "entry_cupom"):
            dados["cupom"] = self.view.entry_cupom.get().strip()
    
        return dados


    def confirmar_cadastro_pendencia(self):

        dados = self.coletar_dados()

        try:
            objeto_data = datetime.strptime(dados["data"], "%d/%m/%Y")
            data_formatada = objeto_data.strftime("%Y-%m-%d")

            dados["data"] = data_formatada
        except Exception:
            dados["data"] = "."

        resultado = validar_pendencia(dados, False)
        if not resultado["sucesso"]:
            return resultado

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

        dados = self.coletar_dados()

        try:
            objeto_data = datetime.strptime(dados["data"], "%d/%m/%Y")
            data_formatada = objeto_data.strftime("%Y-%m-%d")

            dados["data"] = data_formatada
        except Exception:
            dados["data"] = "."

        resultado = validar_pendencia(dados, True)
        if not resultado["sucesso"]:
            return resultado

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

        dados = self.coletar_dados()

        try:
            objeto_data = datetime.strptime(dados["data"], "%d/%m/%Y")
            data_formatada = objeto_data.strftime("%Y-%m-%d")

            dados["data"] = data_formatada
        except Exception:
            dados["data"] = "."


        resultado = validar_pendencia(dados, True)
        if not resultado["sucesso"]:
            return resultado


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


    def buscar_e_exibir_informacoes_pendencia(self, tipo_view="editar"):


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

        

        objeto_data = datetime.strptime(resultado[1], "%Y-%m-%d")
        data_formatada = datetime.strftime(objeto_data, "%d/%m/%Y")

        self.view.entry_cupom.insert(0, resultado[0])
        self.view.entry_cupom.configure(state="readonly")

        self.view.entry_data.set_date(data_formatada)
        self.view.entry_carga.insert(0, resultado[2])
        self.view.entry_codigo_cliente.insert(0, resultado[3])

        if not resultado[4]:
            self.view.label_razao_social.configure(text="CLIENTE NÃO ENCONTRADO")
        else:
            self.view.label_razao_social.configure(text=resultado[4])

        self.view.entry_tipo.set(resultado[5])
        self.view.entry_responsavel.insert(0, resultado[6])
        self.view.entry_situacao.set(resultado[7])
        self.view.entry_carga_entregue.insert(0, resultado[8])
        self.view.entry_codigo_produto.insert(0, resultado[9])

        if not resultado[10]:
            self.view.label_descricao_produto.configure(text="PRODUTO NÃO ENCONTRADO")
        else:
            self.view.label_descricao_produto.configure(text=resultado[10])
            
        self.view.entry_quantidade.insert(0, resultado[11])

        if tipo_view == "excluir":
            self.view.entry_cupom.configure(state="readonly")
            self.view.entry_data.configure(state="readonly")
            self.view.entry_carga.configure(state="readonly")
            self.view.entry_codigo_cliente.configure(state="readonly")
            self.view.entry_tipo.configure(state="readonly")
            self.view.entry_responsavel.configure(state="readonly")
            self.view.entry_situacao.configure(state="readonly")
            self.view.entry_carga_entregue.configure(state="readonly")
            self.view.entry_codigo_produto.configure(state="readonly")
            self.view.entry_quantidade.configure(state="readonly")

        return {
                "sucesso": True,
                "titulo": "Sucesso",
                "mensagem": "Cupom encontrado",
                "icone": "warning"
                }


    def limpar_formulario(self, event=""):
        nomes_campos = [
            "entry_cupom", "entry_data", "entry_carga", "entry_codigo_cliente",
            "entry_tipo", "entry_responsavel", "entry_situacao", "entry_carga_entregue",
            "entry_codigo_produto", "entry_quantidade"
        ]

        for nome in nomes_campos:
            # Tenta pegar o atributo da view com segurança
            campo = getattr(self.view, nome, None)
            
            if campo is not None:
                try:
                    campo.configure(state="normal")
                    # Se for um campo de entrada comum, já aproveita para limpar
                    if hasattr(campo, 'delete'):
                        campo.delete(0, 'end')
                    # Se for um CTkOptionMenu ou similar
                    elif hasattr(campo, 'set'):
                        campo.set("")
                except Exception:
                    pass

        try:
            if hasattr(self.view, 'entry_cupom'):
                self.view.entry_cupom.focus_set()
            else:
                self.view.entry_carga.focus_set()
                
            data_atual = datetime.today().strftime('%d/%m/%Y')
            if hasattr(self.view, 'entry_data'):
                self.view.entry_data.set_date(data_atual)
                
            # Limpar labels que não estão na lista de campos de entrada
            if hasattr(self.view, 'label_razao_social'):
                self.view.label_razao_social.configure(text="")
            if hasattr(self.view, 'label_descricao_produto'):
                self.view.label_descricao_produto.configure(text="")
        except Exception:
            pass
