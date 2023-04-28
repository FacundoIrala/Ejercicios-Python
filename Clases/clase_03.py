#Listas

lista = [1,2,3,4,5,6,7,8,9]

print(lista)
print(f"elemento 3: {lista[3]}")
print(lista[0:3])#[DESDE:HASTA] D: INCLUSIVO / H:EXCLUYENTE
print(lista[3:5])

acumulador = 0
contador = 0
for i in range (len(lista)):
    print(lista[i])
    acumulador =  acumulador + lista[i]
    if lista[i] == 5:
        contador += 1

print(acumulador)
print(contador)


lista.append[100] #agregar contenido a la lista

lista.insert[2,999] #se cola un nuevo numero entre ambos valore definidos.Al numero del indice lo corre a la derecha (INDICE, VALOR)

lista.extend([666,777,888]) #agregar mas de un numero a la lista

lista.remove(2) #remueve de la lista el numero definido

print(lista.index(6)) #te informa en que posicion se encuentra el numero

lista = [1,2,3,4]
index = 3
for i in range (index + 1):
    print(f"{i}->{lista[i]}") #imprime los 3 primeros numeros + 1

#con este for puedo remplazar valores de la lista
for i in range (len(lista)):
    print(f"{i+1}->{lista[i]}") 

#con este for la lista es inmutable,no puedo agregar valores
for numero in lista:
    print(numero)

#---------------------------------------------------------------------
#DICCIONARIO
mi_diccionario = {}
mi_diccionario["nombre"] = "Juan"
print(mi_diccionario["nombre"])
mi_diccionario["edad"] = 25
print(mi_diccionario["edad"])

print(mi_diccionario) 

otro_diccionario = {"nombre: ":"luis","edad: ":25}
print(otro_diccionario)

# maneras de mostar el diccionario 

for key in otro_diccionario:
    print(key)

for key in otro_diccionario:
    print(otro_diccionario [key])

for key in otro_diccionario:
    print(f"{key}->{otro_diccionario [key]}")

for valor in otro_diccionario.values():
    print(f"{valor}")

#---------------------------------------------------------------------
#LISTAS PARALELAS
cantidad_alumnos = 3
lista_nombres = []
lista_apellidos = []

for i in range(cantidad_alumnos):
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese apellido: ")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for i in range(cantidad_alumnos):
    print(f"{i+1})nombre: {lista_nombres[i]} - Apellido: {lista_apellidos[i]}")

#----------------------------------------------------------------------------
# Diccionarios dentro de listas


# DEFINIR SET DE DATOS, MAS FACIL
# lista_alumnos = [ #LISTA HARDCODEADA
#     {"nombre":"juan","apellido":"rodriguez","edad":25},
#     {"nombre":"esteba","apellido":"gonzales","edad":53},
#     {"nombre":"azir","apellido":"peralta","edad":33}
# ]

cantidad_alumnos = 3
lista_alumnos = []

#como crearla
# for i in range(cantidad_alumnos):
#     nombre = input("ingrese nombre: ")
#     apellido = input("ingrese apellido: ")
#     edad = int(input("ingrese edad")) #debo parsear los numeros
#     un_alumno = {}
#     un_alumno["nombre"] = nombre
#     un_alumno["apellido"] = apellido
#     un_alumno["edad"] = edad
#     lista_alumnos.append(un_alumno)

# print(lista_alumnos)


for alumno in lista_alumnos:
    apellido = alumno ["apellido"]
    nombre = alumno["nombre"]
    edad = alumno["edad"]
    if edad >  30:
        print(f"{apellido}-{nombre}-{edad}")



for alumno in lista_alumnos:
    edad = alumno["edad"]
    if edad >  30:
        print(f"{alumno['apellido']}-{alumno['nombre']}-{edad}")