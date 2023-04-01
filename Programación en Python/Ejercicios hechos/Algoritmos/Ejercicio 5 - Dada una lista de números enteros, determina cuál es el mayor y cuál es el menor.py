#Ejercicio 5: Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.
print("Bienvenido/a al programa. Este script ordena una serie de números enteros y te da el mayor y el menor de ellos. Por favor, siga las instrucciones para continuar")
valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Por favor, introduzca una serie de números enteros. Cuando quiera parar, introduzca STOP .")
    cadena = []
    while True:
        try:
            print("Introduzca un número para añadirlo a la lista. Recuerde que parará cuando escriba STOP.")
            numero = input()
            if numero == "STOP":
                break
            else:
                int(numero)
                cadena.append(int(numero))
        except Exception as error:
            print(f"Se ha producido un error {error}. Por favor introduzca únicamente números enteros. ")

    print(f"La lista que ha introducido es {cadena}")      

    #Proceso
    cadenaOrdenada = sorted(cadena)

    #Salida
    try:
        print(f"Su lista de números ordenados es {cadenaOrdenada}, el menor es {cadenaOrdenada[0]} y el mayor es {cadenaOrdenada[len(cadenaOrdenada)-1]}")
    except  Exception as error2:
        print("No ha introducido nada.")
    print("Escriba SALIR para salir del programa o pulse ENTER para reiniciarlo.")
    valMain = input()

