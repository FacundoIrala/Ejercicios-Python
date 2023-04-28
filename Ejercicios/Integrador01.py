from data_stark import lista_personajes

# def mostrar_lista_superheroes_masculino(lista_personajes):
#     masculinos =[]
#     for heroe in lista_personajes:
#         if heroe["genero"] == "M":
#             masculinos.append(heroe["nombre"])
#     return masculinos

# print (mostrar_lista_superheroes_masculino(lista_personajes))



# def mostrar_lista_superheroes_femeninoo(lista_personajes):
#     femenino =[]
#     for heroe in lista_personajes:
#         if heroe["genero"] == "M":
#             femenino.append(heroe["nombre"])
#     return femenino
#     # print(f"nombre: {heroe['nombre']}")  

#solo obtiene personajes masculinos, debemos hacer q la  funcion obtenga tanto masculino como femenino
# def obtener_genero_personaje(lista_p:list):
#         lista_masculinos = []

#         for personaje in lista_p:
#              if personaje["genero"] == "M":
#                   lista_masculinos.append(personaje)

#         return lista_masculinos

# lista_m = obtener_genero_personaje(lista_personajes)
# mostrar_heroes(lista_m)




# mostrar_lista(list:list):
# 	for heroe in lista_heroes:
# 		print(f"Nombre: {heroe['heroe']}")


# nombres = funcion nombre m (lista personajes)
# mostar_lista(nombres)


def mostrar_heroes(lista_p:list):
     for personaje in lista_p:
          print(personaje["nombre"],"-",personaje["genero"])

#corecta
def obtener_personajes_por_genero(lista_personajes,genero):
    lista_femenino_masculino =[]
    for heroe in lista_personajes:
        if heroe["genero"] == genero:
            lista_femenino_masculino.append(heroe)# solo heroe
        
    return lista_femenino_masculino




def mostrar_superheroe_mas_alto(lista_p:list):
     #D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

    flag_primero = True

    for personaje in lista_p:
        if flag_primero == True or float(personaje ['altura'])> maximo_altura:
            maximo_altura = float(personaje["altura"])
            nombre_max_altura = personaje ['nombre']
            flag_primero = False

    return nombre_max_altura
    print (f"La altura maxima del superheroe: {maximo_altura} y su nombre es: {nombre_max_altura}") 
    for personaje in lista_personajes:
            if float(personaje["altura"]) == maximo_altura:
                print(f"{personaje['nombre']}")
    


lista_masculino_alto: list = obtener_personajes_por_genero(lista_personajes,"M")
print(mostrar_superheroe_mas_alto(lista_masculino_alto))

lista_femenino_alto: list = obtener_personajes_por_genero(lista_personajes,"F")
print(mostrar_superheroe_mas_alto(lista_femenino_alto))


def mostrar_superheroe_menos_alto(lista_p:list):
     #E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_primero = True

    for personaje in lista_p:
        if flag_primero == True or float(personaje ['altura']) < minima_altura:
            minima_altura = float(personaje["altura"])
            nombre_menor_altura = personaje ['nombre']
            flag_primero = False

    return nombre_menor_altura

    print (f"La altura minima del superheroe: {minima_altura} y su nombre es: {nombre_max_altura}") 

    for personaje in lista_personajes:
            if float(personaje["altura"]) == minima_altura:
                print(f"{personaje['nombre']}")

lista_masculino_bajo: list = obtener_personajes_por_genero(lista_personajes,"M")
print(mostrar_superheroe_menos_alto(lista_masculino_bajo))

lista_femenina_bajo: list = obtener_personajes_por_genero(lista_personajes,"F")
print(mostrar_superheroe_menos_alto(lista_femenina_bajo))




# def mostrar_menu():
#     for opcion in menu:
#         print(opcion)
        

# menu =  [
#         "1.imprimir nombre superheroe de genero Masculino: "
#         "\n2.imprimir nombre superheroe de genero Femenino: "
#         "\n3.imprimir superheroe mas alto genero Masculino: "

        
        
#         ]

# seguir = True

# while seguir == True:
#     mostrar_menu()
     
#     respuesta = int(input("Ingrese una opcion"))

#     match respuesta:
#         case 1:
#             obtener_personajes_por_genero(lista_personajes,"M")
#         case 2:
#             obtener_personajes_por_genero(lista_personajes,"F")
#         case 3:
#             pass



# # 1. Determinar cuantos colores de hoy (lista de colores  y un set)
# # 2. Me cuente los superheroes

# '''
# BLUE = 7 super
# Green = 5 super
# Yellow = 2 super
# '''
# # PUNTO J
# def determinar_colores_ojos(lista_heroes:list):
#     lista_colores = []
#     # contador  = 0 aca esta mal
#     for personaje in  lista_heroes:
#         lista_colores.append(personaje["color_ojos"])

#     # print(lista_colores)

#     for color in set(lista_colores):
#         contador = contar_colores_ojos((lista_heroes,color))

#         print("{0}: ??? Superheroes".format(color,contador))

# def contar_colores_ojos(lista_heroes:list,color_ojo,clave:str,valor):
#     contador = 0

#     for personaje in lista_heroes:
#             if color_ojo == personaje["color_ojos"]:
#                 #Contarlos
#                 contador +=1
#     return contador

# determinar_colores_ojos(set(lista_personajes))

# # Funcion generica, optima y recomendada

# def contar_elementos(lista:list,color_ojo,clave:str,valor):
#     contador = 0

#     for elemento in lista:
#             if valor == elemento[clave]:
#                 #Contarlos
#                 contador +=1
#     return contador

# cantidad_personajes_intelegencia = contar_elementos(lista_personajes,"inteligencia","good")
# print("la cantidad de personajes con la inteligencia good es de: {0}".format(cantidad_personajes_intelegencia))

# # es lo mismo si invertimos la condicion
# # no hace falta definir str al valor, ya que puede cualquier tipo de dato
 
