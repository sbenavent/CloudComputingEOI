#Ejercicio 3: Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene
#El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.

#Entrada
texto = str(input())

#Proceso
i = 0
contador = 1
while i != len(texto):
    if texto[i] == " ":
        contador = contador +1
    i = i+1

#Salida
print(f"El número de palabras en su texto es {contador}")
input("Pulsa enter para salir.")
#No entiendo por qué hacerlo con un bucle while cuando puedes hacer simplemente print("El número de palabras de su texto es", len(texto.split())) y lo haces todo en 1 línea.
