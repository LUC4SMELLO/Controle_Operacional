from CTkMessagebox import CTkMessagebox

from constants.textos import FONTE_TEXTO
from constants.cores import COR_TEXTO, COR_BOTAO, COR_TEXTO_BOTAO, HOVER_BOTAO


def exibir_mensagem(titulo:str, mensagem:str, icone="info"):
    """
    Exibe um popup com uma mensagem.

    Parameters
    ----------
        titulo : str
            O texto que será o título do popup.
        mensagem : str
            O texto que será a mensagem do popup.
        icone : str
            O ícone do popup, podem ser (check, cancel, info, question, warning).
            O padrão é "info".
    """
    CTkMessagebox(
        title=titulo,
        message=mensagem,
        icon=icone,
        width=320,
        height=50,
        font=FONTE_TEXTO,
        text_color=COR_TEXTO,
        button_color=COR_BOTAO,
        button_text_color=COR_TEXTO_BOTAO,
        button_hover_color=HOVER_BOTAO,
        option_1="Ok"
        )
