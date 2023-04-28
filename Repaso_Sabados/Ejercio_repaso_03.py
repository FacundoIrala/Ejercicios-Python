'''
1.Contar letras: Crea una función que tome una cadena
de texto como argumento y
cuente el número de letras que contiene.

'''
from os import  system #importo de la biblioteca 
from sys import getsizeof



def contar_letras(cadena:str):
    contador = 0
    for letra in cadena:
        if letra.isalpha():
            contador += 1
        else:
            print("tiene letras la cadena")
    return contador

system("cls")

texto = "holaaaaaaaa"
texto2 = "Hola que tal, me llamo facu!312312321321"
num_letras = contar_letras(texto)
num_letras2 = contar_letras(texto2)
print(num_letras)
print("---------------")
print(num_letras2)

'''
2.Eliminar caracteres: Crea una función que tome una
cadena de texto y un carácter como argumentos, y
elimine todas las ocurrencias de ese carácter en la
cadena.
'''








# saludo = "       hola    " 
# prueba = saludo.strip()
# print(prueba) #saca espacios de adelante