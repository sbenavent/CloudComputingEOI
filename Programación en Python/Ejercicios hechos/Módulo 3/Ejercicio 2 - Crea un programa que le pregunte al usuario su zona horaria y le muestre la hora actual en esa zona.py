#Ejercicio 2: Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona.
#El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

from datetime import datetime
import pytz

#Entrada
print("Ingrese su zona horaria. Puede consultar su zona horaria en https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568")
while True:    
    try: 
        zona = input()
        pytz.timezone(zona)
        break
    except Exception as error:
        print(f"Se ha producido un error {error}. Introduzca una zona horaria de la lista.")

#Proceso y salida
print(f"La hora actual en la zona {zona} es",datetime.strftime(datetime.now(pytz.timezone(zona)), "%H:%M:%S del %A %d de %b del %Y"))
input("Pulse enter para salir")