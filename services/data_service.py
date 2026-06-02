import datetime
import locale


def buscar_data_por_extenso(data):

    locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

    data_objeto = datetime.datetime.strptime(data, "%Y-%m-%d")

    data_por_extenso = data_objeto.strftime("%A, %d de %B de %Y")

    return data_por_extenso
