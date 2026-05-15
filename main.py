from views.janela import janela

from views.menu.menu_view import MenuView
from controllers.menu.menu_controller import MenuController


if __name__ == "__main__":
    
    controller = MenuController(janela)

    tela_menu = MenuView(janela, controller)

    controller.set_view(tela_menu)

    tela_menu.grid(row=0, column=0, sticky="nsew")
    janela.mainloop()
