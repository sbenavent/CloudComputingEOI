#Ejercicio 13: Calcular el volumen de un cubo dado su lado.
entrada = ["mm", "cm", "dm", "m"]
salida = ["mm3", "cm3", "dm3","m3", "L"]
valEntradaLista = [0,1,2,3]
valSalidaLista = [0,1,2,3,4]

valMain = ""
while valMain != "SALIR":
    #Entrada
    print("Introduzca la unidad de media del lado del cubo. Solo puede ser mm, cm, dm, m")
    while True:
        uEntrada = input()
        if True in (entrada[i] == uEntrada for i in range (len(entrada))): #Comprueba que haya una igualdad entre lo introducido y los valores de la lista
            for i in range (0, len(entrada)): #Comprueba de nuevo, para seleccionar valor de entrada en las 2 líneas inferiores.
                if entrada[i] == uEntrada:
                    valEntrada = valEntradaLista[i]
            print(f"Ha seleccionado {uEntrada}")
            break
        else:
            print("Seleccione una unidad de las indicadas.")

    print("Seleccione una unidad de volumen para su cubo. Solo puede ser mm3, cm3, dm3, m3, L")
    while True:
        uSalida = input()
        if True in (salida[j] == uSalida for j in range (len(salida))): #Se repite lo mismo que en las líneas 13 y 14.
            for j in range (0,len(salida)):
                if salida[j] == uSalida:
                    valSalida = valSalidaLista[j]
            print(f"Ha seleccionado {uSalida}")
            break
        else:
            print("Seleccione una unidad de las indicadas")

    print("Seleccione el valor del lado de su cubo")
    while True: #Seleccionas un valor de lado
        try:
            lado = float(input())
            if lado > 0:
                break
            else:
                print("El valor del lado debe de ser superior a 0.")
        except Exception as error:
            print(f"Se ha producido un error {error}. Introduzca solo números decimales positivos")

    #Proceso
    volumen = lado ** 3
    if valSalida == 4: #Equivalencia entre dm3 y L.
        valSalida = 2

    #Salida
    if valEntrada == valSalida:
        print(f"El volumen de su cubo es {volumen}{uSalida}")
    else:
        volumen = float(volumen * 1000 ** (int(valEntrada - valSalida))) #Cálculo para mostar el número correcto según las unidades seleccionadas.
        print(f"El volumen de su cubo es {volumen}{uSalida}")
    print("Escriba SALIR para salir o pulse ENTER para seguir usando el programa.")
    valMain = input()