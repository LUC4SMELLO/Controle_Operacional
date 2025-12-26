import customtkinter as ctk

from views.menu_view import TelaMenu
from controllers.fake_controller import FakeController


if __name__ == "__main__":

    janela = ctk.CTk()
    janela.title("Controle Operacional")
    janela.geometry("1280x720")
    
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    controller = FakeController()

    tela = TelaMenu(janela, controller)

    controller.set_view(tela)

    tela.place(relx=0, rely=0, relwidth=1, relheight=1)
    janela.mainloop()
