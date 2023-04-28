# Repaso Funciones y el tp
from data_stark import *

# Listar los super agrupados por color  de ojos

'''
"nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''
# Para no repetir
# set 
# If not in
# pensar siempre otra manera


# FUNCION GENERICA, PUEDO BUSCAR CUALQUIER COSA
def listar_agrupados (lista:list, clave:str):
    lista_colores = []
    for heroe in lista:
        color = heroe[clave]
        lista_colores.append(color)
    lista_colores_filtrada = set(lista_colores)
    

    for color in lista_colores_filtrada:
        print(color)
        for heroe in lista:
            if heroe[clave] == color:
                print(f"\t{heroe['nombre']}") # \t es un tab

    print(lista_colores_filtrada)


listar_agrupados(lista_personajes, "color_pelo")


# ----------------------------------------------------------------
# STRINGS
# Son un tipo de dato inmutable

mi_cadena = "hola"
print(id(mi_cadena))
mi_cadena = "chau"
print(id(mi_cadena)) # cambia de direccion de memoria
                     # random acces memory, siempre sera distinta la posicion de dircc de memoria


# TIPOS DE METODOS

# Strip, saca los espacios
mi_cadena = "    hola mundo    "

mi_cadena = mi_cadena.strip # METODO
mi_cadena = str(mi_cadena)  # FUNCION

mi_cadena = mi_cadena.upper() # Todo mayus
mi_cadena = mi_cadena.lower() # Todo minus
mi_cadena = mi_cadena.capitalize() # Primera letra mayus
mi_cadena = mi_cadena.replace("mundo", "zzzz") # Remplaza la primera palabra, x la asignada

# MALA PRACTICA
mi_cadena = mi_cadena.replace("mundo", "zzzz").strip  

print(mi_cadena)

# ----------------------------------------------------------------------

# "," -> caracter delimitador
# Separa las palabras por la coma

mi_cadena = "Pyton, Java, JavaScript, c#"
lista_split = mi_cadena.split(",") 
for lenguaje in lista_split:
    print(lenguaje.split())

# -----------------------------------------------------------------------

# .join une todo mediante la /

separador = "/"
dia = "10"
mes = "9"
año = "2005"
fecha = separador.join([dia,mes,año]) 

print(fecha)

# -----------------------------------------------------------------------

# Agrega 0, se podria usar para que queden en la misma alturas los legajos

cadena = "123"
cadena = cadena.zfill (25) 
print (cadena)

# -----------------------------------------------------------------------

# Isaplha devuelve true cuando no hay caracteres  especiales o numeros

mi_cadena = "holamundo"
print(mi_cadena.isalpha())

# Ahora si tenemos letras y numeros usaremos, isalnum. Los espacios daran false

mi_cadena = "holamundo"
print(mi_cadena.isalnum())

# -----------------------------------------------------------------------

# Len, contador de letras

mi_cadena = "holamundo"
print(len(mi_cadena))

# Count, cuenta las veces de la palabra asignada
# Sirve para numeros tambien

mi_cadena = "holalala"
print(mi_cadena.count("la"))

# ------------------------------------------------------------------------

# te trae de valor 5 hasta el 10 incluido
# [:5] desde el inicio hasta la letra 5
# [5:] desde la letra 5 hasta el final

cadena = "hola mundo"
print(cadena[5:10])