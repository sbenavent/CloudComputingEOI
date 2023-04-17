#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase. La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.


asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
print(asistencias)
#Se pide:

#1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.
total = len(asistencias["Ana"]) + len(asistencias["Luis"])
print(f"El total de asistencias entre los dos alumnos es de {total}")

#2. Mostrar las sesiones a las que asistieron ambos alumnos.
print(f"Ana ha asistido a las sesiones {asistencias['Ana']} y Luis a las sesiones {asistencias['Luis']}")

#3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.
print("Las sesiones a las que solo ha asistido uno de los alumnos son:")    
for i in asistencias["Ana"]:
    if any(i == j for j in asistencias["Luis"]) == False:
        print(f"Sesión {i}")
for i in asistencias["Luis"]:
    if any(i == j for j in asistencias["Ana"]) == False:
        print(f"Sesión {i}")

#4. Mostrar las sesiones a las que asistió Ana pero no Luis.
print("De las cuales a las que solo ha asistido Ana son:")
for i in asistencias["Ana"]:
    if any(i == j for j in asistencias["Luis"]) == False:
        print(f"Sesión {i}")

#5. Mostrar las sesiones a las que asistió Luis pero no Ana.
print("Y a a las que ha asistido solamente Luis son:")
for i in asistencias["Luis"]:
    if any(i == j for j in asistencias["Ana"]) == False:
        print(f"Sesión {i}")

input("Pulsa Enter para salir.")