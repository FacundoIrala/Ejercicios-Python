'''
3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
cantidad de carreras ganadas (no pueden ser números negativos)
número del vehículo (no puede ser un número negativo)
se necesita saber:
*Nacionalidad del piloto más joven.
*Cantidad de vehículos con número par.
*Nombre del piloto con menos victorias y el número de auto impar.
*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
*Nombre del piloto más joven con más victorias.
*Nacionalidad del piloto más veterano con menos victorias.
*Promedio de edad de los pilotos que tiene un vehículo con número par.
'''

# print( "La edad sumada es {0}".format(edad) ) otra forma de mostrar
# print(hex(id(numero_uno)))muestra el valor de la memoria en hexa

seguir = True
flag = 0
flagVictorias = 0

while seguir:

    nombre = input ("Ingrese nombre del piloto")

    edad = int(input("Ingrese edad "))
    while (edad > 18):
        edad = input("Eror, reingrese su edad mayor a 18")

    nacionalidad = input("Ingrese argentino, ingles, frances, brasilero, eeuu")
    while( nacionalidad!= "argentino" and nacionalidad!="ingles" and nacionalidad!="frances" and nacionalidad!="brasilero" and nacionalidad!="eeuu" ):
        nacionalidad = input (("Error, elija  Ingrese argentino, ingles, frances, brasilero, eeuu"))

    cantidadCarreras = int(input("Ingrese carreras ganadas "))
    while (cantidadCarreras > 0 ):
        cantidadCarreras = input("Eror, reingrese carreras ganadas mayor a 0")
    
    numeroVehiculo = int(input("Ingrese carreras ganadas "))
    while (numeroVehiculo > 0 ):
        numeroVehiculo = input("Eror, reingrese numero del vehiculo mayor a 0")
    
    if flag == 0 or edad < edadminima and carrerasMasVictorias > cantidadCarreras :
        edadminima = edad
	    nacionalidadJoven = nacionalidad
        flag = 1
        carrerasMasVictorias = cantidadCarreras
        nombrePilotoMasVictorias = nombre 

    
    if numeroVehiculo / 2 == 0:
        contadorVehiculosPar = contadorVehiculosPar + 1

    if flagVictorias == 0 and cantidadCarreras < carrerasMenosVictorias and numeroVehiculo / 2 != 0 :
        carrerasMenosVictorias = cantidadCarreras
        nombrePilotoMenosVictorias = nombre
        flagVictorias = 1
    
    if edad > 25 and numeroVehiculo / 2 != 0:
        contadorPilotosMayores = contadorPilotosMayores + 1 
    


        