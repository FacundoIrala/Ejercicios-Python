# {lista_bzrp=[    
#     {
#         'title': 'QUEVEDO || BZRP Music Sessions #52',
#         'views': 227192970,
#         'length': 204,
#         'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
#         'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
#         'date': '2022-07-06 00:00:00'
#      }, 
#      {
#         'title': 'VILLANO ANTILLANO || BZRP Music Sessions #51',
#         'views': 112947399, 
#         'length': 188, 
#         'img_url': 'https://i.ytimg.com/vi/wvz97-lNPH8/sddefault.jpg', 
#         'url': 'https://youtube.com/watch?v=wvz97-lNPH8', 
#         'date': '2022-06-08 00:00:00'
#      }]}

from data import lista_bzrp
from os import system


# print(type(lista_bzrp))
# print(type(lista_bzrp[0]))


# B. Recorrer la lista imprimiendo por consola el titulo de cada video
for tema in lista_bzrp:
    print (tema["title"])