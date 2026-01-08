import customtkinter as ctk
import tkinter as tk


class TelaPesquisaProdutoView(ctk.CTkToplevel):

    def __init__(self, master, campo_destino):
        super().__init__(master)

        self.title("Pesquisar Produto")
        self.geometry("300x400")
        self.grab_set()

        self.campo_destino = campo_destino

        self.produtos = [
            "Arroz",
            "Feijão",
            "Açúcar",
            "Café",
            "Macarrão",
            "Farinha de Trigo",
            "Óleo de Soja",
            "Sal",
            "Leite",
            "Manteiga"
        ]


        self.entry_pesquisa = ctk.CTkEntry(self, placeholder_text="Digite o nome do produto")
        self.entry_pesquisa.pack(fill="x", padx=10, pady=10)
        self.after(100, self.entry_pesquisa.focus_set)
        self.entry_pesquisa.bind("<KeyRelease>", self.filtrar_produtos)
        self.entry_pesquisa.bind("<Return>", self.selecionar_produto)
        self.entry_pesquisa.bind("<Down>", self.ir_para_lista)


        # LISTBOX (TKINTER)
        self.listbox = tk.Listbox(self, height=15)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=5)

        self.listbox.bind("<Double-Button-1>", self.selecionar_produto)
        self.listbox.bind("<Return>", self.selecionar_produto)
        self.listbox.bind("<Up>", self.navegar_lista)
        self.listbox.bind("<Down>", self.navegar_lista)


        self.atualizar_lista(self.produtos)


    def filtrar_produtos(self, event=None):
        texto = self.entry_pesquisa.get().lower()

        filtrados = [
            produto for produto in self.produtos
            if texto in produto.lower()
        ]

        self.atualizar_lista(filtrados)

    def atualizar_lista(self, lista):
        self.listbox.delete(0, tk.END)

        for item in lista:
            self.listbox.insert(tk.END, item)

    def selecionar_produto(self, event=None):
        try:
            selecionado = self.listbox.get(self.listbox.curselection())

            self.campo_destino.delete(0, tk.END)
            self.campo_destino.insert(0, selecionado)

            self.destroy()

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
