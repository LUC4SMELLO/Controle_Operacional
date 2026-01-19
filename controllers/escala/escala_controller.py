from views.escala.components.frame_carga import FrameCarga
from views.dialogs.exibir_mensagem import exibir_mensagem


class EscalaController:
    def __init__(self, janela):
        self.janela = janela
        self.view = None
        self.tela_atual = None

    def set_view(self, view):
        self.view = view



    def _on_mousewheel(self, event):
        # USE O CANVAS INTERNO PARA ROLAR
        self.view.container_cargas._parent_canvas.yview_scroll(int(-1 * (event.delta / 250)), "units")

    def _recursive_bind_scroll(self, widget):
        # O 'add="+"' PERMITE QUE O SCROLL FUNCIONE SEM QUEBRAR O CLIQUE/HOVER DO WIDGET
        widget.bind("<MouseWheel>", self._on_mousewheel, add="+")
        
        # IMPORTANTE: ACESSAR COMPONENTES INTERNOS SE FOR UM WIDGET DO CUSTOMTKINTER
        
        for child in widget.winfo_children():
            self._recursive_bind_scroll(child)





    def criar_cargas(self):
        try:
            quantidade = int(self.view.entry_numero_cargas.get())
        except ValueError:
            exibir_mensagem("Erro", "Informe um número válido", "warning")
            return

        self.limpar_cargas()

        self.view.frames_cargas.clear()

        for i in range(quantidade):
            frame = FrameCarga(self.view.container_cargas, self.view.controller)
            frame.pack(fill="x", pady=5, padx=(5, 10))
            self.view.frames_cargas.append(frame)
        
            self._recursive_bind_scroll(frame)


    def limpar_cargas(self):
        for frame in self.view.frames_cargas:
            frame.destroy()


    def adicionar_carga_separada(self):
        frame = FrameCarga(self.view.container_cargas, self.view.controller)
        frame.pack(fill="x", pady=5, padx=(5, 10))
        self.view.frames_cargas.append(frame)

        self._recursive_bind_scroll(frame)


    def remover_ultima_carga(self):
        if not self.view.frames_cargas:
            exibir_mensagem("Aviso", "Não há cargas para remover.", "warning")
            return

        frame = self.view.frames_cargas.pop()
        frame.destroy()


    def coletar_dados(self):
        dados = []

        for frame in self.view.frames_cargas:
            dados.append({
                "numero_carga": frame.label_numero_carga.cget("text"),
                "motorista": frame.entry_cod_motorista.get(),
                "ajudante_1": frame.entry_cod_ajudante_1.get(),
                "ajudante_2": frame.entry_cod_ajudante_2.get(),
                "rota": frame.entry_rota.get(),
                "observacao": frame.entry_observacao.get()
            })

        return dados
