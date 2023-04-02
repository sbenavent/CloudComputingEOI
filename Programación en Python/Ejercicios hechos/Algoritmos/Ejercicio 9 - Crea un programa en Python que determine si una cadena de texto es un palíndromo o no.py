#Ejercicio 9:  Crea un programa en Python que determine si una cadena de texto es un palíndromo o no.
print("Bienvenido/a al programa. Este algoritmo determinará si el texto introducido es un palíndromo o no. Tenga en cuenta que no debe introducir tildes ni caracteres especiales.")
specialChar = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"#Lista de caracteres espciales
valMain = ""
while valMain != "SALIR": #Este bucle evita que se cierre el programa sin permiso del usuario.
    
    #Entrada
    val = ""
    while val != True: #Este bucle actúa para comprobar si el texto tiene caracteres especiales. Permite ingresar números, por lo que 1ojo1 es un palíndromo pero 1ojo no. 
        print("Introduzca su texto.")
        texto = input()
        contador = 0
        for i in range(0,len(texto)):
            for j in range(0, len(specialChar)):
                if texto[i] == specialChar[j]:
                    print("No se admiten caracteres especiales")
                    contador = 1
        if contador != 1:
            val = True

    #Proceso
    textoLista = list(texto) #En primer lugar quitamos los espacios con la función remove(x), que quita el primer elemento que coincide con x, pasado en bucle.
    while True:
        try:
            textoLista.remove(" ")
        except:
            break
    textoDep = "".join(textoLista) #Transformamos el texto en str.
    textoDep = textoDep.lower() #Aplicamos la fucnión lower para que todo sea minúsculas
    valores = []
    for character in textoDep: #Pasamos el texto a número aplicándole un valor siguiendo código ascii y añadimos los valores a una lista.
        numero = ord(character) - 96
        valores.append(int(numero))

    contador = 0  #Reusamos contador para no generar más variables
    for k in range(len(valores)-1): #Comparamos el valor con el simétrico y asignamos contador a 1 si en alguno de los puntos son diferentes
        if valores[k] != valores[len(valores)-k-1]:
            contador = 1
            break
  
    #Salida
    if contador == 1:
        print(f"El texto {texto} no es un palíndromo.")
    else:
        print(f"El texto {texto} es un palíndromo")
    print("Para salir del programa escriba SALIR, en caso contrario pulse ENTER")
    valMain = input() 
