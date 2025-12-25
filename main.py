from views.menu import TelaMenu

if __name__ == "__main__":
    import customtkinter as ctk

    class FakeController:

        def alternar_modo_aparencia(self):
            if ctk.get_appearance_mode() == "Light":
                ctk.set_appearance_mode("Dark")
            else:
                ctk.set_appearance_mode("Light")

    app = ctk.CTk()
    app.title("Controle Operacional")
    app.geometry("1280x720")
    ctk.set_appearance_mode("Dark")

    tela = TelaMenu(app, FakeController())
    tela.place(relx=0, rely=0, relwidth=1, relheight=1)

    app.mainloop()
