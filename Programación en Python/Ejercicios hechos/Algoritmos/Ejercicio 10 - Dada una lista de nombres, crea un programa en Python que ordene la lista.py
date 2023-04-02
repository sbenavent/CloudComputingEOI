#Ejercicio 10: Dada una lista de nombres, crea un programa en Python que ordene la lista alfabéticamente.
print("Bienvenido/a. Este algoritmo ordenará una lista de palabras alfabéticamente.")
valMain = ""
while valMain != "SALIR":

    #Entrada
    lista = []
    palabra = ""
    while True:
        print("Introduzca una palabra para la lista.Cuando quiera parar escriba STOP")
        palabra = input()
        if palabra == "STOP":
            break
        else:
            lista.append(palabra)

    #Proceso
    listaOrd = sorted(lista)

    #Salida
    print(f"Ha introducido las siguientes palabras {lista} que ordenadas alfabéticamente quedan como {listaOrd}")
    valMain = input("Escriba SALIR para salir.")

