#Ejercicio 18: Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto

specialChar = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" #Lista de caracteres especiales
print("Bienenvido/a al programa. Este algoritmo determinará si dos textos son anagramas. No se admiten números o caracteres especiales.")
print("El algoritmo no es sensible a las mayúsculas o los espacios, pero sí a las tildes. Se recomienda no usar acentos.")

valMain = ""
while valMain != "SALIR":
    #Entrada. Los bucles de entrada solo permiten que seguir si el texto no tiene caracteres espciales ni números.
    print("Introduzca el primer texto.")
    while True:
        texto1 = input()
        textoLista1 = list(texto1)
        contador = 0
        for i in range (0, len(textoLista1)):
            if any(textoLista1[i] == specialChar[j] for j in range(0,len(specialChar))) == True:
                print("No se admiten caracteres especiales")
                contador = 1
                break
            if textoLista1[i].isnumeric() == True:
                print("No se admiten números.")
                contador = 1
                break
        if contador == 0:
            break

    print("Introduzca el segundo texto.")
    while True:
        texto2 = input()
        textoLista2 = list(texto2)
        contador = 0
        for i in range (0, len(textoLista2)):
            if any(textoLista2[i] == specialChar[j] for j in range(0,len(specialChar))) == True:
                print("No se admiten caracteres especiales")
                contador = 1
                break
            if textoLista2[i].isnumeric() == True:
                print("No se admiten números.")
                contador = 1
                break
        if contador == 0:
            break

    #Proceso

        #Subalgoritmo para remover espacios en blanco
    while True:
            try:
                textoLista1.remove(" ")
            except:
                break

    while True:
            try:
                textoLista2.remove(" ")
            except:
                break

        #Subalgoritmo para pasarlo todo a minusculas. Para poder aplicar lower debe ser de tipo str por lo que hay que hacer join y pasarlo a lista de nuevo.
    textoDep1 = "".join(textoLista1)
    textoDep1 = textoDep1.lower()
    textoDep1 = list(textoDep1)

    textoDep2 = "".join(textoLista2)
    textoDep2 = textoDep2.lower()
    textoDep2 = list(textoDep2)

        #Comparamos letra por letra entre las dos cadenas. Si encuentra igualdades, el elemento duplicado pasa a ser "". 
        #Luego se revisa si algún elemento es diferente de "". 
        #Para ello debe de haber máxima igualdad. 
    for i in range (0, len(textoLista1)):
        for j in range (0, len(textoLista2)):
            if textoDep1[i] == textoDep2[j]:
                textoDep2[j] = ""
                break
    contador = 0
    for i in range (0, len(textoDep2)):
        if textoDep2[i] != "":
            contador = contador+1

    #Salida
    if contador == 0:
        print(f"Los textos {texto1} y {texto2} son anagramas.")
    else:
        print(f"Los textos {texto1} y {texto2} no son anagramas.")
    print("Si desea salir introduzca SALIR. En caso contrario, pulse ENTER.")
    valMain = input()