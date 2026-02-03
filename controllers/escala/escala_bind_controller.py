class EscalaBindController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def set_view(self, view):
        self.view = view

    # CONFIGURAÇÃO POR FRAME
    def configurar_frame(self, frame):
        frame.entry_cod_motorista.bind(
            "<Return>",
            lambda e: self._on_enter(frame, "motorista", frame.entry_cod_ajudante_1)
        )
        frame.entry_cod_ajudante_1.bind(
            "<Return>",
            lambda e: self._on_enter(frame, "ajudante_1", frame.entry_cod_ajudante_2)
        )
        frame.entry_cod_ajudante_2.bind(
            "<Return>",
            lambda e: self._on_enter_ultimo(frame)
        )

        frame.entry_cod_motorista.bind(
            "<FocusOut>",
            lambda e: self._on_focus_out(frame, "motorista")
        )
        frame.entry_cod_ajudante_1.bind(
            "<FocusOut>",
            lambda e: self._on_focus_out(frame, "ajudante_1")
        )
        frame.entry_cod_ajudante_2.bind(
            "<FocusOut>",
            lambda e: self._on_focus_out(frame, "ajudante_2")
        )

        self._bind_autosave_entry(frame.entry_cod_motorista, frame)
        self._bind_autosave_entry(frame.entry_cod_ajudante_1, frame)
        self._bind_autosave_entry(frame.entry_cod_ajudante_2, frame)
        self._bind_autosave_entry(frame.entry_rota, frame)
        self._bind_autosave_entry(frame.entry_observacao, frame)


        self._configurar_tab(frame)

    # ENTER / FOCUS
    def _on_enter(self, frame, campo, proximo=None):
        entry = self._get_entry(frame, campo)
        entry._enter_executado = True

        self.controller._processar_funcionario(frame, campo)

        if proximo:
            proximo.focus_set()

    def _on_enter_ultimo(self, frame):
        entry = frame.entry_cod_ajudante_2
        entry._enter_executado = True

        self.controller._processar_funcionario(frame, "ajudante_2")

        try:
            idx = self.view.frames_cargas.index(frame)
        except ValueError:
            return

        if idx + 1 < len(self.view.frames_cargas):
            proximo = self.view.frames_cargas[idx + 1].entry_cod_motorista
            proximo.focus_set()
            self.controller.scroll.scroll_para_widget(proximo)

    def _on_focus_out(self, frame, campo):
        entry = self._get_entry(frame, campo)
        if getattr(entry, "_enter_executado", False):
            entry._enter_executado = False
            return

        self.controller._processar_funcionario(frame, campo)

    # NAVEGAÇÃO PELO TAB
    def _get_ordem(self, frame):
        return [
            frame.entry_cod_motorista._entry,
            frame.entry_cod_ajudante_1._entry,
            frame.entry_cod_ajudante_2._entry,
            frame.entry_rota._entry,
            frame.entry_observacao._entry,
        ]

    def _configurar_tab(self, frame):
        for entry in self._get_ordem(frame):
            entry.bind("<Tab>", lambda e, f=frame: self._on_tab(e, f), add="+")
            entry.bind("<Shift-Tab>", lambda e, f=frame: self._on_tab(e, f, True), add="+")

    def _on_tab(self, event, frame, reverso=False):
        ordem = self._get_ordem(frame)

        try:
            idx = ordem.index(event.widget)
        except ValueError:
            return "break"

        novo = idx - 1 if reverso else idx + 1

        if novo >= len(ordem):
            self._ir_para_proxima_carga(frame)
            return "break"

        if novo < 0:
            self._ir_para_carga_anterior(frame)
            return "break"

        destino = ordem[novo]
        destino.focus_set()
        self.controller.scroll.scroll_para_widget(destino)
        return "break"

    def _get_entry(self, frame, campo):
        return {
            "motorista": frame.entry_cod_motorista,
            "ajudante_1": frame.entry_cod_ajudante_1,
            "ajudante_2": frame.entry_cod_ajudante_2,
        }[campo]
    

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
        self.controller.scroll.scroll_para_widget(destino)


    def _ir_para_carga_anterior(self, frame_atual):
        try:
            idx = self.view.frames_cargas.index(frame_atual)
        except ValueError:
            return

        anterior_idx = idx - 1

        if anterior_idx < 0:
            anterior_idx = len(self.view.frames_cargas) - 1

        frame_anterior = self.view.frames_cargas[anterior_idx]
        ordem = self._get_ordem(frame_anterior)
        destino = ordem[-1]

        destino.focus_set()
        self.controller.scroll.scroll_para_widget(destino)


    def salvar_automatico(self, frame):
        if self.controller._carregando:
            return

        if self.controller._after_id:
            self.view.after_cancel(self.controller._after_id)

        self.controller._after_id = self.view.after(
            500,
            lambda: self.controller.escala_temporaria.salvar_frame_temporario(frame)
        )

    def _bind_autosave_entry(self, entry, frame):
        entry.bind(
            "<KeyRelease>",
            lambda e, f=frame: self.salvar_automatico(f)
        )
