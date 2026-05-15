import tkinter as ttk
import customtkinter as ctk

janela = ctk.CTk()
janela.title("Controle Operacional")
janela.geometry("1280x720")
janela.after(0, lambda: janela.state("zoomed"))

janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")