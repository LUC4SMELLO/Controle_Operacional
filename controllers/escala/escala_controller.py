from views.escala.components.frame_carga import FrameCarga
from views.dialogs.exibir_mensagem import exibir_mensagem


class EscalaController:
    def __init__(self, janela):
        self.janela = janela
        self.view = None
        self.tela_atual = None

    def set_view(self, view):
        self.view = view



    def _bind_mousewheel(self, event):
        self.view.container_cargas._parent_canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.view.container_cargas._parent_canvas.yview_scroll(
                int(-1 * (e.delta / 14)), "units"
                )
            )
        
    def _unbind_mousewheel(self, event):
        self.view.container_cargas._parent_canvas.unbind_all("<MouseWheel>")



    def criar_cargas(self):
        try:
            quantidade = int(self.view.entry_numero_cargas.get())
        except ValueError:
            exibir_mensagem("Erro", "Informe um número válido", "warning")
            return

        # Limpa cargas anteriores
        for frame in self.view.frames_cargas:
            frame.destroy()

        self.view.frames_cargas.clear()

        for i in range(quantidade):
            frame = FrameCarga(self.view.container_cargas)
            frame.pack(fill="x", pady=5, padx=(5, 10))
            self.view.frames_cargas.append(frame)


    def coletar_dados(self):
        dados = []

        for frame in self.view.frames_cargas:
            dados.append({
                "carga": frame.numero_carga,
                "motorista": frame.entry_cod_motorista.get(),
                "ajudante_1": frame.entry_cod_ajudante_1.get(),
                "ajudante_2": frame.entry_cod_ajudante_2.get(),
                "rota": frame.entry_rota.get(),
                "observacao": frame.entry_observacao.get()
            })

        return dados