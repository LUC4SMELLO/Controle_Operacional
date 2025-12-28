from views.janela import janela

from views.menu_view import TelaMenu
from controllers.menu_controller import MenuController


if __name__ == "__main__":
    
    controller = MenuController(janela)

    tela_menu = TelaMenu(janela, controller)

    controller.set_view(tela_menu)

    tela_menu.place(relx=0, rely=0, relwidth=1, relheight=1)
    janela.mainloop()
