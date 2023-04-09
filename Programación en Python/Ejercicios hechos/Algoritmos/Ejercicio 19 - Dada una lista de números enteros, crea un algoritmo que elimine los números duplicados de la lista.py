#Ejercicio 19: Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

print("Bienvenido/a al programa. Este algoritmo eliminará los duplicados de una lista de números enteros. Siga las instrucciones para continuar.")
valMain = ""
while valMain != "SALIR":
    #Entrada
    lista = []
    while True:
        print("Introduzca un número para la lista. Cuando desee parar, introduzca STOP.")
        numero = input()
        if numero != "STOP":
            try:
                lista.append(int(numero))
            except  Exception as error:
                print(f"Se ha producido un error {error}. Solo se admiten números enteros.")
        else:
            break

    #Proceso
    print(f"La lista de números introducidos es {lista}.")
    listaDup = lista
    for i in range (0,len(listaDup)):
        for j in range (i+1, len(listaDup)):
            if listaDup[i] == listaDup[j]:
                listaDup[j] = ""
    
    while True:
        try:
            listaDup.remove("")
        except:
            break

    #Salida
    print(f"La lista de números sin elementos repetidos es {listaDup}.")
    print("Si desea salir introduzca SALIR. En caso contrario pulse ENTER.")
    valMain = input()

