''''La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (&quot;barbijo&quot;, &quot;jabón&quot; o &quot;alcohol&quot;)
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.'''

from os import  system #importo de la biblioteca 
system("cls") # clear para la terminal


opcion = input(" Ingrese barbijo, jabon o alcohol: ")
while( opcion!= "barbijo" and opcion!="jabon" and opcion!="alcohol" ):
    opcion = input (("Error, reingrese elija barbijo, jabon o alcohol"))


precio = float (input("Ingrese precio: "))
cantidadUnidades = int (input("Ingrese cantidadUnidades: "))
marca = (input("Ingrese marca: "))
fabricante = (input("Ingrese fabricante: "))

print("opcion: " ,opcion)
print("precio:",precio)
print("cantidadUnidades:",cantidadUnidades)
print("marca: " ,marca)
print("fabricante: ",fabricante)


