#2 FORMAS DE IF


color=input("Ingrese color")
if color == "azul":
    print("Es azul")
elif color == "verde":
     print("Es verde")
elif color == "rojo":
     print("Es rojo")
else:
     print("Es otro color")


if color == "azul":
    print("Es azul")
else:
     if color == "verde":
          print("Es azul")
     else:
          if color == "rojo":
                print("Es rojo")
          else:
               print("no es ninguno de estos")





#SWTICH PYTHON

color = "azul"

match color:   
    case  "azul":
        print("Es azul")
    case  "verde":
        print("Es verde")
    case "rojo":
        print("Es rojo")
    case other: #o mimsmo case_
        print("Es otro color")





# CICLO WHILE

acumulador = 0
seguir = True
while seguir: 
    numero = int(input("Ingrese un numero"))
    acumulador+=numero

    seguir = input ("Desea continuar?")
    if seguir != "si":
         seguir = False

print(f"Acumulado: {acumulador}")





# CICLO REPETITIVO DO WHILE Y ACUMULADOR

acumulador = 0

while True:#entra de una x tener el true
     numero =  int(input("ingrese numero: "))
     acumulador += numero

     seguir = input ("desea continuar")
     if seguir != "si":
          break
     print(f"acumulado: {acumulador}") #sirve para anidar





#LISTAS

lista_nombres = ["luis", "nico", "pepe"]
lista_nombres.reverse()
for nombre in lista_nombres:#foreach
     print (nombre)