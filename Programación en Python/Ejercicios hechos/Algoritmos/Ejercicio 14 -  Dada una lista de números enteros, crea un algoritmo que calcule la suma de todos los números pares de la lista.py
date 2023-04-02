#Ejercicio 14:  Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.
print("Bienvenido/a al programa. Este algoritmo calculará la suma de todos los números pares de una lista de números")
valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Para continuar, introduzca números en su lista. Cuando desee parar, escriba STOP")
    lista= []
    while True:
        print("Introduzca un número entero.")
        num = input()
        if num == "STOP":
            break
        else:
            try:
                lista.append(int(num))
            except Exception as error:
                print(f"Ha ocurrido un error {error}. Solo se admiten numeros enteros")

    #Proceso
    suma = int(0)
    print(f"Su lista de números es {lista}")
    listaPar = lista
    for i in range (0, len(lista)):
        if lista[i] != 0 and lista[i]%2 != 0:
            listaPar[i] = ""
        else:
            suma = suma + listaPar[i]

    #Salida
    print(f"Dada la lista de números introducida cuyos elementos pares son {listaPar}, la suma de dichos elementos es: {suma}.")
    print("Para salir escriba SALIR. Si desea seguir usando el programa pulse ENTER.")
    valMain = input()