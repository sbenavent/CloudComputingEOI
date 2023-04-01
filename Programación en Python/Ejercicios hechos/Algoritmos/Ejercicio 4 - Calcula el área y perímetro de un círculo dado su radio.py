#Ejercicio 4: Calcula el área y perímetro de un círculo dado su radio
print("Bienvenido a la calculadora de perímetro y radio de un círculo, para continuar, siga las instrucciones.")
valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Por favor, intruzca el radio de su círculo.")
    val = ""
    while val != True:
        radio = input()
        try:
            radio = float(radio)
            if radio > 0:
                val = True
            else:
                print("Por favor intruzca un número decimal positivo.")
        except Exception as error:
            print(f"Se ha producido un error {error}, por favor, introduce un decimal positivo")

    print("Por favor introduzca la unidad de medida de su círculo")
    unidad = input()

    #Proceso
    area = 3.14 * (radio ** 2)
    perimetro = 3.14 * radio * 2

    #Salida
    print(f"El perímetro de su círculo es {perimetro}{unidad} y el área de su círculo es {area}{unidad}^2.")
    print("Escriba SALIR para salir o pulse ENTER para seguir usando el programa.")
    valMain = input()