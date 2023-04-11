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
        contador = 0
        for i in texto1:
            if any(i == j for j in specialChar) == True:
                print("No se admiten caracteres especiales")
                contador = 1
                break
            if i.isnumeric() == True:
                print("No se admiten números.")
                contador = 1
                break
        if contador == 0:
            break

    print("Introduzca el segundo texto.")
    while True:
        texto2 = input()
        contador = 0
        for i in texto2:
            if any(i == j for j in specialChar) == True:
                print("No se admiten caracteres especiales")
                contador = 1
                break
            if i.isnumeric() == True:
                print("No se admiten números.")
                contador = 1
                break
        if contador == 0:
            break

    #Proceso

        #Subalgoritmo para pasarlo todo a minusculas. Para poder aplicar lower debe ser de tipo str por lo que hay que hacer join y pasarlo a lista de nuevo.
    textoDep1 = texto1.lower().replace(" ", "")
    textoDep2 = texto2.lower().replace(" ", "")

        #Comparamos letra por letra entre las dos cadenas. Si encuentra igualdades, el elemento duplicado pasa a ser "". 
        #Luego se revisa si algún elemento es diferente de "". 
        #Para ello debe de haber máxima igualdad. 
    
    resultados = list(textoDep2) #Necesario que sea lista para poder reemplazar
    for i in range (0,len(textoDep1)):
        for j in range (0,len(resultados)):
            if textoDep1[i] == resultados[j]:
                resultados[j] = ""
                break

    contador = 0
    if len(textoDep1) != len(textoDep2):
        contador = 1
    elif any(char != "" for char in resultados) == True:
        contador = 1

    #Salida
    if contador == 0:
        print(f"Los textos {texto1} y {texto2} son anagramas.")
    else:
        print(f"Los textos {texto1} y {texto2} no son anagramas.")
    print("Si desea salir introduzca SALIR. En caso contrario, pulse ENTER.")
    valMain = input()