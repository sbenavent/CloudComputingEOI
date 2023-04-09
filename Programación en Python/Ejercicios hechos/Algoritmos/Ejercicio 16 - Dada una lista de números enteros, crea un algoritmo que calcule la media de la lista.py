#Ejercicio 16: Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.
from statistics import mean

print("Bienvenido/a al programa. Por favor, introduzca una serie de números enteros. El algoritmo calculará la media de la lista")
valMain = ""
while valMain != "SALIR":
    
    #Entrada
    lista = []
    while True:
        print("Introduzca un número para añadirlo a la lista. Escriba STOP terminar la lista.")
        numero = input()
        if numero == "STOP":
            break
        else:
            try:
                lista.append(int(numero))
            except Exception as error:
                print(f"Ha sucedido un error {error}. Por favor, introduzca solo números enteros.")
    
    #Proceso
    resultado = round(mean(lista), 3)

    #Salida
    print(f"Dada la lista de números enteros {lista}, se calculó la media de la lista como {resultado}.")
    print("Si quiere seguir usando el prgrama pulse ENTER. De lo contrario, Introduzca SALIR para salir.")
    valMain = input()
    