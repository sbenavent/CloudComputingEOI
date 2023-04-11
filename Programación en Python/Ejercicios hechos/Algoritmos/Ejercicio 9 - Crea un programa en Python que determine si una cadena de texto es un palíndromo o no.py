#Ejercicio 9:  Crea un programa en Python que determine si una cadena de texto es un palíndromo o no.
print("Bienvenido/a al programa. Este algoritmo determinará si el texto introducido es un palíndromo o no. Tenga en cuenta que no debe introducir tildes ni caracteres especiales.")
specialChar = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"#Lista de caracteres espciales
valMain = ""
while valMain != "SALIR": #Este bucle evita que se cierre el programa sin permiso del usuario.
    
    #Entrada
    while True: #Este bucle actúa para comprobar si el texto tiene caracteres especiales. Permite ingresar números, por lo que 1ojo1 es un palíndromo pero 1ojo no. 
        print("Introduzca su texto.")
        texto = input()
        contador = 0
        for i in range(0,len(texto)):
            for j in range(0, len(specialChar)):
                if texto[i] == specialChar[j]:
                    print("No se admiten caracteres especiales")
                    contador = 1
        if contador != 1:
            break

    #Proceso
    textoDep = texto.replace(" ", "").lower()
    contador = 0  #Reusamos contador para no generar más variables
    for k in range (0, len(textoDep)):
        if textoDep[k] != textoDep[len(textoDep)-1-k]:
            contador = 1
            break
  
    #Salida
    if contador == 1:
        print(f"El texto {texto} no es un palíndromo.")
    else:
        print(f"El texto {texto} es un palíndromo")
    print("Para salir del programa escriba SALIR, en caso contrario pulse ENTER")
    valMain = input() 
