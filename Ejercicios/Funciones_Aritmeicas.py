from data_stark import lista_personajes

def mostrar_lista_superheroes():
     #B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for i in range(len(lista_personajes)):
        print(f"{lista_personajes[i]['nombre']}")  

def mostrar_lista_superheroes_altura():
     #C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    for nombre in lista_personajes:    
        print (f"{nombre['nombre']} - {nombre['altura']}")

def mostrar_superheroe_mas_alto():
     #D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

    flag_primero = True

    for personaje in lista_personajes:
        if flag_primero == True or float(personaje ['altura'])> maximo_altura:
            maximo_altura = float(personaje["altura"])
            nombre_max_altura = personaje ['nombre']
            flag_primero = False

    print (f"La altura maxima del superheroe: {maximo_altura} y su nombre es: {nombre_max_altura}") 
    for personaje in lista_personajes:
            if float(personaje["altura"]) == maximo_altura:
                print(f"{personaje['nombre']}")

def mostrar_superheroe_menos_alto():
     #E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_primero = True

    for personaje in lista_personajes:
        if flag_primero == True or float(personaje ['altura']) < minima_altura:
            minima_altura = float(personaje["altura"])
            nombre_max_altura = personaje ['nombre']
            flag_primero = False

    print (f"La altura minima del superheroe: {minima_altura} y su nombre es: {nombre_max_altura}") 

    for personaje in lista_personajes:
            if float(personaje["altura"]) == minima_altura:
                print(f"{personaje['nombre']}")

def calcular_promedio_altura_superheroes():
     #F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)

    acumulador_altura = 0
    for tema in lista_personajes:
        acumulador_altura += float(tema["altura"])

    contar_heroes = len(lista_personajes)

    promedio_altura = (float(acumulador_altura)) / contar_heroes

    print(f"El promedio de altura de los superheroes es: {promedio_altura}")

def mostrar_superheroe_mas_peso():
     # H. Calcular e informar cual es el superhéroe más y menos pesado.
    flag_primero = True

    for personaje in lista_personajes:
        if flag_primero == True or float(personaje ['peso'])> mayor_peso:
            mayor_peso = float(personaje["peso"])
            nombre_max_altura = personaje ['nombre']
            flag_primero = False

    print (f"El peso del superheroes mas pesado es: {mayor_peso} y su nombre es: {nombre_max_altura}") 

    for personaje in lista_personajes:
            if float(personaje["peso"]) == mayor_peso:
                print(f"{personaje['nombre']}")

def mostrar_superheroe_menos_peso():
     # H. Calcular e informar cual es el superhéroe más y menos pesado.
    flag_primero = True
    
    for personaje in lista_personajes:
        if flag_primero == True or float(personaje ['peso']) < menor_peso:
            menor_peso = float(personaje["peso"])
            nombre_max_altura = personaje ['nombre']
            flag_primero = False

    print (f"El peso del superheroes menos pesado es: {menor_peso} y su nombre es: {nombre_max_altura}") 

    for personaje in lista_personajes:
            if float(personaje["peso"]) == menor_peso:
                print(f"{personaje['nombre']}")


def mostrar_menu():
    for opcion in menu:
        print(opcion)
        