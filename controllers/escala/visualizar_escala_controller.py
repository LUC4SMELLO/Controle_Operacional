from datetime import datetime
from PIL import ImageTk

from constants.caminho_arquivos import CAMINHO_IMAGENS_ESCALA

from scripts.gerar_imagem import gerar_imagem_escala


class VisualizarEscalaController:
    def __init__(self, model):
        self.model = model
        self.view = None

        self.zoom = 1.0

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
    
    def limpar_imagens_escala(self):
        for img in self.view.imagens_originais:
            try:
                img.close()
            except Exception:
                pass

        self.view.imagens_originais.clear()
        self.view.imagens_tk.clear()
        self.view.canvas.delete("all")

        for caminho in CAMINHO_IMAGENS_ESCALA:
            caminho.unlink(missing_ok=True)
        

    def zoom_in(self):
        self.zoom += 0.1
        self.aplicar_zoom(self.zoom)

    def zoom_out(self):
        self.zoom -= 0.1
        self.aplicar_zoom(self.zoom)

    def aplicar_zoom(self, fator):
        self.zoom = max(0.3, fator)
        self.redesenhar_imagens()

    def redesenhar_imagens(self):
        self.view.canvas.delete("all")
        self.view.imagens_tk.clear()

        y_offset = 0
        espacamento = 30

        for img in self.view.imagens_originais:
            largura = int(img.width * self.zoom)
            altura = int(img.height * self.zoom)

            img_resize = img.resize((largura, altura))
            img_tk = ImageTk.PhotoImage(img_resize)

            self.view.imagens_tk.append(img_tk)

            self.view.canvas.create_image(0, y_offset, image=img_tk, anchor="nw")

            y_offset += altura + espacamento

        self.view.canvas.configure(scrollregion=self.view.canvas.bbox("all"))

    def zoom_mousewheel(self, event):
        if event.delta > 0:
            self.zoom += 0.1
        else:
            self.zoom -= 0.1

        self.zoom = max(0.3, min(self.zoom, 3.0))
        self.redesenhar_imagens()
