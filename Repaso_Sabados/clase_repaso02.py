from data_stark import lista_personaje

primer_personaje = [0]
altura = float (primer_personaje["altura"])
for personajes in lista_personaje:
    altura_personaje = float (personajes["altura"])
    if altura_personaje > altura:
        altura = altura_personaje
print(f"la altura maxima  es de {altura}")

#-------------------------------------------------------------------------
# FUNCIONES MAL

# def pedir_datos(texto:str)->int:
#     numero = input(texto)
#     numero = int(numero)
#     return numero


# def sumar_numeros()->int:#Implentacion de la funciones
#     primer_numero = int(input("Ingrese el primero numero: "))
#     segundo_numero = int(input("Ingrese el primero numero: "))#vienen de afuera

#     suma = primer_numero + segundo_numero

#     return suma

# def restar_numeros()->int: #Implentacion de la funcion
#       if (numero == int):
#     primer_numero = int(input("Ingrese el primero numero: "))
#     segundo_numero = int(input("Ingrese el primero numero: "))

#     resta = primer_numero - segundo_numero

#     return resta# devuelvo el resultado,generando independencia

# Funciones bien
# --------------------------------------------------------------------

# pasaje por valor, las variables son inmutables, no cambian su valor

def suma(numero):
    numero = numero + 1
    return numero

a = 3
b = suma(a)

print("Este es el valor de a: ",a)
print("Este es el valor de b: ",a)

def agregar_personas(lista,nombre):
    lista.append(nombre)

lista_nombres = ['marina','pedro']
print(lista_nombres)

agregar_personas(lista_nombres,'juan')
print(lista_nombres)


'''
Esta funcion se encarga de recorrer una lista e imprimir por una caracteristica
Parametro:
Lista: (list) Es una lista de diccionario
Carateristica: (str) es el nombre de la clave del diccionario

Retorna
No retorna nada
'''

def listar_por_caracteristicas(lista:list[dict],caracteristica:str)->None:
    for element in lista:
        print(element[caracteristica])
    
listar_por_caracteristicas(lista_personaje,"nombre")


# Validacion dentro de las funciones

# se usa el if not isinstance(numero, int): no?
# depende el caso, si esperas una lista, y no llega una lista por parametro, o llega vacia, no podes hacer ningun casteo, en ese caso informas que algo salio mal,
#  ya sea mediante un retorno o un print()
# se puede usar eso, pero es mas claro que accedan al tipo de dato usando type() y a eso lo incluyas en una condicion == con el tipo de dato


# el str es inmutable
nombre = "marina"

print(nombre)
print (id(nombre))

nombre = nombre + "cardozo"

# con . agregas metodos

ejemplo = len(nombre)
print(ejemplo)

print(nombre.upper())

print(nombre.lower())

# .capitalize, mayus primera letra y luego minisc

saludo = "       hola    " 
prueba = saludo.strip()
print(prueba) #saca espacios de adelante

prueba = nombre.split()
print(prueba)

prueba_dos = " ".join(prueba)
print(prueba_dos)

#[INICIO:FIN:PASO] Slicing
print(nombre[0])

print(nombre[:6:2])




print(nombre)
print (id(nombre))
