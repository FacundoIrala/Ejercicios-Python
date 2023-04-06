'''La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio (acumular) por kilo (contador) en total.'''

seguir = True

while seguir:

    peso = int(input("Ingrese peso entre 10 y 100 kilos "))
    while (peso > 10 or peso < 100):
        peso = input("Eror, reingrese peso entre 10 y 100 kilos")
    
    precio = int(input("Ingrese precio por kilo "))
    while (precio > 0):
        precio = input("Eror, precio por kilo")
        contadorKilos = contadorKilos + 1
    
    variedad = input(" Ingrese variedad, vegetal, animal o mezcla")
    while( variedad!= "vegetal" and variedad!="animal" and variedad!="mezcla" ):
        variedad = input (("Error, Ingrese variedad, vegetal, animal o mezcla"))

    
    totalBruto = peso * precio

    if(peso > 100):
        descuento = (totalBruto * 15) / 100
        totalConDescuento = totalBruto - descuento
    elif(peso > 300):
        descuento = (totalBruto * 25) / 100
        totalConDescuento = totalBruto - descuento

    

    seguir = input ("Desea continuar?")
    if seguir != "si":
            seguir = False
    
    