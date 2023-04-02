#Ejercicio 7: Dado un número entero, crea un programa en Python que determine si es par o impar.
print("Bienvenido al programa. La aplicación le indicará si el número entero que introduzca es par o impar. Siga las instrucciones para continuar")
valMain = ""
while valMain != "SALIR": #Este bucle sirve para que el programa solo se cierre a petición del usuario.

    #Entrada
    val1 = ""
    while val1 != True:
        try:
            print("Introduzca un número entero.")
            numero = int(input())
            val1 = True
        except Exception as error:
            print(f"Se ha producido un error {error}. Solo se admiten números enteros. ")
    
    #Proceso
    resto = numero%2
    resultado = "par."
    if resto != 0:
        resultado = "impar."
    
    #Salida
    print(f"El número que ha introducido es {numero}, que es un número {resultado}")
    print("Introduzca SALIR para cerrar el programa o pulse ENTER para introducir otro número.")
    valMain = input()
