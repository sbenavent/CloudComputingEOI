#Ejercicio 6: Crea un programa en Python que convierta grados Celsius a Fahrenheit
print("Bienvenido/a al conversor de grados celsius a Farenheit. Siga las instrucciones para continuar.")
valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Introduzca la temperatura en Celsius")
    val = ""
    while val != True:
        try:
            celsius = float(input())
            val = True
        except Exception as error:
            print(f"Se ha producido un error {error}. Por favor, introduzca solo números decimales")

    #Proceso
    farenheit = celsius * (9/5) + 32 

    #Salida
    print(f"Su temperatura celsius es {celsius}ºC. Su temperatura en Farenheit es {farenheit}ºF")
    print("Escriba SALIR para salir o pulse la tecla ENTER para hacer otra conversión")
    valMain = input()