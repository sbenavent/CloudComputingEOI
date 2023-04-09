#Ejercicio 4: Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30")
#La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros
from datetime import datetime

#Entrada
print("Introduzca la hora en formato hh:mm")
while True:
    try:
        hora = datetime.strptime(input(), "%H:%M")
        break
    except Exception as error: 
        print(f"Se ha producido un error {error}. Ingrese solamente una hora válida siguiendo el formato ofrecido. Ej: 19:30")

#Proceso y salida
print("La hora introducida es", datetime.strftime(hora, "%X"))