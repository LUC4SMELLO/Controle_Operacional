class EscalaScrollController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def set_view(self, view):
        self.view = view

    # MOUSE WHEEL
    def _on_mousewheel(self, event):
        canvas = self.view.container_cargas._parent_canvas
        canvas.yview_scroll(int(-1 * (event.delta / 250)), "units")

    def recursive_bind_scroll(self, widget):
        widget.bind("<MouseWheel>", self._on_mousewheel, add="+")
        for child in widget.winfo_children():
            self.recursive_bind_scroll(child)

    # PAGE UP / PAGE DOWN
    def configurar_scroll_janela(self):
        janela = self.view.winfo_toplevel()
        janela.bind("<Prior>", self._on_page_up)
        janela.bind("<Next>", self._on_page_down)

    def _on_page_up(self, event):
        self.scroll_container(ir_para_topo=True)
        return "break"

    def _on_page_down(self, event):
        self.scroll_container(ir_para_topo=False)
        return "break"

    # SCROLL
    def scroll_container(self, ir_para_topo: bool):
        self.view.container_cargas.update_idletasks()
        canvas = self.view.container_cargas._parent_canvas
        canvas.yview_moveto(0.0 if ir_para_topo else 1.0)

    def scroll_para_widget(self, widget):
        canvas = self.view.container_cargas._parent_canvas
        canvas.update_idletasks()

        bbox = canvas.bbox("all")
        if not bbox:
            return

        altura_total = bbox[3]
        altura_canvas = canvas.winfo_height()

        widget_y = widget.winfo_rooty()
        canvas_y = canvas.winfo_rooty()

        delta = widget_y - canvas_y
        nova_posicao = canvas.canvasy(0) + delta - altura_canvas // 3
        nova_posicao = max(0, min(nova_posicao, altura_total))

        canvas.yview_moveto(nova_posicao / altura_total)
