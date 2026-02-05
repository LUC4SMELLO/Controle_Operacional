from datetime import datetime

from scripts.gerar_imagem import gerar_imagem_escala


class VisualizarEscalaController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def exibir_escala(self):

        data = self.view.entry_data.get()

        try:
            objeto_data = datetime.strptime(data, "%d/%m/%Y")
            data_formatada = objeto_data.strftime("%Y-%m-%d")

            data = data_formatada
        except Exception:
            data = "."

        resultado = self.model.buscar_escala(data)

        if not resultado:
            return {
                "sucesso": False,
                "titulo": "Aviso",
                "mensagem": "Nenhuma escala encontrada.",
                "icone": "warning"
            }

        try:
            gerar_imagem_escala(resultado)
        except Exception as e:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {e}",
                "icone": "warning"
            }

        return {
            "sucesso": True,
            "titulo": "Sucesso",
            "mensagem": "Escala Encontrada!",
            "icone": "check"
        }
