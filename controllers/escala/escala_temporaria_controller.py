from typing import Literal


class EscalaTemporariaController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def set_view(self, view):
        self.view = view


    def salvar_frame_temporario(self, frame):
        if not frame.label_numero_carga.cget("text").strip():
            return

        dados = {
            "numero_carga": frame.label_numero_carga.cget("text"),
            "horario": frame.label_horario_saida.cget("text"),
            "codigo_motorista": frame.entry_cod_motorista.get(),
            "nome_motorista": frame.label_nome_motorista.cget("text"),
            "codigo_ajudante_1": frame.entry_cod_ajudante_1.get(),
            "nome_ajudante_1": frame.label_nome_ajudante_1.cget("text"),
            "codigo_ajudante_2": frame.entry_cod_ajudante_2.get(),
            "nome_ajudante_2": frame.label_nome_ajudante_2.cget("text"),
            "rota": frame.entry_rota.get(),
            "observacao": frame.entry_observacao.get(),
        }

        self.controller.model.salvar_escala_temporaria(dados)

    def inicializar_escala(self):

        registros = self.controller.model.carregar_escala_temporaria()

        if registros:
            for dados in registros:
                frame = self.view.criar_frame_carga()
                self._preencher_frame(frame, dados)
    
    def carregar_escala_temporaria(self):

        registros = self.controller.model.carregar_escala_temporaria()

        for dados in registros:
            frame = self._buscar_frame_por_numero_carga(dados["numero_carga"])

            if frame:
                self._preencher_frame(frame, dados)
            
    def _buscar_frame_por_numero_carga(self, numero_carga):

        for frame in self.view.frames_cargas:
            if frame.label_numero_carga.cget("text") == numero_carga:
                return frame

        return None
    
    def _preencher_frame(self, frame, dados):

        self._carregando = True

        frame.label_numero_carga.configure(text=dados["numero_carga"])
        frame.label_horario_saida.configure(text=dados["horario"])


        frame.entry_cod_motorista.delete(0, "end")
        frame.entry_cod_motorista.insert(0, dados["codigo_motorista"])

        frame.entry_cod_ajudante_1.delete(0, "end")
        frame.entry_cod_ajudante_1.insert(0, dados["codigo_ajudante_1"])

        frame.entry_cod_ajudante_2.delete(0, "end")
        frame.entry_cod_ajudante_2.insert(0, dados["codigo_ajudante_2"])


        frame.label_nome_motorista.configure(text=dados["nome_motorista"])

        frame.label_nome_ajudante_1.configure(text=dados["nome_ajudante_1"])

        frame.label_nome_ajudante_2.configure(text=dados["nome_ajudante_2"])


        frame.entry_rota.set(dados["rota"])

        frame.entry_observacao.delete(0, "end")
        frame.entry_observacao.insert(0, dados["observacao"])

        self.controller.atualizar_indices_cargas()
        self.controller.atualizar_numero_total_cargas()
        self.controller.atualizar_numero_total_repetidos()
        self.controller.atualizar_numero_total_motoristas()
        self.controller.atualizar_numero_total_ajudantes()

        self._carregando = False


    def salvar_escala_temporaria(self):

        dados = self.coletar_dados()

        for carga in dados:
            self.controller.model.salvar_escala_temporaria(carga)

    def excluir_escala_temporaria(self, frame=None, individual: Literal[True, False] = True):
        if individual:
            self.controller.model.excluir_escala_temporaria(frame.label_numero_carga.cget("text"))
        else:
            self.controller.model.limpar_banco_dados_escala_temporaria()
