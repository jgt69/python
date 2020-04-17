import re
regex_marca = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{5,30}$"
regex_precio = r"^[0-9,\.]{1,9}$"
regex_modelo = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{5,40}$"


def validar_marca(marca):
    validador_marca = re.compile(regex_marca)
    return validador_marca.match(marca)


def validar_modelo(modelo):
    validador_tema = re.compile(regex_modelo)
    return validador_tema.match(modelo)


def validar_precio(precio):
    validador_precio = re.compile(regex_precio)
    return validador_precio.match(precio)