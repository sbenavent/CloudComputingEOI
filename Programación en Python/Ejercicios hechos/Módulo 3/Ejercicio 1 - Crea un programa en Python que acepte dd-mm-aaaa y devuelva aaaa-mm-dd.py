#Ejercicio 1: Crea un programa en Python que acepte una fecha como cadena de caracteres en formato "dd/mm/aaaa" y devuelva la fecha en formato "aaaa-mm-dd", con el año primero
# El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
from datetime import datetime

#Entrada
while True:
    print("Introduzca su fecha en formato dd/mm/aaaa")
    try:
        fecha = datetime.strptime(input(),"%d/%m/%Y")
        break
    except Exception as error:
        print(f"Se ha producido un error {error}. Solo se admiten fechas con formato dd/mm/aaaa")

#Proceso y Salida.
print(f"Su fecha en formato convertido es {fecha.year}-{fecha.month}-{fecha.day}.")
input("Pulse ENTER para salir.")