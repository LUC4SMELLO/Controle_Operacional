import customtkinter as ctk
import tkinter as tk

import re

from constants.textos import FONTE_TEXTO


class TelaPesquisaProdutoView(ctk.CTkToplevel):

    def __init__(self, master, campo_destino, campo_apos_pesquisa):
        super().__init__(master)

        self.title("Buscar Produto")
        self.geometry("300x400+850+100")
        self.resizable(False, False)
        self.grab_set()

        self.campo_destino = campo_destino
        self.campo_apos_pesquisa = campo_apos_pesquisa

        self.produtos = {
            "8533": "Coca Cola Lata 350ml",
            "56600": "Coca Cola 2L",
            "55818": "Coca Cola Zero 2L",
            "119567": "Ades Pessêgo 200ml",
            "141160": "Pringles Original"
        }


        self.entry_pesquisa = ctk.CTkEntry(self, font=FONTE_TEXTO, corner_radius=2, placeholder_text="Digite o nome do produto")
        self.entry_pesquisa.pack(fill="x", padx=10, pady=10)
        self.after(100, self.entry_pesquisa.focus_set)
        self.entry_pesquisa.bind("<KeyRelease>", self.filtrar_produtos)
        self.entry_pesquisa.bind("<Return>", self.selecionar_produto)
        self.entry_pesquisa.bind("<Down>", self.ir_para_lista)

        self.bind("<Escape>", lambda event: self.destroy())  

        self.focus_force()


        # LISTBOX (TKINTER)
        self.listbox = tk.Listbox(self, height=15)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=5)

        self.listbox.bind("<Double-Button-1>", self.selecionar_produto)
        self.listbox.bind("<Return>", self.selecionar_produto)
        self.listbox.bind("<Up>", self.navegar_lista)
        self.listbox.bind("<Down>", self.navegar_lista)


        self.atualizar_lista(self.produtos.items())


    def filtrar_produtos(self, event=None):
        texto = self.entry_pesquisa.get().lower()

        filtrados = [
            (codigo, nome) for codigo, nome in self.produtos.items()
            if texto in codigo.lower() or texto in nome.lower()
        ]


        self.atualizar_lista(filtrados)

    def atualizar_lista(self, lista):
        self.listbox.delete(0, tk.END)

        for codigo, nome in lista:

            item_formatado = f"{codigo} - {nome}"

            self.listbox.insert(tk.END, item_formatado)

    def selecionar_produto(self, event=None):
        try:
            produto_selecionado = self.listbox.get(self.listbox.curselection())

            resultado = re.search(r"^\d+", produto_selecionado)
            
            codigo_produto = resultado.group()

            self.campo_destino.delete(0, tk.END)
            self.campo_destino.insert(0, codigo_produto)

            self.destroy()

            self.campo_apos_pesquisa.focus_set()

        except tk.TclError:
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
