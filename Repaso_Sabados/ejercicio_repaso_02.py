animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

'''
1-Generar una sublista de los animes estrenados antes de 1995:
2-Generar una sublista de los animes con más de 1 temporada:
3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:
4-Crear un nuevo diccionario con los nombres y años de estreno de los animes de la lista:
'''

'''
    [
        {'temporadas':1,'nombres':["digimon adventure","evangelion"]}

    ]
'''

nuevo_diccionario = {}
for anime in animes_90s:
    if "temporadas" not in nuevo_diccionario :
        nueva_lista = []
        nueva_lista.append(anime["nombre"])

        nuevo_diccionario["temporadas"] = anime["temporadas"]
        nuevo_diccionario["nombres"] = nueva_lista
    elif nuevo_diccionario["temporadas"] == anime["temporadas"]:
        nuevo_diccionario["nombre"].append(anime["nombre"])
    print(anime)



temporadas = []
mal_normalizado = False

#Obtener informacion de los elementos que se encuentra guardados en la lista

for anime in animes_90s:
    if "temporadas" not in anime:
        mal_normalizado = True

for anime in animes_90s:
    if anime["temporadas"] > 1:
        temporadas.append(anime["nombre"])

print(temporadas)



#hacer una cantidad de vuelta de forma determinada, ej 3 o 10 veces, usar rang
for i in range(10):
    print(i)

#Recorrer la lista contando la cantidad de elentos que tiene esa lista
range(len(animes_90s))

for indice in range(len(animes_90s)):
    print(animes_90s[indice]["nombre"]) #manera vieja

for elemento_anime in animes_90s:
    print(anime["nombre"]) # manera correcta