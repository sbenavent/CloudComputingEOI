#Ejercicio 8: Crea un algoritmo que determine si un año es bisiesto o no.
print("Bienvenido/a al programa. Este algoritmo determinará si el año introducido es bisiesto o no.Siga las instrucciones para continuar")
valMain = ""
while valMain != "SALIR": #Este bucle sirve para que el programa solo se cierre a petición del usuario.

    #Entrada
    val1 = ""
    while val1 != True:
        try:
            print("Introduzca el año.")
            numero = int(input())
            val1 = True
        except Exception as error:
            print(f"Se ha producido un error {error}. Solo se admiten números enteros. ")
    
    #Proceso
    resultado = "no es bisiesto."
    if numero%400 == 0:
        resultado = "es bisiesto."
    if numero%4 == 0 and numero%100 != 0:
        resultado = "es bisiesto."
    
    #Salida
    print(f"El año {numero} que ha introducido {resultado}")
    print("Escriba SALIR para salir del programa o pulse ENTER para introducir otro año.")
    valMain = input()