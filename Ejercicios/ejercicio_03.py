'''Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)'''




contadorNacho = 0
contadorJulieta = 0
contadorMarcos = 0
acumuladorFemenino = 0
contadorFemenino = 0
seguir = True
contadorAntiMarcos = 0
flag = 0
edadMinima = 0


while seguir:

    nombre= input("Ingrese nombre: ")

    edad = int(input("Ingrese edad: "))
    while (int(edad < 13)):
        edad = input("Eror, reingrese su edad mayor a 13")

    genero = input(" Ingrese genero masculino , femenino o otro: ")
    while( genero!= "masculino" and genero!="femenino" and genero!="otro" ):
        genero = input (("Error, elija  masculino o femenino o otro"))

    opcion = input(" Ingrese nombre participante Nacho, Julieta o Marcos: ")
    while( opcion!= "Nacho" and opcion!="Julieta" and opcion!="Marcos" ):
        opcion = input (("Error, elija  Nacho, Julieta o Marcos"))
    
    match opcion:   
        case  "Nacho":
            contadorNacho = contadorNacho + 1
        case  "Julieta":
            contadorJulieta = contadorJulieta + 1
        case "Marcos":
            contadorMarcos = contadorMarcos + 1   
        case other: #o mimsmo case_
            print("Error")

    if(genero == "femenino"):
        acumuladorFemenino = acumuladorFemenino + edad
        contadorFemenino = contadorFemenino + 1
    else:
        promedioMujeres = 0

    
    if genero == "masculino" and edad >= 25 or edad <= 40 and opcion == "Nacho" and opcion == "Julieta":
        contadorAntiMarcos = contadorAntiMarcos + 1
   
    if(flag == 0 or opcion == "Nacho" and edad < edadMinima):
        edadMinima = edad
	    
        nombreJoven = nombre
	    
        flag = 1
  
    seguir = input ("Desea continuar?")
    if seguir != "si":
            seguir = False

if contadorFemenino >= 1:
    promedioMujeres= acumuladorFemenino / contadorFemenino
            
contadorGeneral = contadorNacho + contadorJulieta + contadorMarcos

porcentajeNacho = (contadorNacho * 100 ) / contadorGeneral
porcentajeJulieta= (contadorJulieta * 100 ) / contadorGeneral
porcentajeMarcos = (contadorMarcos * 100 ) / contadorGeneral



if contadorNacho > contadorJulieta and contadorNacho > contadorMarcos:
    participanteMasAtendido = "Nacho"
elif contadorJulieta > contadorNacho and contadorJulieta > contadorMarcos:
    participanteMasAtendido = "Julieta"
else:
    participanteMasAtendido = "Marcos"


#poner un algoritmo para posiblidad de empate?

print("El promedio de edad de las votantes de género femenino: ",promedioMujeres)
print("La cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta fue de: ",contadorAntiMarcos)
print("Nombre del votante más joven que votó a Nacho es: ", nombreJoven)
print("El participante Nacho obtuvo un porcentaje de votos de: ", porcentajeNacho," %")
print("El participante Julieta obtuvo un porcentaje de votos de: ",porcentajeJulieta," %" )
print("El participante Marcos obtuvo un porcentaje de votos de: ",porcentajeMarcos," %" )
print("El nombre del participante que gano el  reality es: ",participanteMasAtendido )

