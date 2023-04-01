#Ejercicio 2: Calcular el salario de un empleado

print("Bienvenido a la calculadora de salario, por favor, siga las instrucciones para continuar.")
valMain = ""
while valbucle != "SALIR": #Para poder usar el programa en varias ocasiones
    #Entrada
    print ("Introduzca las horas que trabaja a la semana")
    val1 = ""
    while val1 != True:
        try:
            horas = float(input())
            if horas > 0:
                val1 = True
            else:
                print("El número debe ser mayor que 0.")
        except :
            print(f"Se ha producido un error {error}, debe introducir un número decimal.")

    print("Introduzca el número de pagas anuales")
    val2 = ""
    while val2 != True:
        try:
            pagas = int(input())
            if pagas > 0:
                val2 = True
            else:
                print("El número de pagas no puede ser igual o menor a 0.")
        except Exception as error:
            print(f"Se ha producido un error {error}, debe introducir un número entero")

    print("Introduzca su salario pagado por hora.")
    val3 = ""
    while val3 != True:
        try:
            salario = float(input())
            if salario > 0:
                val3 = True
            else:
                print("El número de horas no puede ser igual o menor a 0.")
        except Exception as error:
            print(f"Se ha producido un error {error}, debe introducir un número decimal.")

    #Proceso
    horas = horas * 4 #Sacamos las horas mensuales
    horas = float(horas) #Las pasamos a float de nuevo
    pagas = float (pagas) #Pasamos pagas a float para poder hacer el cálculo
    salarioAnualBruto = float(horas * pagas * salario) #Calculamos bruto anual
    tablaIrpf = [0.81, 0.76, 0.70, 0.63, 0.55, 0.43] #Porcentajes del IRPF en España. En el primer caso sería un 19% de impuestos, por lo que se cobraría un 81% o Salario * 0.81
    if salarioAnualBruto >= 300000:
        salarioAnualNeto = salarioAnualBruto * tablaIrpf[5]
    elif salarioAnualBruto >= 60000:
        salarioAnualNeto = salarioAnualBruto  * tablaIrpf[4]
    elif salarioAnualBruto >= 35200:
        salarioAnualNeto = salarioAnualBruto * tablaIrpf[3]
    elif salarioAnualBruto >= 20200:
        salarioAnualNeto = salarioAnualBruto * tablaIrpf[2]
    elif salarioAnualBruto >= 12451:
        salarioAnualNeto = salarioAnualBruto * tablaIrpf[1]
    else:
        salarioAnualNeto = salarioAnualBruto * tablaIrpf[0]
    salarioMensual = salarioAnualNeto / pagas

    #Salida
    print(f"Su salario anual será de {salarioAnualBruto}€ en bruto, cobrando {salarioAnualNeto}€ en neto en {pagas} pagas de {salarioMensual} €")
    print("Escriba SALIR para salir del programa o pulse Enter para calcular otro salario")
    valMain = input()
