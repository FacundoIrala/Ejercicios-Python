'''Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”'''


while True:

	numero = int(input("Ingrese numero entre 1 y 8: "))
	while (numero < 0 or numero > 150):
		numero = input("Eror, reingrese numero entre 1 y 8")


	match numero:   
		case  1:
			print("Usted ingreso a la 1° regla de estilo: ¿Cuál es el sentido? ")
			print("Resulta importante escribir código que no sólo funcione, sino que además pueda ser leído con facilidad.")
		case 2:
			print("Usted ingreso a la 2° regla de estilo: ¿Qué es PEP? ")
			print("Python Enhancement Proposal es un documento que proporciona información a la comunidad de Python, o que describe una nueva característica.")
		case 3:
			print("Usted ingreso a la 3° regla de estilo: ¿Qué es PEP8? ")
			print("Es un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.")
		case 4:
			print("Usted ingreso a la 4° regla de estilo: Indentado ")
			print("Python no usa {} para designar bloques de código como otros lenguajes de programación, sino que usa bloques identados para indicar que un determinado bloque de código pertenece a por ejemplo un if.")
		case 5:
			print("Usted ingreso a la 5° regla de estilo: Tamaño máximo linea ")
			print("Se recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer scroll a la derecha.")
		case 6:
			print("Usted ingreso a la 6° regla de estilo: Líneas en blanco ")
			print("El uso de espacios en blanco mejora la legibilidad del código, y es por lo que la PEP8 indica dónde debemos usar espacios y dónde no.")
		case 7:
			print("Usted ingreso a la 7° regla de estilo: Comentarios ")
			print("Evitar comentarios poco descriptivos que no  aporten nada más allá de lo que ya se ve a simple vista.")
		case 8:
			print("Usted ingreso a la 8° regla de estilo: Nombres ")
			print("Funciones: Uso de snake_case, letras en minúscula separadas por guión bajo: mi_funcion.")
			print("Variables: Al igual que las funciones: variable, mi_variable.")
			print("Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.")
			print("Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo.")
			print("Constantes: Nombrarlas usando mayúsculas y separadas por guión bajas: UNA_CONSTANTE")
			print("Módulos: Igual que las funciones: modulo.py, mi_modulo.py.")

		case other: #o mimsmo case_
			print("Error, regla de estilo inexistente")

		
	seguir = input ("Desea ingresar nuevamente otro numero? Indique si o no ")
	if seguir != "si":
    		break