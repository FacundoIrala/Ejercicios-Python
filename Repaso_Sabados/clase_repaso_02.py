#Python es un lenguaje de alto nivel
#Las listas en python puede contener muchos datos
#Es algo indexeado, osea que se puede acceder x los indices
#Se pueden modificar (mutabilidad), ordenar, agregar y borrar elementos,
#Que sea inmuteable es que todo lo que agregamos a la lista, es que se va a manetener en la misma direccion de memoria
#variable_lista[]
#variable = list()

mi_lista = [1,2,"marina",['a','b','c'],True]

print("Mi lista: ")
print(mi_lista[-1])#cuando declaramos con negativo empieza desde atras para adelante

if type(mi_lista[3]) == list:  #corraboramos q sea lista y ejecutamos la condicion
    sub_lista = mi_lista [3][1]
    print(sub_lista)
else:
    print("te equivocaste")

mi_lista.append("hola") #buscar Append agrega un elemento a lista, para agregar a una lista

#-------------------------------------------------------------------------
#incio:final:paso
print(mi_lista[2:4]) #la 4 es no inclusive
print(mi_lista[::2]) #agrega todo menos el indice 2
print(mi_lista[:-2]) #al no tenr nada al principio ,empieza desde 0,te imprime todos menos el marcado


notas_1  = [6,7,8]
notas_2 = [4,5,6]
alumnos = ['pepe','juan','facu']


#recorro 3 listas al mismo tiempo por su indice, para ello usamos i
for i in range (3):
    print(f"Alumno: {alumnos[i]} Primera nota: {notas_1[i]}, Segunda nota: {notas_2[i]}")

#-----------------------------------------------------------------------------------
#diccionario , compuesto x clave y valor
#se diferencia de la lista xq el diccionario se inicializa con llaves {}
#el diccionario contiene valores y no indices

mi_dic = {"nombre":"marina","apellido":"cardozo"}
mi_dic = {"nombre":"marina","apellido":["cardozo","pagura"]}

print(mi_dic["nombre"])
print(mi_dic["apellido"])

#agregar nueva info

mi_dic["edad"] = 21

print(mi_dic)

mi_dic["edad"] = 15
print(mi_dic)

if "edad" in mi_dic: #el in es si existe
    print (True)
else:
    print (False)

del mi_dic["edad"]
print(mi_dic)

mi_dic["apellido"] = ["hola"]
print(mi_dic)

ingreso = input("ingrese el campo q desea modificar:  nombre -edad -apellido")

if ingreso in mi_dic:
    print(True)
else:
    print(False)
  
#----------------------------------------------------------------------------------

#tupla ,va entre parantesis
#lista ordenada, podemos acceder a cada elemento
#es inmutable = performance de memoria, cambia de memoria
#es inmodificable
#generalmente se usa para desclarar constantes

mi_tupla = (1,'2',True)

print(type(mi_tupla))
print(mi_tupla)

#-----------------------------------------------------------------------------------

#set
#es una coleccion que no se encuentra elementos repetidos
#es inmutable

mi_set = set([1,2,2,3,4,4,5])

print(type(mi_set))
print(mi_set)#elimina los numeros repetidos

Un casteo a string de todos los elementos para despues ir sacando los repetidos uno a uno
