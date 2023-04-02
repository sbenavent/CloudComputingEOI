#Ejercicio 12: Dado un número entero, crea un algoritmo que determine si es primo o no.
print("Bienvenido/a. Este algoritmo hayará si el número entero que introduzca es primo o no.")
valMain = ""
while valMain != "SALIR":
#Entrada
    print("Introduzca un número entero.")
    while True:
        try:
            n = int(input())
            if n != 0:
                break
            else:
                print("El número no puede ser 0.")
        except Exception as error:
            print(f"Se ha producido un error {error}. Introduzca solo números enteros")

    #Proceso
    resultado = "es primo."
    for i in range (2,n-1):
        if n%i == 0:
            resultado = "no es primo."
            break

    #Salida
    print(f"El número {n} {resultado}")
    print("Escriba SALIR para salir o pulse ENTER para calcular otro factorial.")
    valMain = input()