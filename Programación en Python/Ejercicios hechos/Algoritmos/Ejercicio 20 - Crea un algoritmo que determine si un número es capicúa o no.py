#Ejercicio 20: Crea un algoritmo que determine si un número es capicúa o no.
print("Bienvenido/a al programa. Este algoritmo determinará si el número entero introducido es capicúa o no. Siga las instrucciones para continuar.")

valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Introduzca un número entero.")
    while True:
        try:
            numero = int(input())
            break
        except Exception as error: 
            print(f"Se ha producido un error {error}, solo se admiten números enteros.")

    #Proceso
    numero = str(numero) #No me deja hacer len(numero) si el número es int.
    resultado = "es capicúa."
    for i in range (0, len(numero)):
        if numero[i] != numero[len(numero)-1-i]:
            resultado = "no es capicúa."
            break

    #Salida
    print(f"El número introducido {numero} {resultado}")
    print("Si desea salir introduzca SALIR. En caso contrario pulse ENTER.")
    valMain = input()