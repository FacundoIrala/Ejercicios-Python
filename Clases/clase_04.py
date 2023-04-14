

from data import lista_bzrp
from os import system

def mostrar_lista_temas():
    # B. Recorrer la lista imprimiendo por consola el titulo de cada video
    for i in range(len(lista_bzrp)):
        print(f"{lista_bzrp[i]['title']}")  

def mostrar_lista_temas_views():
    # C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
    for tema in lista_bzrp:    
        print (f"{tema['tema']} - {tema['views']}")

def buscar_temas_mas_views():
    # D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones
    flag_primero = True

    for tema in lista_bzrp:
        if flag_primero == True or tema ['views'] > maximo_views:
            maximo_views = tema["views"]
            flag_primero = False

    print (f"Cantidad maxima de reproduccion: {maximo_views}") # si hay mas de 2 canciones iguales con misma cantidad de viewers
    for tema in lista_bzrp:
            if tema["views"] == maximo_views:
                print(f"{tema['title']}")

def buscar_temas_menos_views():
    # E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones (MÍNIMO)
    for tema in lista_bzrp:
        if flag_primero == True or  tema["views"] < minima_views:
            minima_views = tema ["views"]
            flag_primero = False
        
        print (f"Cantidad minima de reproduccion: {minima_views}") # si hay mas de 2 canciones iguales con misma cantidad de viewers
        for tema in lista_bzrp:
            if tema["views"] == minima_views:
                print(f"{tema['title']}")

def calcular_promedio():
    # F. Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)
    acumulador_views = 0
    for tema in lista_bzrp:
        acumulador_views += tema["views"]

    print(f"Sumatoria  de reproducciones: {acumulador_views}")

    # G. Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)

    contar_temas = len(lista_bzrp)

    promedio_views = acumulador_views / contar_temas

    print(f"El promedio de vistas es: {promedio_views}")

def mostrar_menu():
    for opcion in menu:
        print(opcion)


menu = ["1.Mostrar temas", "2.Mostrar temas con vistas","3.Mostrar temas mas vistas","4.Mostrar temas con  menos views","5.Mostrar promedio reproducciones","6.Salir"]

seguir = True
while seguir == True:
    system("cls") # eliminar buffer
    mostrar_menu()


    respuesta = int(input("Ingrese una opcion"))
    match respuesta:
        case 1:
            mostrar_lista_temas()
            #for tema in lista_bzrp:
                #print (tema["title"]) 
        case 2: 
            mostrar_lista_temas_views()
        case 3:
            buscar_temas_mas_views()
        case 4:
            buscar_temas_menos_views()
        case 5:
            calcular_promedio()
        case 6:
            seguir = False


# print(type(lista_bzrp))
# print(type(lista_bzrp[0]))




# otra manera
#  contar_temas = 0

#     for tema in lista_bzrp:
#         contar_temas += 1


# contar_temas = len(lista_bzrp) #no espepecifica algo en particular, es generico


# H. Informar cual es el Título del vídeo asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO, ACUMULADOR y PROMEDIO)
