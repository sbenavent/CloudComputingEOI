#Ejercicio 17: Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. 
#El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.
import random

valMain = ""
while valMain != "SALIR":
   
    print("¡Bienvenido al juego! Tienes 10 intentos para adivinar un número del 1 al 100. ¿Podrás conseguirlo?")
    numeroAleatorio = random.randint(1,100)

    val = "" 
    contador = (int(0))

    print("Mira a ver si aciertas el número")
    while True:
        try:
            guess = int(input())
            if guess >= 1 and guess <= 100:
                if contador == 10:
                    print("SE TE ACABARON LOS INTENTOS")
                    print(f"El número correcto era {numeroAleatorio}")
                    break
                elif guess > numeroAleatorio:
                    print("Un poco más bajo.")
                    contador = contador+1
                elif guess < numeroAleatorio:
                    print("Un poco más alto.")
                    contador = contador+1
                else:
                    print("¡¡¡PREMIO!!!")
                    break
            else:
                print("Solo se admiten números enteros del 1 al 100.")
        except Exception as error:
            print(f"Se ha producido un error {error}. Por favor introduzca solo números enteros del 1 al 100.")
            


    print("Escribe SALIR para cerrar el juego o pulsa ENTER para intentarlo de nuevo")
    valMain = input()