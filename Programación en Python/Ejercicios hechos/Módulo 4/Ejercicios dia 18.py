#### Ejercicios básicos:

#Hacer para el martes 18 de abril, los siguientes ejercicios básicos con compresión de colecciones y mostrar su equivalente con el bucle .
from os import system
#1. Crear una lista que contenga las letras de una palabra, cada una en mayúscula:
def listaCadena():
    while True:
        palabra = input("Introduzca una palabra")
        contador = 0
        for letra in palabra:
            if letra.isalnum() == False:
                contador = 1
                print("No se admiten caracteres especiales")
                break
            if letra.isnumeric() == True:
                contador = 1
                print("No se admiten números")
                break
        if contador == 0:
            break
    print("La cadena de su palabra con todas las letras mayúsculas es")
    print(list(palabra.upper()))

#2. Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:
def numCuadrados():
    cuadrados = {"1": 1,"2":4,"3":9,"4":16,"5":25}
    print(cuadrados)

#3. Crear un diccionario que contenga los nombres y edades de varias personas:
def dicPer():
    diccionarioPersonas = {}
    for i in range (1,99):
            element = input("Si quiere añadir los datos de una persona pulse enter, si quiere parar introduzca STOP")
            if element == "STOP":
                break
            else:
                datos = []
                datos.append(input("Introduzca su nombre completo"))
                datos.append(input("Introduzca su edad"))
                diccionarioPersonas.update({i:datos})
    print("Los datos de las personas introducidas son")
    print(diccionarioPersonas)
#4. Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por "EOI", los múltiplos de 5 por "Cloud" y los múltiplos de ambos por "EOICloud".
def multiplos():
    lista=[]
    for i in range (1,21):
        lista.append(int(i))
    for n in range(len(lista)):
        if lista[n]%3 == 0 and lista[n]%5 == 0:
            lista[n] ="EOICloud"
        elif lista[n]%3 == 0:
            lista[n] = "EOI"
        elif lista[n] %5 == 0:
            lista[n] = "Cloud"
    print(f"La lista según lo que se pide en el ejercicio es {lista}")

#5. Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.
def palabras():
    while True:
        texto = input("Introduzca un texto")
        contador = 0
        for char in texto:
            if char.isalnum == False:
                contador = 1
                print("No se admiten caracteres especiales")
                break
            if char.isnumeric == True:
                print("No se admiten números")
                contador = 1
                break
        if contador == 0:
            break
    lista = texto.lower().split(" ")
    diccionario = {i:lista.count(i) for i in lista} 
    print(f"El diccionario generado es {diccionario}") 
#6. Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema.
#   **Nota** el diccionario deberá ordenarse por su clave.
def ciudades():    
  
    listaCiudades = ["Nueva York", "Tokio", "París","Londres","Sídney","Buenos Aires","Johannesburgo","Moscú","Ámstedarm","Dubai"]
    listaEmblemas = ["Estatua de la Libertad","Las flores de cerezo","La Torre Eiffel","El Big Ben", "La ópera de Sídney","El obelisco","El león","El Kremlin","Los Molinos de Viento","El Burj Khalifa"]

    print("Dada la siguiente lista de ciudades, seleccione aquellas de las que quiera saber su emblema")
    print("""
    Nueva York
    Tokio
    París
    Londres
    Sídney
    Buenos Aires
    Johannesburgo
    Moscú
    Ámsterdam
    Dubai
    """)
    dicCiudad = {}
    while True:
        ciudad = input("Escriba el nombre de su ciudad o STOP para terminar: ")
        if ciudad == "STOP":
            break
        else:
            if all(ciudad != n for n in listaCiudades) == True:
                print("Esa ciudad no está en la lista.")
            else:
                for n in range(0,len(listaCiudades)):
                    if ciudad == listaCiudades[n]:
                        dicCiudad[listaCiudades[n]]=listaEmblemas[n]
    print(f"La lista de ciudades con sus emblemas correspondientes es {dicCiudad}")


### Menú principal
while True:
    system("cls")
    print("Seleccione numero ejercicio. 0 para salir: ")
    print("1. Crear una lista que contenga las letras de una palabra, cada una en mayúscula:")
    print("2. Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:")
    print("3. Crear un diccionario que contenga los nombres y edades de varias personas:")
    print("4. Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por EOI, los múltiplos de 5 por CLOUD y los múltiplos de ambos por EOICloud")
    print("5. Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.")
    print("6. Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema.")
    try:
        ejercicio = int(input())
    except Exception:
        print("Numeros pls")

    if ejercicio == 0:
        break
    elif ejercicio == 1:
        listaCadena()
    elif ejercicio == 2:
        numCuadrados()
    elif ejercicio == 3:
        dicPer()
    elif ejercicio == 4:
        multiplos()
    elif ejercicio == 5:
        palabras()
    elif ejercicio == 6:
        ciudades()
    else:
        print("Solo del 1 al 6")
    input("Pulse enter para continuar")
