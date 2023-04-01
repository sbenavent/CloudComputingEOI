#Ejercicio1: Calcular la letra del DNI español.

letras = "TRWAGMYFPDXBNJZSQVHLCKE"
valMain = "false"
print("Bienvenido al programa. Este algoritmo calculará la letra de su DNI en España. Para continuar, siga las instrucciones.")
while valMain != "SALIR": #Para poder usar el programa en varias ocasiones
    #Entrada
    print("Introduzca los 8 dígitos de su número")
    val1 = ""
    while val1 != True:
        nif = input()
        try:
            int(nif)
            if len(nif) == 8:
                val1 = True
            else:
                print(f"Introduzca un número de 8 dígitos.")
        except Exception as error:
            print(f" Se ha producido un error {error} Debe introducir un número entero.")

    #Proceso
    nif = int(nif)
    resto = nif%23

    #salida
    print(f"La letra de su DNI es {letras[resto]}")
    print("Si desea salir, escriba SALIR o pulse ENTER para calcular otra letra ")
    valMain = input()
        
        
