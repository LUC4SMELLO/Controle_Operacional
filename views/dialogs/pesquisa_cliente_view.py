import customtkinter as ctk
import tkinter as tk

import re

from constants.textos import FONTE_TEXTO, FONTE_LISTBOX

from services.clientes_service import listar_clientes_banco_dados


class TelaPesquisaClienteView(ctk.CTkToplevel):

    def __init__(self, master, campo_destino, campo_apos_pesquisa, label_razao_social):
        super().__init__(master)

        self.title("Pesquisar Cliente")
        self.geometry("455x540+850+100")
        self.resizable(False, False)
        self.grab_set()

        self.campo_destino = campo_destino
        self.campo_apos_pesquisa = campo_apos_pesquisa
        self.label_razao_social = label_razao_social

        self.clientes = listar_clientes_banco_dados() or {}

        self.entry_pesquisa = ctk.CTkEntry(self, font=FONTE_TEXTO, corner_radius=2, placeholder_text="Digite a razão social do cliente")
        self.entry_pesquisa.pack(fill="x", padx=10, pady=10)
        self.after(200, self.entry_pesquisa.focus_set)
        self.entry_pesquisa.bind("<KeyRelease>", self.filtrar_clientes)
        self.entry_pesquisa.bind("<Return>", self.selecionar_cliente)
        self.entry_pesquisa.bind("<Down>", self.ir_para_lista)

        self.bind("<Escape>", lambda event: self.destroy())  

        self.focus_force()


        # LISTBOX (TKINTER)
        self.listbox = tk.Listbox(self, height=15, font=FONTE_LISTBOX)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=5)

        self.listbox.bind("<Double-Button-1>", self.selecionar_cliente)
        self.listbox.bind("<Return>", self.selecionar_cliente)
        self.listbox.bind("<Up>", self.navegar_lista)
        self.listbox.bind("<Down>", self.navegar_lista)


        self.atualizar_lista(self.clientes.items())


    def filtrar_clientes(self, event=None):
        texto = self.entry_pesquisa.get().lower()

        filtrados = [
            (codigo, nome) for codigo, nome in self.clientes.items()
            if texto in str(codigo).lower() or texto in nome.lower()
        ]


        self.atualizar_lista(filtrados)

    def atualizar_lista(self, lista):
        self.listbox.delete(0, tk.END)

        for codigo, nome in lista:

            item_formatado = f"{codigo} - {nome}"

            self.listbox.insert(tk.END, item_formatado)

    def selecionar_cliente(self, event=None):
        try:
            cliente_selecionado = self.listbox.get(self.listbox.curselection())

            match_codigo = re.search(r"^\d+", cliente_selecionado)
            match_razao_social = re.search(r" - (.+)", cliente_selecionado)

            if match_codigo and match_razao_social:
            
                codigo_cliente = match_codigo.group()
                razao_social_cliente = match_razao_social.group(1)

                self.campo_destino.delete(0, tk.END)
                self.campo_destino.insert(0, codigo_cliente)
                self.label_razao_social.configure(text=razao_social_cliente)

                self.destroy()

                self.campo_apos_pesquisa.focus_set()

        except (tk.TclError, AttributeError):
            pass


    def ir_para_lista(self, event):
        if self.listbox.size() == 0:
            return

        self.listbox.focus_set()

        # SE NADA ESTIVER SELECIONADO SELECIONA O PRIMEIRO ITEM
        if not self.listbox.curselection():
            self.listbox.selection_set(0)
            self.listbox.activate(0)
        return "break"
    

    def navegar_lista(self, event):
        selecionado = self.listbox.curselection()

        if not selecionado:
            index = 0
        else:
            index = selecionado[0]

        # DESCER NA LISTA
        if event.keysym == "Down":
            if index < self.listbox.size() - 1:
                index += 1

        # SUBIR NA LISTA
        elif event.keysym == "Up":
        
            if index == 0:
                self.entry_pesquisa.focus_set()
                self.listbox.selection_clear(0, "end")
                return "break"
            else:
                index -= 1

        self.listbox.selection_clear(0, "end")
        self.listbox.selection_set(index)
        self.listbox.activate(index)
        self.listbox.see(index)

        return "break"
