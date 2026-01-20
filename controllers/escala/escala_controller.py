from datetime import datetime

from views.escala.components.frame_carga import FrameCarga

from views.dialogs.exibir_mensagem import exibir_mensagem

from constants.rotas import (
    ROTAS_SEGUNDA,
    ROTAS_TERCA,
    ROTAS_QUARTA,
    ROTAS_QUINTA,
    ROTAS_SEXTA
)


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

    def scroll_topo(self):
        self.view.container_cargas._parent_canvas.yview_moveto(0.0)

    def scroll_final(self):
        self.view.container_cargas._parent_canvas.yview_moveto(1.0)

    def exibir_data_atual(self):
        dias_semana = ("Segunda", "Terça", "Quarta", 
                "Quinta", "Sexta", "Sábado", "Domingo")

        hoje = datetime.now()

        data = hoje.strftime("%d/%m/%Y")
        dia_semana = dias_semana[hoje.weekday()]

        self.view.label_data.configure(text=f"{dia_semana}  -  {data}")
        return
    

    def mostrar_escala_dia_semana(self, dia_semana):

        mapa_rotas = {
            "segunda": ROTAS_SEGUNDA,
            "terça":   ROTAS_TERCA,
            "quarta":  ROTAS_QUARTA,
            "quinta":  ROTAS_QUINTA,
            "sexta":   ROTAS_SEXTA
        }

        rotas = mapa_rotas.get(dia_semana.lower(), [])

        self.limpar_cargas()

        self.view.frames_cargas.clear()

        for index, (chave, dados) in enumerate(rotas.items()):
            frame = FrameCarga(self.view.container_cargas, self.view.controller)

            frame.label_cod_carga.configure(text= index + 1)

            frame.entry_rota.set(dados[1])
            frame.entry_observacao.insert(0, dados[2])

            frame.pack(fill="x", pady=5, padx=(5))
            self.view.frames_cargas.append(frame)
        
            self._recursive_bind_scroll(frame)



    def criar_cargas(self):
        try:
            quantidade = int(self.view.entry_numero_cargas.get())

            if quantidade > 30:
                exibir_mensagem("Aviso", "Esse número de cargas não é permitido.", "warning")
                return

        except ValueError:
            exibir_mensagem("Aviso", "Informe um número válido", "warning")
            return

        self.limpar_cargas()

        self.view.frames_cargas.clear()

        for i in range(quantidade):
            frame = FrameCarga(self.view.container_cargas, self.view.controller)
            frame.label_cod_carga.configure(text=i + 1)

            frame.pack(fill="x", pady=5, padx=(5))
            self.view.frames_cargas.append(frame)
        
            self._recursive_bind_scroll(frame)


    def limpar_cargas(self):
        for frame in self.view.frames_cargas:
            frame.destroy()

        self.view.frames_cargas.clear()
        


    def adicionar_carga_separada(self):

        quantidade_cargas_total = len(self.view.frames_cargas)

        frame = FrameCarga(self.view.container_cargas, self.view.controller)
        frame.label_cod_carga.configure(text=quantidade_cargas_total + 1)

        frame.pack(fill="x", pady=5, padx=(5, 10))
        self.view.frames_cargas.append(frame)

        self._recursive_bind_scroll(frame)

        frame.after(10, self.scroll_final)


    def remover_carga_especifica(self, frame):
        if not self.view.frames_cargas:
            exibir_mensagem("Aviso", "Não há cargas para remover.", "warning")
            return
        
        if frame in self.view.frames_cargas:
            self.view.frames_cargas.remove(frame)

        frame.destroy()

        self.atualizar_indices_cargas()


    def atualizar_indices_cargas(self):
        for i, frame in enumerate(self.view.frames_cargas):
            frame.label_cod_carga.configure(text=i + 1)


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
