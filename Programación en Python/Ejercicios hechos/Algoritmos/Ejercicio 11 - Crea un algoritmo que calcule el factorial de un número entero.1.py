#Ejercicio 10: Crea un algoritmo que calcule el factorial de un número entero.
from math import factorial

print("Bienvenido/a. Este algoritmo hayará el factorial del número introducido.")
valMain = ""
while valMain != "SALIR":
#Entrada
    print("Introduzca un número entero.")
    while True:
        try:
            n = int(input())
            break
        except Exception as error:
            print(f"Se ha producido un error {error}. Introduzca solo números enteros")

    #Proceso
    if n == 0:
        print(f"El factorial de {n} es 1.")
    else:
        fact = factorial(n)

    #Salida
    print(f"El factorial de {n} es {fact}.")
    print("Escriba SALIR para salir o pulse ENTER para calcular otro factorial.")
    valMain = input()