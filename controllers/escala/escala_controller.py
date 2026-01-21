from typing import Literal
import customtkinter as ctk
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
    def __init__(self, model):
        self.model = model
        self.view = None

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
        
            self._configurar_eventos_frame_carga(frame)

        self.atualizar_numero_total_cargas()



    def criar_cargas(self):
        try:
            quantidade = int(self.view.entry_numero_cargas.get())

            if quantidade > 30:
                exibir_mensagem("Aviso", "Esse número de cargas não é permitido.", "warning")
                return

        except ValueError:
            exibir_mensagem("Aviso", "Informe um número válido.", "warning")
            return

        self.limpar_cargas()

        self.view.frames_cargas.clear()

        for i in range(quantidade):
            frame = FrameCarga(self.view.container_cargas, self.view.controller)
            frame.label_cod_carga.configure(text=i + 1)

            frame.pack(fill="x", pady=5, padx=(5))
            self.view.frames_cargas.append(frame)
        
            self._configurar_eventos_frame_carga(frame)

        self.atualizar_numero_total_cargas()


    def limpar_cargas(self):
        
        self.view.entry_numero_cargas.delete(0, ctk.END)

        for frame in self.view.frames_cargas:
            frame.destroy()

        self.view.frames_cargas.clear()


        self.view.container_cargas._parent_canvas.focus_set()
        self.atualizar_numero_total_cargas()
        


    def adicionar_carga_separada(self):

        quantidade_cargas_total = len(self.view.frames_cargas)

        if quantidade_cargas_total >= 30:
            exibir_mensagem("Aviso", "Número máximo de cargas já alcançado.", "warning")
            return

        frame = FrameCarga(self.view.container_cargas, self.view.controller)
        frame.label_cod_carga.configure(text=quantidade_cargas_total + 1)

        frame.pack(fill="x", pady=5, padx=(5, 10))
        self.view.frames_cargas.append(frame)

        self._configurar_eventos_frame_carga(frame)

        frame.after(10, self.scroll_final)

        self.atualizar_numero_total_cargas()


    def remover_carga_especifica(self, frame):
        if not self.view.frames_cargas:
            exibir_mensagem("Aviso", "Não há cargas para remover.", "warning")
            return
        
        if frame in self.view.frames_cargas:
            self.view.frames_cargas.remove(frame)

        frame.destroy()

        self.atualizar_indices_cargas()
        self.atualizar_numero_total_cargas()


    def atualizar_indices_cargas(self):
        for i, frame in enumerate(self.view.frames_cargas):
            frame.label_cod_carga.configure(text=i + 1)


    def atualizar_numero_total_cargas(self):
        quantidade_total = len(self.view.frames_cargas)

        self.view.label_numero_total_cargas.configure(text=f"Total: {quantidade_total}")


    def exibir_nome_funcionario(self, frame, tipo: Literal["motorista", "ajudante1", "ajudante2"]):
        widgets = {
            "motorista": (frame.entry_cod_motorista, frame.label_nome_motorista),
            "ajudante1": (frame.entry_cod_ajudante_1, frame.label_nome_ajudante_1),
            "ajudante2": (frame.entry_cod_ajudante_2, frame.label_nome_ajdudante_2)
        }
        
        entry, label = widgets[tipo]
        codigo = entry.get().strip()

        if codigo:
            resultado = self.model.buscar_informacoes_funcionario(codigo)
            if resultado:
                nome_exibicao = (resultado[0][:23] + "...") if len(resultado[0]) > 25 else resultado[0]
                label.configure(text=nome_exibicao)
            else:
                label.configure(text="Não encontrado")
        else:
            label.configure(text="")

        self.exibir_numero_carga(frame)

    
    def exibir_numero_carga(self, frame):

        hoje = datetime.now()

        dia_formatado_atual = hoje.strftime("%d")

        codigo = frame.entry_cod_motorista.get()

        resultado = self.model.buscar_informacoes_funcionario(codigo)
        if resultado:
            if resultado[1] != "Ajudante":
                numero_carga = f"7{resultado[4]}{dia_formatado_atual}01"
                frame.label_numero_carga.configure(text=numero_carga)
            else:
                frame.label_numero_carga.configure(text="")
        else:
            frame.label_numero_carga.configure(text="")





    def _configurar_eventos_frame_carga(self, frame):
        """Configura os eventos de digitação para um frame carga recém-criado."""

        frame.entry_cod_motorista.bind("<Return>", 
            lambda event: self.exibir_nome_funcionario(frame, "motorista"))
            
        frame.entry_cod_ajudante_1.bind("<Return>", 
            lambda event: self.exibir_nome_funcionario(frame, "ajudante1"))
            
        frame.entry_cod_ajudante_2.bind("<Return>", 
            lambda event: self.exibir_nome_funcionario(frame, "ajudante2"))

        self._recursive_bind_scroll(frame)





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
