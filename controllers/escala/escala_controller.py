class EscalaController:
    def __init__(self, janela):
        self.janela = janela
        self.view = None
        self.tela_atual = None

    def set_view(self, view):
        self.view = view