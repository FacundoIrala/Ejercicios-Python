# FUNCIONES 2°PARTE

# def potenciar(base,exponente):
#     return  base**exponente


# base = 2
# exponente = 3

# resultado = potenciar(base,exponente)
# print(resultado)

# b = 2
# e = 3

# #no recomendada
# resultado = potenciar(base = e,exponente = b)
# print(resultado)

from data import lista_bzrp
from os import system


def mostrar_lista_temas_views():
    # C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
    for tema in lista_bzrp:    
        print (f"{tema['tema']} - {tema['views']}")


def calcular_maximo(lista:list,clave:str)->int:
    '''
    Brief: Calcula el maximo valor numero en base a una clave
    Parameters: 
        Lista: list -> lista sobre la que voy a hacer la busqueda
        Clave: str  -> La clave con la cual realizo la busqueda en la lista
    Return: un entero que representa  el maximo valor de la clave
    ''' 

    flag_primero = True

    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0): #validacion para q entre
        for tema in lista:
            if flag_primero == True or tema [clave] > maximo:
                maximo = tema[clave]
                flag_primero = False
    
    return maximo


def mostrar_lista_temas(lista:list, clave=None, valor = None)->None:
     if clave is None and valor is None:
        for tema in lista:
           print(f"{lista['title']}")
        else:
            for tema in lista:
                    if tema[clave] == valor:
                        print(f"{tema['title']}")


def buscar_temas_mas_views(lista:list):
    
    maximo_views = calcular_maximo(lista, "views")
    print (f"Cantidad maxima de reproduccion: {maximo_views}") # si hay mas de 2 canciones iguales con misma cantidad de viewers
    mostrar_lista_temas(lista,'views', maximo_views)
   
def buscar_temas_mas_largos(lista:list):
    maximo_len = calcular_maximo(lista,'length')
    print(f"Duracion maxima: {maximo_len}")
    mostrar_lista_temas(lista,'length',maximo_len)





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
            mostrar_lista_temas(lista_bzrp)
        case 2: 
            buscar_temas_mas_largos(lista_bzrp)       
        case 3:
            buscar_temas_mas_views(lista_bzrp)
        case 4:
            buscar_temas_menos_views()
        case 5:
            calcular_promedio()
        case 6:
            print("submenu: a.  ... b. ...")
            funciones
            seguir = False


