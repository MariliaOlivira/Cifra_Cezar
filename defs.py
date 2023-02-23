import string

alfa = list(string.ascii_lowercase)
export = []
count = 0
def cezar_recursivo():
    dict = {}
    dict.keys = alfa
    print(dict)

cezar_recursivo()

def cifra_cesar_encode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 + chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado


def cifra_cesar_decode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 - chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado
