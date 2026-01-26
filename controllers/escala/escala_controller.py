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
        self.atualizar_numero_total_motoristas()
        self.atualizar_numero_total_ajudantes()



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
        self.atualizar_numero_total_motoristas()
        self.atualizar_numero_total_ajudantes()


    def limpar_cargas(self):

        self.scroll_topo()
        
        self.view.entry_numero_cargas.delete(0, ctk.END)

        for frame in self.view.frames_cargas:
            frame.destroy()

        self.view.frames_cargas.clear()


        self.view.container_cargas._parent_canvas.focus_set()
        self.atualizar_numero_total_cargas()
        self.atualizar_numero_total_motoristas()
        self.atualizar_numero_total_ajudantes()
        self.atualizar_numero_total_repetidos()
        


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
        self.atualizar_numero_viagem_cargas()
        self.atualizar_numero_total_motoristas()
        self.atualizar_numero_total_ajudantes()
        self.atualizar_numero_total_repetidos()


    def remover_carga_especifica(self, frame):
        if not self.view.frames_cargas:
            exibir_mensagem("Aviso", "Não há cargas para remover.", "warning")
            return
        
        if frame in self.view.frames_cargas:
            self.view.frames_cargas.remove(frame)

        frame.destroy()

        self.atualizar_indices_cargas()
        self.atualizar_numero_total_cargas()
        self.atualizar_numero_viagem_cargas()
        self.atualizar_numero_total_motoristas()
        self.atualizar_numero_total_ajudantes()
        self.atualizar_numero_total_repetidos()


    def atualizar_indices_cargas(self):
        for i, frame in enumerate(self.view.frames_cargas):
            frame.label_cod_carga.configure(text=i + 1)


    def atualizar_numero_total_cargas(self):
        quantidade_total = len(self.view.frames_cargas)

        self.view.label_numero_total_cargas.configure(text=f"Total: {quantidade_total}")


    def atualizar_numero_viagem_cargas(self):
        for frame in self.view.frames_cargas:
            codigo = frame.entry_cod_motorista.get().strip()
            if not codigo:
                continue

            funcionario = self.model.buscar_informacoes_funcionario(codigo)
            if funcionario:
                self.exibir_numero_carga(frame)


    def atualizar_numero_total_motoristas(self):
        dados = self.coletar_dados()

        total_motorista = 0

        for carga in dados:
            if not carga["motorista"]:
                continue
            else:
                resultado = self.model.buscar_informacoes_funcionario(carga["motorista"])
                if resultado:
                    total_motorista += 1

        self.view.label_numero_total_motoristas.configure(text=f"Motoristas: {total_motorista}")

    def atualizar_numero_total_ajudantes(self):
        dados = self.coletar_dados()

        total_ajudantes = 0

        for carga in dados:
            if carga["ajudante_1"]:
                resultado = self.model.buscar_informacoes_funcionario(carga["ajudante_1"])
                if resultado:
                    total_ajudantes += 1
            if carga["ajudante_2"]:
                resultado = self.model.buscar_informacoes_funcionario(carga["ajudante_2"])
                if resultado:
                    total_ajudantes += 1

        self.view.label_numero_total_ajudantes.configure(text=f"Ajudantes: {total_ajudantes}")


    def atualizar_numero_total_repetidos(self):
        dados = self.coletar_dados()
        contagem_geral = {}
        total_repetidos = 0

        for carga in dados:
            funcionarios = [carga.get("motorista"), carga.get("ajudante_1"), carga.get("ajudante_2")]
            
            for codigo in funcionarios:
                if codigo and str(codigo).strip():
                    contagem_geral[codigo] = contagem_geral.get(codigo, 0) + 1
                    
        for codigo, qtd in contagem_geral.items():
            if qtd > 1:
                total_repetidos += (qtd - 1)

        self.view.label_numero_total_repetidos.configure(text=f"Repetidos: {total_repetidos}")



    def exibir_nome_funcionario(self, frame, tipo: Literal["motorista", "ajudante1", "ajudante2"]):
        widgets = {
            "motorista": (frame.entry_cod_motorista, frame.label_nome_motorista),
            "ajudante_1": (frame.entry_cod_ajudante_1, frame.label_nome_ajudante_1),
            "ajudante_2": (frame.entry_cod_ajudante_2, frame.label_nome_ajudante_2)
        }
        
        entry, label = widgets[tipo]
        codigo = entry.get().strip()

        if codigo:
            resultado = self.model.buscar_informacoes_funcionario(codigo)
            if resultado:
                nome_exibicao = (resultado[0][:22] + "...") if len(resultado[0]) > 23 else resultado[0]
                label.configure(text=nome_exibicao)
            else:
                label.configure(text="Não encontrado.")
        else:
            label.configure(text="")

        self.exibir_numero_carga(frame)

    
    def exibir_numero_carga(self, frame):

        hoje = datetime.now()
        dia_atual = hoje.strftime("%d")

        codigo = frame.entry_cod_motorista.get().strip()

        resultado = self.model.buscar_informacoes_funcionario(codigo)
        try:
            if resultado[1] != "Ajudante":
                viagem = self.calcular_numero_viagem_carga(codigo, frame)
                numero_carga = f"7{resultado[4]}{dia_atual}{viagem:02d}"
                frame.label_numero_carga.configure(text=numero_carga)
            else:
                frame.label_numero_carga.configure(text="")
        except Exception:
            frame.label_numero_carga.configure(text="")

        
    def calcular_numero_viagem_carga(self, codigo_motorista, frame_atual):
        contador = 0

        for frame in self.view.frames_cargas:
            if frame is frame_atual:
                break
            
            codigo = frame.entry_cod_motorista.get().strip()
            if codigo == codigo_motorista:
                contador += 1

        return contador + 1
    

    def _configurar_eventos_frame_carga(self, frame):
        """Configura os eventos de digitação para um frame carga recém-criado."""

        frame.entry_cod_motorista.bind("<Return>",
            lambda event: self._on_enter_funcionario(frame, "motorista", frame.entry_cod_ajudante_1))
        frame.entry_cod_ajudante_1.bind("<Return>",
            lambda event: self._on_enter_funcionario(frame, "ajudante_1", frame.entry_cod_ajudante_2))
        frame.entry_cod_ajudante_2.bind("<Return>",
            lambda event: self._on_enter_ajudante_2_ultimo(frame))
        

        frame.entry_cod_motorista.bind("<FocusOut>",
            lambda event: self._on_focus_out_funcionario(frame, "motorista"))
        frame.entry_cod_ajudante_1.bind("<FocusOut>",
            lambda event: self._on_focus_out_funcionario(frame, "ajudante_1"))
        frame.entry_cod_ajudante_2.bind("<FocusOut>",
            lambda event: self._on_focus_out_funcionario(frame, "ajudante_2"))
        
        self._configurar_navegacao_tab(frame)
        
        self._recursive_bind_scroll(frame)


    def _processar_funcionario(self, frame, campo):
        codigo = {
            "motorista": frame.entry_cod_motorista.get(),
            "ajudante_1": frame.entry_cod_ajudante_1.get(),
            "ajudante_2": frame.entry_cod_ajudante_2.get()
        }[campo]

        self.verificar_repeticao_ao_digitar(
            codigo,
            frame.label_cod_carga.cget("text")
        )

        self.exibir_nome_funcionario(frame, campo)

        self.atualizar_numero_total_motoristas()
        self.atualizar_numero_total_ajudantes()
        self.atualizar_numero_total_repetidos()


    def _on_enter_funcionario(self, frame, campo, proximo_widget=None):
        entry = {
            "motorista": frame.entry_cod_motorista,
            "ajudante_1": frame.entry_cod_ajudante_1,
            "ajudante_2": frame.entry_cod_ajudante_2,
        }[campo]

        entry._enter_executado = True

        self._processar_funcionario(frame, campo)

        if proximo_widget:
            proximo_widget.focus_set()


    def _on_enter_ajudante_2_ultimo(self, frame):
        entry = frame.entry_cod_ajudante_2
        entry._enter_executado = True

        self._processar_funcionario(frame, "ajudante_2")

        try:
            idx = self.view.frames_cargas.index(frame)
        except ValueError:
            return

        proximo_idx = idx + 1

        if proximo_idx < len(self.view.frames_cargas):
            proximo_frame = self.view.frames_cargas[proximo_idx]
            proximo_entry = proximo_frame.entry_cod_motorista

            proximo_entry.focus_set()
            self._scroll_para_widget(proximo_entry)

        if proximo_idx < len(self.view.frames_cargas):
            proximo_frame = self.view.frames_cargas[proximo_idx]
            entry = proximo_frame.entry_cod_motorista

            entry.focus_set()
            self._scroll_para_widget(entry)


    def _on_focus_out_funcionario(self, frame, campo):
        entry = {
            "motorista": frame.entry_cod_motorista,
            "ajudante_1": frame.entry_cod_ajudante_1,
            "ajudante_2": frame.entry_cod_ajudante_2,
        }[campo]

        if entry._enter_executado:
            entry._enter_executado = False
            return

        self._processar_funcionario(frame, campo)


    def _on_tab(self, event, frame, reverso=False):
        ordem = self._get_ordem_navegacao(frame)

        try:
            idx = ordem.index(event.widget)
        except ValueError:
            return "break"

        novo_idx = idx - 1 if reverso else idx + 1

        if novo_idx >= len(ordem):
            self._ir_para_proxima_carga(frame)
            return "break"

        if novo_idx < 0:
            self._ir_para_carga_anterior(frame)
            return "break"

        destino = ordem[novo_idx]
        destino.focus_set()
        self._scroll_para_widget(destino)

        return "break"


    def _scroll_para_widget(self, widget):
        scrollframe = self.view.container_cargas
        canvas = scrollframe._parent_canvas

        canvas.update_idletasks()

        bbox = canvas.bbox("all")
        if not bbox:
            return

        altura_total = bbox[3]
        altura_canvas = canvas.winfo_height()

        if altura_total <= altura_canvas:
            return

        widget_y = widget.winfo_rooty()
        canvas_y = canvas.winfo_rooty()

        delta = widget_y - canvas_y

        nova_posicao = canvas.canvasy(0) + delta - altura_canvas // 3

        nova_posicao = max(0, min(nova_posicao, altura_total))

        canvas.yview_moveto(nova_posicao / altura_total)
    

    def buscar_funcionario_em_cargas(self, codigo):
        dados = self.coletar_dados()

        ocorrencias = []

        for carga in dados:
            if codigo in (
                carga["motorista"],
                carga["ajudante_1"],
                carga["ajudante_2"]
            ):
                ocorrencias.append(carga["cod_carga"])

        return ocorrencias
    
    def verificar_repeticao_ao_digitar(self, codigo, cod_carga_atual):
        if not codigo.strip():
            return

        dados = self.coletar_dados()

        # -----------------------------
        # A) REPETIÇÃO NA MESMA CARGA
        # -----------------------------
        carga_atual = next(
            carga for carga in dados if carga["cod_carga"] == cod_carga_atual
        )

        campos = [
            carga_atual["motorista"],
            carga_atual["ajudante_1"],
            carga_atual["ajudante_2"]
        ]

        if campos.count(codigo) > 1:
            exibir_mensagem(
                "Funcionário repetido",
                f"O funcionário {codigo} está repetido "
                f"na mesma carga ({cod_carga_atual}).",
                "warning"
            )
            return

        # --------------------------------
        # B) REPETIÇÃO EM OUTRAS CARGAS
        # --------------------------------

        cargas = self.buscar_funcionario_em_cargas(codigo)

        cargas_anteriores = [
            c for c in cargas if c != cod_carga_atual
        ]

        if cargas_anteriores:
            exibir_mensagem(
                "Funcionário repetido",
                f"O funcionário {codigo} já está na(s) carga(s): "
                f"{', '.join(map(str, cargas_anteriores))}",
                "warning"
            )

    def _get_ordem_navegacao(self, frame):
        return [
            frame.entry_cod_motorista._entry,
            frame.entry_cod_ajudante_1._entry,
            frame.entry_cod_ajudante_2._entry,
            frame.entry_rota._entry,
            frame.entry_observacao._entry,
        ]

    
    def _configurar_navegacao_tab(self, frame):
        for entry in self._get_ordem_navegacao(frame):
            entry.bind(
                "<Tab>",
                lambda e, f=frame: self._on_tab(e, f),
                add="+"
            )
            entry.bind(
                "<Shift-Tab>",
                lambda e, f=frame: self._on_tab(e, f, reverso=True),
                add="+"
            )

    def _ir_para_proxima_carga(self, frame_atual):
        try:
            idx = self.view.frames_cargas.index(frame_atual)
        except ValueError:
            return

        proximo_idx = idx + 1

        if proximo_idx >= len(self.view.frames_cargas):
            proximo_idx = 0 

        proximo_frame = self.view.frames_cargas[proximo_idx]
        destino = proximo_frame.entry_cod_motorista._entry

        destino.focus_set()
        self._scroll_para_widget(destino)


    def _ir_para_carga_anterior(self, frame_atual):
        try:
            idx = self.view.frames_cargas.index(frame_atual)
        except ValueError:
            return

        anterior_idx = idx - 1

        if anterior_idx < 0:
            anterior_idx = len(self.view.frames_cargas) - 1

        frame_anterior = self.view.frames_cargas[anterior_idx]
        ordem = self._get_ordem_navegacao(frame_anterior)
        destino = ordem[-1]

        destino.focus_set()
        self._scroll_para_widget(destino)


    def coletar_dados(self):
        dados = []

        for frame in self.view.frames_cargas:
            dados.append({
                "cod_carga": frame.label_cod_carga.cget("text"),
                "numero_carga": frame.label_numero_carga.cget("text"),
                "motorista": frame.entry_cod_motorista.get(),
                "ajudante_1": frame.entry_cod_ajudante_1.get(),
                "ajudante_2": frame.entry_cod_ajudante_2.get(),
                "rota": frame.entry_rota.get(),
                "observacao": frame.entry_observacao.get()
            })

        return dados


    def confirmar(self):

        dados = self.coletar_dados()

        print(dados)