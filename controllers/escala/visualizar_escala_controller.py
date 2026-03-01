from typing import Literal
import win32clipboard
import io

from datetime import datetime
from PIL import Image, ImageTk

from constants.caminho_arquivos import CAMINHO_IMAGENS_ESCALA

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


    def copiar_imagem_para_clipboard(self, caminho_imagem: Literal["pagina_1", "pagina_2"]):

        if not all(imagens.exists() for imagens in CAMINHO_IMAGENS_ESCALA):
            return

        # ABRE IMAGEM
        if caminho_imagem == "pagina_1":
            imagem = Image.open(CAMINHO_IMAGENS_ESCALA[0])
        else:
            imagem = Image.open(CAMINHO_IMAGENS_ESCALA[1])

        # CONVERTE PARA BPM
        with io.BytesIO() as output:
            imagem.convert("RGB").save(output, "BMP")
            dados = output.getvalue()[14:]

        # COPIA PARA A CLIPBOARD
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, dados)
        win32clipboard.CloseClipboard()
    
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

    def limpar_canvas(self):
        self.view.canvas.delete("all")
        self.view.imagens_tk.clear()
        

    def zoom_in(self):
        self.view.zoom += 0.1
        self.aplicar_zoom(self.view.zoom)

    def zoom_out(self):
        self.view.zoom -= 0.1
        self.aplicar_zoom(self.view.zoom)

    def aplicar_zoom(self, fator):
        self.view.zoom = max(0.3, fator)
        self.redesenhar_imagens()

    def redesenhar_imagens(self):
        self.view.canvas.delete("all")
        self.view.imagens_tk.clear()

        canvas_width = self.view.canvas.winfo_width()

        y_offset = 0
        espacamento = 30

        for img in self.view.imagens_originais:
            largura = int(img.width * self.view.zoom)
            altura = int(img.height * self.view.zoom)

            img_resize = img.resize((largura, altura))
            img_tk = ImageTk.PhotoImage(img_resize)

            self.view.imagens_tk.append(img_tk)

            x = max((canvas_width - largura) // 2, 0)

            self.view.canvas.create_image(x, y_offset, image=img_tk, anchor="nw")

            y_offset += altura + espacamento

        self.view.canvas.configure(scrollregion=self.view.canvas.bbox("all"))

    def zoom_mousewheel(self, event):
        if event.delta > 0:
            self.view.zoom += 0.1
        else:
            self.view.zoom -= 0.1

        self.view.zoom = max(0.3, min(self.view.zoom, 3.0))
        self.redesenhar_imagens()
