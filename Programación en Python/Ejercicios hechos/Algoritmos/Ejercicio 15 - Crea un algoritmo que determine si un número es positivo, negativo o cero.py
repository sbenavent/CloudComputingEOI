#Ejercicio 15: Crea un algoritmo que determine si un número es positivo, negativo o cero.

valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Introduzca un número.")
    while True:
        try:
            num = float(input())
            break
        except Exception as error:
            print(f"Ha ocurrido un error {error}. Introduzca solo números.")

    #Proceso y salida.
    if num == 0:
        print(f"El numero introducido es {num}")
    elif num > 0:
        print(f"El número {num} es un número positivo")
    else:
        print(f"El número {num} es un número negativo")
    print("Si desea salir escriba SALIR. Si desea seguir usando el programa, pulse ENTER")
    valMain = input()