# NO CONTROLLER:
# return {
#     "sucesso": True,
#     "mensagem": "Pendência cadastrada com sucesso"
# }


# NA VIEW:
# from views.dialogs.message_dialog import exibir_mensagem

# def confirmar(self):
#     resultado = self.controller.confirmar_cadastro_pendencia()

#     if resultado["sucesso"]:
#         exibir_mensagem("Sucesso", resultado["mensagem"], "check")
#     else:
#         exibir_mensagem("Erro", resultado["mensagem"], "error")