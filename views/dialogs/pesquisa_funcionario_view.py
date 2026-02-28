import customtkinter as ctk
import tkinter as tk

from constants.textos import FONTE_TEXTO, FONTE_LISTBOX

from services.funcionarios_service import listar_funcionarios_banco_dados


class TelaPesquisarFuncionarioView(ctk.CTkToplevel):

    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.title("Pesquisar Funcionário")
        self.geometry("455x540+850+100")
        self.resizable(False, False)
        self.grab_set()

        self.funcionarios = listar_funcionarios_banco_dados() or []

        self.entry_pesquisa = ctk.CTkEntry(
            self,
            font=FONTE_TEXTO,
            corner_radius=2,
            placeholder_text="Digite o nome do funcionário",
        )
        self.entry_pesquisa.pack(fill="x", padx=10, pady=10)
        self.after(200, self.entry_pesquisa.focus_set)
        self.entry_pesquisa.bind("<KeyRelease>", self.filtrar_funcionarios)
        self.entry_pesquisa.bind("<Return>", self.selecionar_funcionario)
        self.entry_pesquisa.bind("<Down>", self.ir_para_lista)

        self.bind("<FocusIn>", lambda event: self.atualizar_lista(self.funcionarios))

        self.bind("<Escape>", lambda event: self.destroy())

        self.focus_force()

        # LISTBOX (TKINTER)
        self.listbox = tk.Listbox(self, height=15, font=FONTE_LISTBOX)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=5)

        self.listbox.bind("<Double-Button-1>", self.selecionar_funcionario)
        self.listbox.bind("<Return>", self.selecionar_funcionario)
        self.listbox.bind("<Up>", self.navegar_lista)
        self.listbox.bind("<Down>", self.navegar_lista)

        self.atualizar_lista(self.funcionarios)


    def funcionario_em_uso(self, codigo):
        return bool(self.controller.buscar_funcionario_em_cargas(codigo))
    

    def filtrar_funcionarios(self, event=None):
        texto = self.entry_pesquisa.get().lower()

        filtrados = [
            (codigo, nome, funcao, codigo_caminhao)
            for codigo, nome, funcao, codigo_caminhao in self.funcionarios
            if texto in str(codigo).lower()
            or texto in nome.lower()
            or texto in funcao.lower()
            or texto in str(codigo_caminhao).lower()
        ]

        self.atualizar_lista(filtrados)

    def atualizar_lista(self, lista, event=None):
        self.listbox.delete(0, tk.END)

        for codigo, nome, funcao, codigo_caminhhao in lista:
            if not codigo_caminhhao:
                funcionario_formatado = f"{codigo} - {nome} - {funcao}"
            else:
                funcionario_formatado = f"{codigo} - {nome} - {funcao} - {codigo_caminhhao}"

            self.listbox.insert(tk.END, funcionario_formatado)


            ultimo_indice = self.listbox.size() - 1

            em_uso = self.funcionario_em_uso(str(codigo))

            if em_uso:
                self.listbox.itemconfig(ultimo_indice, bg="#89cf5a", fg="black")
            else:
                if funcao.lower() == "motorista":
                    self.listbox.itemconfig(ultimo_indice, bg="#d9d9d9", fg="black")
                elif funcao.lower() == "ajudante":
                    self.listbox.itemconfig(ultimo_indice, bg="#ffffff", fg="black")
                else:
                    self.listbox.itemconfig(ultimo_indice, bg="#2b2b2b", fg="white")


    def selecionar_funcionario(self, event=None):
        try:
            funcionario_selecionado = self.listbox.get(self.listbox.curselection())

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
