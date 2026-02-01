import customtkinter as ctk


class VeiculoController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view