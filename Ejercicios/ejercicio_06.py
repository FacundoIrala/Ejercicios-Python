from data import lista_bzrp
from os import system

# 'QUEVEDO || BZRP Music Sessions #52'
# {
# 'title': 'QUEVEDO || BZRP Music Sessions #52', 
# 'views': 227192970,
# 'length': 204, 
# 'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
# 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
# 'date': '2022-07-06 00:00:00'}

def prueba ():
    titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")
    artista = cadena[0].strip
    cadena2 = cadena[1].split("#")
    tipo =  cadena2 [0]
    numero = cadena2 [1]
    print(cadena)
    print(cadena2)
    print(f"{artista} - {tipo} - {numero}")


prueba()

def prueba2 (titulo:str):
    cadena = titulo.split("||")
    artista = cadena[0].strip
    cadena2 = cadena[1].split("#")
    tipo =  cadena2 [0].strip()
    numero = cadena2 [1].strip()
    print(cadena)
    print(cadena2)
    print(f"{artista} - {tipo} - {numero}")

def test(lista:list):
    for tema in lista:
        prueba2(tema["title"])

test()



def prueba3 (titulo:str):
    cadena = titulo.split("||")
    if(len(cadena) > 1):
        artista = cadena[0].strip
        cadena2 = cadena[1].split("#")
        if(len(cadena2) > 1):
            tipo =  cadena2 [0].strip()
            numero = cadena2 [1].strip()
            print(f"{artista} - {tipo} - {numero}")

def test(lista:list):
    for tema in lista:
        prueba3(tema["title"])


# 'QUEVEDO || BZRP Music Sessions #52'
def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1 = titulo.split(tipo)
    if(len(parte1) == 2):
        artista = parte1[0].replace("||","").strip()
        numero = parte1[1].replace("#","").strip()
        print(f"{artista} - {tipo} - {numero}")


def test(lista:list):
    for tema in lista:
        prueba4(tema["title"])
# 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',


def url(tema:dict):
    # cadena = tema["url"].split("=")
    # print(cadena[1])

    codigo = tema["url"].replace("https://youtube.com/watch?v=","")
    print(codigo)

    l = len("https://youtube.com/watch?v=")
    url = tema["url"]
    codigo = url[l:]
    print(codigo)

    indice = url.index("=") # Devuelve la posicion de la primera ocurrencia del caracter asisganado, el "=" es el delimitador
    codigo = url[indice+1:]# +1 para que empiece en el codigo
    print(codigo)


def test(lista:list):
    for tema in lista:
        url(tema)


# '2022-07-06 00:00:00'
def formatear_fecha(fecha_cadena:str) -> str:
    fecha_split = fecha_cadena.split(" ")
    fecha = fecha_split[0].split("-")
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    separador = "/"
    fecha_formato = separador.join([dia,mes,año])

    return  fecha_formato
    # print(f"{dia} - {mes} - {año}")


def test(lista:list):
    for tema in lista:
       fecha = formatear_fecha(tema["date"])
       print(fecha)
