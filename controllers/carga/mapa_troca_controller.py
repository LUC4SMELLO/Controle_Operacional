from typing import Literal

from datetime import datetime
from PIL import Image, ImageTk

from scripts.gerar_imagem import gerar_imagem_mapa_troca_frente

from constants.caminho_arquivos import CAMINHO_IMAGEM_MAPA


class MapaTrocaController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view


    def exibir_mapa(self):

        carga = self.view.entry_numero_carga.get().strip()
        if not carga:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": "O campo 'Carga' precisa estar preenchido.",
                "icone": "warning"
            }

        resultado = self.model.buscar_mapa(carga)
        resultado_pendencias = self.model.buscar_pendencias_carga_por_cliente(carga)

        if not resultado:
            return {
                "sucesso": False,
                "titulo": "Aviso",
                "mensagem": "Nenhum mapa encontrado.",
                "icone": "warning"
            }
        
        try:
            gerar_imagem_mapa_troca_frente(resultado, resultado_pendencias)
        except Exception as erro:
            return {
                "sucesso": False,
                "titulo": "Erro",
                "mensagem": f"Falha no banco: {erro}",
                "icone": "warning"
            }
        
        return {
            "sucesso": True,
            "titulo": "Sucesso",
            "mensagem": "Mapa Encontrado!",
            "icone": "check"
        }





    def zoom_in(self):
        self.view.zoom += 0.1
        self.aplicar_zoom(self.view.zoom)

    def zoom_out(self):
        self.view.zoom -= 0.1
        self.aplicar_zoom(self.view.zoom)

    def aplicar_zoom(self, fator):
        self.view.zoom = max(0.3, fator)
        self.redesenhar_imagens()

    def limpar_imagem_mapa(self):
        for img in self.view.imagens_originais:
            try:
                img.close()
            except Exception:
                pass

        self.view.imagens_originais.clear()
        self.view.imagens_tk.clear()
        self.view.canvas.delete("all")

        for caminho in CAMINHO_IMAGEM_MAPA:
            caminho.unlink(missing_ok=True)

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
