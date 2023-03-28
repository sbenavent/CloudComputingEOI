#	Fundamentos de Programación	

##	Sesión 17.03.2023 - Ejercicios de Algoritmos

###	1. **Calculadora de letra de DNI**

***Paso 1*** Definir el problema

Para calcular la letra del DNI se necesita dividir los 8 dígitos entre el 23 y el resto se compara con el código TRWAGMYFPDXBNJZSQVHLCKE.

En primer lugar necesitamos introducir el valor ```nif``` de longitud 8 y dividirlo entre 23 para obtener el resto. 

En segundo lugar obtener el resto y establecer una variable ```resultadoResto```			

En segundo lugar establecer un if de varios resultados, donde ```if resultadoResto = n, print(x)``` donde n es una letra del 0 al 22 y x es la letra en la posición del código cuyos valores se establecen en una tabla.

***Paso2***: Planteamiento del problema

Entrada

* Introducir DNI mediante teclado y controlar la longitud
* Comprobar que tiene la longitud correcta

Proceso

* Si tiene la longitud correcta, comprobar en un tabla el valor de la letra según el resto del NIF mod 22.

Salida

* Devolver la letra.

***Paso 2*** Pseudocódigo

``` nif``` con tipado num = entrada teclado

```longitudNif``` en base a nif

```resultadoResto``` 

​	```longitudNif=false```

​	```until longitudNif = true```

​		```if longitudNif = 8 ; set longitudNif = true``` 

​		```if not print(Introduzca un DNI correcto)```

​		```end if```

​	```end until```

```resultadoResto = nif%23```

```if resultadoResto = 0 , print(T)``` 

...

```if resultadoResto = 22 ; print(E)```

###	2. Calcular el salario de un empleado

***Paso 1:*** Definir el problema

1. Pedir al empleado que introduzca el pago por hora
2. Pedir que introduzca las horas trabajadas
3. Pedir que introduzca su número de pagas
4. Calcular en base a eso su salario en bruto anual
5. Definir su estado de IRPF 
6. Deducir los impuestos de su nómina y calcular neto anual
7. Dividir neto anual y sacamos nómina. 

***Paso 2:*** Procedimiento

Introducir variables 

- salariohora
- horas trabajadas
- pagas
- salarioAnualBruto = salario * pagas * horas
- irpf
- salarioAnualNeto = salarioAnualBruto * irpf
- nomina = salarioAnualNeto/pagas

Para calcular IRPF lo sacamos de esta tabla:

Hasta 12450 , 19.0%

Entre 12450 hasta 20.1999 -> 24%

Entre 20.200 a 35.199 -> 30%

35.200 < x < 59.999 -> 37%

... < x < 299.999 -> 45%

x>300.000 --> 47%

Con una serie de ifs podemos establecer irpf como 1-porcentaje/100 por ejemplo 1-0.19 para el primer caso. 

Hacer los cálculos. 

***Paso 3:*** Pseudocódigo

```var salario num``` 

```var horas trabajadas```

```var pagas num ```

```var salarioAnualBruto num = salario * horasTrabajadas * pagas```

```var irpf``` num

```var salarioAnualNeto``` num

```var nomina``` num



```Algoritmo```

​	```salario <- entrada teclado```

​	```pagas <- entrada teclado```

```	horasTrabajadas <- entrada teclado```

​		if salarioAnualBruto < 12450 ; set irpf = 1-0.19  //todo: optimizar todos estos ifs

​		if 12450 < salarioAnualBruto < 201999; set irpf = 1-0.24

​		if ...	

​		...

​		endif

​	set salarioAnualNeto = salarioAnualBruto * irpf

​	set nomina = salarioAnualNeto / pagas

​	print("Su nómina es [nomina]")

endAlgoritmo

### 3 Determinar la ruta para llegar a una ciudad por avión

***Paso 1:*** Definir el problema

Para definir una ruta en avión hay que tener en cuenta la ciudad de destino, el aeropuerto más cercano a la salida y el aeropuerto más cercano al destino. Una vez hecho eso, consultar en una base de datos los vuelos disponibles. En este caso me voy delimitar al territorio español por conveniencia. 

***Paso 2:*** Planteamiento

Lo primero es introducir las bases de datos datosAeropuertos y datosVuelos. También hay que cargar una base de datos de las ciudades de España. A todo esto habría que integrar una herramienta como Maps. En segundo lugar, preguntar al usuario de qué ciudad a qué ciudad va, asegurando que las variables sean de la base de Maps Por último, mostarle una oferta de diferentes vuelos con enlaces a aerolíneas, para los que también necesitamos base de datos, después de consultar. 

**Entrada**

Pedir ciudad salida

Pedir ciudad de destino

**Proceso**

Consultar base de datosAeropuertos usar maps para ver el más cercano a la salida.

Hacer lo mismo para la ciudad de destino.

Consultar en datosVuelos , obtener información de ofertas de vuelos.

**Salida**

Dar enlaces para comprar los vuelos. 

***Paso 3:*** Pseudocódigo

```
Algoritmo vuelos

ciudadOrigen <- texto

ciudadDestino <- texto

baseDatosAeropuertos

baseDatosVuelos

(herramientaBusquedaVuelos)

(herramientaCreacionRutas)

##

origen <- false

print("Introduzca su lugar de salida")

hasta que origen <- true 

​	ciudadOrigen <- Leer (Teclado)

​	if ciudadOrigen está en la base de Maps, entonces

​		origen <- true

​	ifnot entonces

​		print(Introduzca un lugar de salida válido)

​	finif

finhasta

destino <- false

print("Introduzca su ciudad de destino")

ciudadDestino <- Leer (Teclado)

hasta destino = true

​	if ciudadDestino está en la base de Maps, entonces

​		destino <- true

​	ifnot entonces

​		print(Introduzca un lugar de destino válido)	

​	finif

​	fin hasta

#####

ruta <-Establecer (herramientaCreacionRutas)

vuelos <- Búsqueda y crear lista (herramientaBusquedaVuelos)

###

print("Puede obtener su billete en los siguientes enlaces" +vuelos)

Fin Algoritmo
```

### 4. Calcula el área y perímetro de un círculo dado su radio.

***Paso 1***: Descripción de problema

El área un círculo es pi * r^2, perímetro es 2 * pi * radio.

***Paso 2:*** Planteamiento.

variables: radio, perímetro, área

Entrada

- Introducir radio 

  

Proceso

* Cálculo del perimetro
* Calculo del area

Salida

* Imprimir resultados

***Paso 3*** Pseudocódigo

```
Algoritmo círculo

radio <- 0

area <- 0

perímetro <- 0

###

print("Introduzca el radio de su círculo en metros")

radionum<- false

hasta que radionum = true, entonces

radio <-Leer (Teclado)

​	if radio = numérico, entonces

​		radionum <- true

​	ifnot, entonces

​		print("Introduzca un valor numérico válido")

​	finif	

finhasta

###

area <- radio * 3.14^2

perimetro <- 2 * 3.14 * radio

###

Print("Para un círculo de radio" +radio "Su área sería" +area "m^2 y su perímetro sería de" +perimetro "m")

Fin Algoritmo
```



### 5. Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

***Paso 1***: Definición del problema

No es difícil definir el problema, se podría hacer con un subalgoritmo de ordenación de variables, que seguramente la mayoría de las herramientas de código tienen. 

***Paso 2***: Planteamiento del problema

Para poder comenzar con el problema hay que establecer una "lista" de números enteros y una variable "n" que es el número de elementos en la lista. 

Entrada

* Introducir la lista de números enteros, separados por comas
* Asegurarnos de que solo hay números enteros

Proceso

* Ejecutamos el subalgoritmo de ordenación, este lo he sacado gracias a herramientas como chatgpt y lo he adecuado al pseudocódigo para entenderlo. 

Salida

* Dar la lista de números ordenados

***Paso 3***: Pseudocódigo

[Algoritmo Python que uso como base](https://gptsave.xyz/images?id=90f04fce-e804-436d-b0a6-bd85d1d93dde )

```
Algoritmo números enteros

lista

lista ordenada

n <- longitud lista

### // 

print ("Introduzca una serie de números enteros separados por comas")

listaval <- false

hasta que listaval = true, repetir

lista <-  Leer (Teclado) // (8,7,9,3)

listaval <- false

hasta que listaval = true, repetir

​	si lista sólo contiene números enteros, entonces

​		listaval <- true

​	sino, entonces

​		print("Introduzca solamente números enteros")

​	finsi

finhasta

###

n <- longitud lista // 4 (0,1,2,3)

i <- 0

para i=0, repetir

​	para j = 0, hasta j=n-i-1, repetir

​		si lista(j) mayor que lista(j+1), entonces // (8,7,9,3)

​			lista(j), lista(j+1) <- lista(j+1), lista(j)  // (7,8,9,3) --> (7,8,9,3) --> (7,8,3,9) | (7,8,3,9) --> (7,3,8,9) | (3,7,8,9)

​		finsi

​		j <- j+1
	hasta j=n-i-1

	i <- i+1
hasta i=n

###

print("Su lista ya ordenada es" +lista)	

Fin Algoritmo
```



### 6. Crea un algoritmo que convierta grados Celsius a Fahrenheit.

***Paso 1***: Definición del problema

El problema es realmente sencillo, la conversión se realiza siguiendo una fórmula matemática

***Paso 2***: Planteamiento del problema

Simplemente, entrada estándar donde solo se puedan introducir números, proceso con la fórmula y salida con resultado. 

***Paso 3***: Pseudocódigo

```
Algoritmo de celsius a farenheit

###

print("Introduzca la temperatura en ºC")

temp <- false

hasta temp = true, repetir

celsius <- Leer(Teclado)

​	si celsius es un numero, entonces

​		temp <- true

​	sino, entonces

​		print("Sólo se aceptan valores numéricos.")

​	finsi
fin hasta

### 

farenheit <- (celsius * 9/5) + 32 

###

print ("La temperatura es de" +farenheit "ºF")

Fin algoritmo
```



### 7.  Dado un número entero, crea un algoritmo que determine si es par o impar.

***Paso 1***: Definición del problema

La solución es determinar si el número es igual a 0 o divisible entre 2. 

***Paso 2***: Planteamiento del problema

Entrada

* Introducir número y comprobar si es entero

Proceso

* Comprobar si es 0 o si mod = 0

Salida

* Decir si es par o impar

***Paso 3***: Pseudocódigo

```
Algoritmo número par o impar

###

print("Introduzca un número entero ")

val <- false

hasta val = true, repetir

​	numero <- Leer(Teclado)

​	si numero = numero entero, entonces

​		val = true

​	sino, entonces

​		print("Solo se admiten números enteros.")

​	fin si

fin hasta

###

resultado <- impar

si numero = 0 ó numero mod 2 = 0 , entonces

​	resultado <- par

fin si

###

print("Su número es" +resultado)

Fin Algoritmo
```



### 8. Crea un algoritmo que determine si un año es bisiesto o no.

***Paso 1***: Definición del problema

Problema muy similar al anterior. Para saber si un año es bisiesto debe de: 

* O bien ser divisible entre 400
* O bien ser divisible entre 4 y no divisible entre 100

***Paso 2***: Planteamiento del problema

Entrada

* Pedir por teclado un numero entero y comprobar 

Proceso

* Uso de funciones if para sacar mod de 400, mod de 4 y mod de 100

Salida

Decir si es bisiesto o no. 

***Paso 3***: Pseudocódigo

```
Algortimo bisiestos

###

print("Introduzca el año")

val <- false

hasta val = true, repetir

​	anyo <- Leer(Teclado)

​	si anyo = numero entero, entonces

​		val <- true

​	sino, entonces

​		print("Introduzca solamente números enteros.")

​	fin si

fin hasta

###

resultado <- no bisiesto

si anyo mod 400 = 0, entonces

​		resultado <- bisiesto

si anyo mod 4 = 0 y anyo mod 100 diferente a 0

​	resultado <- bisiesto

fin si

###

print("El año introducido es" +resultado)

Fin algoritmo
```

​		

### 9. Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

***Paso 1***: Definición del problema

Un palíndromo es una palabra que se lee igual en ambos sentidos, como por ejemplo: ojo, seres, asa... 

***Paso 2***: Planteamiento del problema

Para poder comprobar si una palabra es un palíndromo, yo convertiría la palabra en una cadena, y comprobaría los valores de cada una de las posiciones hasta  la mitad de la longitud con su posición simétrica.

Entrada

* Introducir una cadena de texto, que no admita signos de puntuación, números, o caracteres especiales.

Proceso

* Depurar la cadena de texto.
* Comprobar letra por letra si la posición de la cadena se corresponde con su simétrico. 

Salida

* Imprimir si la palabra es o no un palíndromo. 

***Paso 3***: Pseudocódigo

```
Algoritmo palindromo

###

print("Introduzca texto aquí.")

val<-false

hasta val = true, repetir

​	texto <- Leer(Teclado)

​	si texto = texto sin caracteres especiales, entonces
​		val <- true

​	si no, entonces

​		print ("No se admiten números o caracteres especiales")

​	finsi

fin hasta

###

textoDepurado <- depuraciónCadena(texto)

arrayTexto <- convertirArray(textoDepurado)

n=longitud(textoDepurado)

resultado <- "es un palíndromo"

j<-0

para j=0, repetir hasta j=n

​	si arrayTexto (j) es diferente de arrayTexto(n-j), entonces

​		resultado<- "no es un palíndromo"

​		j <- n #break

​	si no, entonces

​		j <- j+1

​	finsi

fin repetir

###

print("La cadena de texto que has introducido" +resultado)

Fin algoritmo
```



```
SubAlgoritmo depuracionCadena (cadena)    #quita los espacios en blanco, otros caracteres y convierte todo a minusculas    

i<-0    

Mientras cadena[i] sea diferente de findecadena Haga        

​	caracter<-""       

​	Si  el ASCII de cadena[i]  mayor que 64 y ASCII de cadena[i] menor que 91 Entonces           

​		 caracter<-cadena[i] en minusculas      

​	Fin Si        

​	Si  el ASCII de cadena[i]  mayor que 96 y ASCII de cadena[i] menor que 123 Entonces            

​		caracter<-cadena[i]        

​	End Si        

​	temporal <- temporal + caracter        

​	Si caracter es diferente "" Entonces            

​		i<-i+1        

​	Fin Si    

Fin Mientras    

L<-i    

reversa<-""    

Para N = 0 Hasta L-1 Con Paso 1 Haga        

​	reversa    <-reversa+ temporal[i-1]        

​	i<-i-1    

Fin Para    

devuelva reversa 

Fin SubAlgoritmo


```



### 10. Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente.

***Paso 1***: Definición del problema

El problema lo define tal cual el enunciado del ejercicio, es ordenar una lista de palabras según orden alfabético. Para ello se le asignará un valor a cada letra del abecedario del 1 al 27. 

| A    | 1    |
| ---- | ---- |
| B    | 2    |
| C    | 3    |
| D    | 4    |
| E    | 5    |
| F    | 6    |
| G    | 7    |
| H    | 8    |
| I    | 9    |
| J    | 10   |
| K    | 11   |
| L    | 12   |
| M    | 13   |
| N    | 14   |
| Ñ    | 15   |
| O    | 16   |
| P    | 17   |
| Q    | 18   |
| R    | 19   |
| S    | 20   |
| T    | 21   |
| U    | 22   |
| V    | 23   |
| W    | 24   |
| X    | 25   |
| Y    | 26   |
| Z    | 27   |

***Paso 2***: Planteamiento del problema

Entrada

* Introducir una lista de palabras leyendo teclado, introducir todas en un array llamado lista.

Proceso

* Crear dos arrays, uno con numeros del 1 al 27 y otro con las letras del abecedario.
* Usar un subalgoritmo similar al usado en el ejercicio 5 para ordenar la lista de menor a mayor. Para ello se hará un array de cada una de las entradas de lista. Ej: madrid = (m,a,d,r,i,d) y se cambiará por su correspondiente valor en la lista.

Salida

* Imprimir la lista ordenada

***Paso 3***: Pseudocódigo

```
Algoritmo ordenar abc.

###

print("Introduzca una serie de palabras separadas por comas.")

val <-false
mientras val diferente de true, repetir

​	lista <- Leer(Teclado)

​	si lista solo tiene texto plano, entonces

​		val <- true

​	si no, entonces

​		print("Solo se admite texto")

​	fin si

fin mientras

###

n <- longitud(lista)

i <- 0

j <-0

h <- 0

k <- 0

l <- 0

letrasABC = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z]

valorABC = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

#Subalgoritmo de valores ABC

para i=0 hasta i=n, repetir con paso 1

​	lista(i) <- subAlg[Lista(i)] ## abc se convierte en (a,b,c)

​	para j = 0 hasta j = longitud(lista i)

​		para h = 0 hasta h = 26 repetir con paso 1

​			si lista(i(j)) = letrasABC(h), entonces

​				lista(i(j)) <- valorABC(h)

​				h <-27#break

​		si no, entonces

​			h <- h+1

​		fin si

​		fin para

​	j <- j+1

​	fin para

i <- i+1

fin para

#fin subalgoritmo

#en este punto ya tenemos todas las entradas con valor numérico ejemplo: abc = (1,2,3)

#Subalgoritmo ordenar

para k = 0 hasta k = n

​	para l = 0 hasta l = n-k-1

​		si lista(l(1)) mayor que lista(l+1(1)), entonces

​			lista(l), lista (l+1) <- lista(l+1), lista(l)

​		fin si

​		l <- l+1

​	fin para

k <- k+1

fin para

#Fin subalgoritmo ordenar

#En este momento ya tenemos toda la lista ordenada.

### Soy consciente de que solo tiene en cuenta la primera letra pero mis conocimientos terminan aquí :(

print(+lista)

```

###	11.Crea un algoritmo que calcule el factorial de un número entero.

***Paso 1:*** Definir el problema

Un factorial es el producto de él mismo por todos los números menores que él, terminando en uno. Se puede calcular con un algoritmo de matemática sencillo.

***Paso 2:*** Planteamiento del problema

Entrada

* Pedir que se introduzca un número entero

Proceso

* Empezando por el numero introducido, crear un bucle multiplicando resultado por su numero anterior.

Salida

* Dar el resultado

***Paso 3:*** Pseudocódigo

```
Algoritmo factorial

###

print("Introduzca un número entero")

val <- false

mientras que val distinta de true, repetir

​	numero <- (Leer)

​	si numero = numero entero, entonces

​		val <- true

​	sino, entonces

​		print("Solo se admiten números enteros")

​	fin si

fin hasta

###

i<- 0

si numero mayor o igual a 2, entonces // 4

​	para i=numero-1 hasta i=2; repetir

​		numero <- numero * i // 1º --> 4 * 3 = 12 (i=3); 2º --> 12 * 2 = 24 (i=2); 3º --> 24*1 = 24 (i=1, break) 

​		i <- i-1

​	fin repetir

si numero menor o igual a -2, entonces // -4

​	para i = numero+1 hasta i = -1, repetir

​		numero <- numero * i // 1º --> -4 * -3 = 12 (i=-3) ; 2º --> 12 * -2 = -24 (i=-2); 3º --> -24 * -1 = 24 (i=-1, break)

​		i <- i+1

​	fin repetir

fin si

###

print("El factorial de su número es" +numero)

Fin Algoritmo
```



###	12.Dado un número entero, crea un algoritmo que determine si es primo o no.

***Paso 1:*** Definir el problema

Un numero primo es aquel que solo es divisible por él mismo y por 1. Por tanto, si el resto de su división de ese número por cualquiera que no sea uno de los mencionados es 0, no es un numero primo. 

***Paso 2:*** Planteamiento del problema

Entrada

* Leer del teclado un numero entero

Proceso

* Realizar el algoritmo de cálculo con mod en bucle 

Salida

* Imprimir si el número es primo o no. 

***Paso 3:*** Pseudocódigo

```
Algoritmo primo

###

print("Introduzca un número entero")

val <- false

mientras que val distinta de true, repetir

​	numero <- (Leer)

​	si numero = numero entero, entonces

​		val <- true

​	sino, entonces

​		print("Solo se admiten números enteros")

​	fin si

fin hasta

###

i <- 0 

resultado <- primo

si numero igual o menor que -1, entonces

​	numero <- numero * (-1)

fin si

para i = numero -1 , hasta 2, repetir

​	si numero mod i = 0; entonces

​		resultado <- no primo		

​		i = 2 #break		

​	si no, entonces			

​		i <- i-1

​	fin si

fin repetir

###

print("El número que ha introducido es " +resultado)

Fin Algoritmo
```



###	13 Calcular el volumen de un cubo dado su lado

***Paso 1*** Definir el problema

Para calcular el volumen de un cubo lo único que necesitamos es introducir el lado y elevarlo al cubo, por lo que obtener su volumen debería ser bastante simple. El problema debería venir de seleccionar la unidad de medida que el usuario esté introduciendo.

***Paso 2*** Planteamiento

Para empezar crear una variable llamada lado y una variable llamada unidad. La variable lado se introduciría mediante teclado y la unidad mediante un desplegable, que debería crearse en una tabla. También se le debe dar la opción de en qué unidad quiere recibir el volumen. 

Crear variables: lado, unidadEntrada, unidadSalida, valorUnidadEntrada, valorUnidadSalida, volumen

Crear arrays: 

- unidadEntrada: [m, dm, cm, mm ]
- valorUnidadEntrada: [0,1,2,3]
- unidadSalida: [m3, dm3, cm3, mm,3 L]
- valorUnidadSalida: [0,1,2,3,4]

**Algoritmo** 

- Entrada:

​	Introducir lado (Teclado)

​	Introducir unidad de entrada (Desplegable)

​	Introducir unidad de salida (Desplegable)

- Proceso:

  Calcular volumen elevando lado al cubo

  Comprobar si quiere el volumen en la misma unidad, sí es así, print. 

  Si no es así, hacer el cambio de unidad. 

- Salida:

  Print "El volumen de su cubo es (volumen)(unidadSalida)" 

***Paso 3*** Pseudocódigo. 

```var lado```

```var unidadEntrada =[m,dm,cm,mm] ``` 

```var valorUnidadSalida = [0,1,2,3]``` 

```var unidadSalida = [m3, dm3, cm3, mm3, L]``` 

```var valorUnidadSalida = [0,1,2,3,4]``` 

```var volumen```

Algoritmo

**Entrada**

```Print ("Por favor introduzca el lado de su cubo")``` 

```lado <- Leer (Teclado)``` 

```unidadEntrada <- Leer (desplegable)```

```unidadSalida <- Leer (desplegable)```

**Proceso**

```valorUnidadEntrada <- Leer(Tabla)```

```valorUnidadSalida <- Leer(tabla)```

`if valorUnidadSalida = 4; valorUnidadSalida = 1 `

`fin if`

`volumen = lado^3`

`if valorUnidadEntrada = valorUnidadSalida; print("El volumen de su cubo es <Volumen><unidadSalida>")`

`ifnot volumen = volumen * 1000^(valorUnidadSalida - valorUnidadEntrada)` 

`endif`

**Salida**

`print("El volumen de su cubo es" +volumen +unidadSalida)`

###	14. Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

***Paso 1*** Descripción del problema

Un número par es aquel que es 0 o que es divisible entre dos. Por tanto, habría que pasar un primer bucle por los elementos de la lista y si n mod 2 !=0 ; n <- 0. Después pasar un bucle de suma de los elementos.

***Paso 2:*** Planteamiento del problema

Entrada

* Pedir que se introduzca una lista de números enteros, separados por comas, para crear un array

Proceso

* Ejecutar un subalgoritmo de depuración de los impares
* Ejecutar un subalgoritmo para sumar los elementos de la lista

Salida

Dar el resultado

***Paso 3:*** Pseudocódigo

```
Algoritmo suma pares

###

print ("Introduzca una serie de números enteros separados por comas")

val <- false

mientras que val diferente de true, repetir

listaNum <- Leer(Teclado)

​	si listaNum solo está conformada por números enteros, entonces

​		val <- true

​	si no, entonces

​		print("Solo se admiten números enteros")

​	fin si

fin mientras

###

i <- 0

para i=0 hasta i = longitud(listaNum), repetir

​	si listaNum(i) mod 2 es diferente a 0, entonces

​		listaNum(i) <- 0

​	i <- i+1

fin repetir

j <- 0

resultado <- 0

para j = 0 hasta j = longitud(listaNum), repetir

​	resultado <- resultado + listaNum(j)

fin repetir

###

print("La suma de los números pares introducidos en la lista es" +resultado)

Fin algoritmo
```



###	15.Crea un algoritmo que determine si un número es positivo, negativo o cero

***Paso 1:*** Definir el problema

Un problema realmente sencillo que se puede hacer con con un algoritmo "si" con múltiples condiciones

***Paso 2:*** Planteamiento del problema

Entrada

* Pedir que se introduzca un numero y comprobar que la entrada es un numero

Proceso

* Algoritmo si de dos condiciones

Salida

* Imprimir el resultado

***Paso 3:*** Pseudocódigo

```
Algoritmo positivo negativo 0

###

print("Introduzca un número.")

val <- false

mientras val diferente de true, repetir

​	num <- (Leer)

​	si num es un número, entonces

​		val <- true

​	si no, entonces

​		print("El valor introducido no es un número")

​	fin si

fin mientras

### 

resultado <- 0

si num es igual o mayor que 1, entonces

​	resultado <- positivo

si num es igual o menor que -1, entonces

​	resultado <- negativo

fin si

###

print("El número introducido es" +resultado)
```



###	16.. Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista

***Paso 1:*** Definir el problema

La media de una lista de números es la suma de todos estos números dividida por la cantidad de elementos de la lista, lo cual es un algoritmo realmente simple de escribir. 

***Paso 2:*** Planteamiento del problema

Entrada

* Pedir que se introduzca una lista de números enteros, separados por comas, para crear un array

Proceso

* Ejecutar un subalgoritmo que sume todos los números de la lista con un bucle 
* Dividir la suma por el numero de elementos de la lista. 

Salida

Dar el resultado

***Paso 3:*** Pseudocódigo

```
Algoritmo media

###

print ("Introduzca una serie de números enteros separados por comas")

val <- false

mientras que val diferente de true, repetir

listaNum <- Leer(Teclado)

​	si listaNum solo está conformada por números enteros, entonces

​		val <- true

​	si no, entonces

​		print("Solo se admiten números enteros")

​	fin si

fin mientras

###

i <- 0

total <-0

para i = 0 hasta i=longitud(listaNum), repetir

​	total <- total + listaNum(i)

​	i <- i+1

fin repetir

media <- total / longitud(listaNum)

###

print("La media de los elementos introducidos es" +media)

Fin Algoritmo
```

​	

###	17.Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto

***Paso 1:*** Definir el problema

Usando el comando rantint generamos el número aleatorio, y después acercamos al jugador a la respuesta con una serie de prints organizados por ints.

***Paso 2:*** Planteamiento del problema

Definir este algoritmo con entrada, proceso y salida es complicado, puesto que el programa comienza con la generación de un número aleatorio entre el 1 y el 100 y el comando de introducir un número viene dado dentro de un bucle para definir si el usuario ha adivinado el número.

1.- Generamos numero aleatorio

2.- Bucle que se repite hasta que el usuario acierte

​	2.1- Intenta adivinar

​	2.2. Si el intento es mayor, indicarlo

​	2.3. Si el intento es menor, indicarlo

​	2.4 Si el usuario acierta, indicarlo.

Como dije antes, entrada, proceso y salida se junta todo en la misma parte del algoritmo. 

***Paso 3:*** Pseudocódigo

```
Algoritmo adivinanzas

premio <- ranint(1,100) //Como esto no se ha visto en clase lo he buscado en Python porque se dijo que es un lenguaje simple

val <- false

mientras que val es distinta de true, repetir

​	guess <- Leer(Teclado)

​	si guess = premio, entonces

​		print("¡PREMIO!")

​		play("musicavictoria.mp3")

​		val <- true

​	si guess es mayor que premio, entonces

​		print("Casi casi, prueba a tirar un poquito más bajo")

​	si guess es menor que premio, entonces

​		print("Casi casi, un poquito más alto")

​	finsi

fin mientras

Fin Algoritmo
```



###	18.. Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

***Paso 1:*** Definir el problema

Que un texto sea un anagrama de otro significa que tiene las mismas letras. Esto se puede solucionar comparando dos cadenas.

***Paso 2:*** Planteamiento del problema

Entrada

* Pedir al usuario que introduzca dos cadenas de texto, sin caracteres especiales ni números.
* Comprobar que lo anterior sea correcto.

Proceso

* Transformar las entradas en cadenas mediante un subalgoritmo.
* Eliminar los espacios en blanco de ambas cadenas.
* Comparar ambas cadenas, con un primer bucle que pase por la primera cadena y lo compare con la cadena segunda. En caso de que la letra coincida, se transformará en un espacio en blanco en la segunda cadena. 
* Si la segunda cadena está compuesta enteramente por espacios en blanco, se tratará de un anagrama, si no, no.

Salida

Devolver el resultado.

***Paso 3:*** Pseudocódigo

```
Algoritmo anagrama

###

print("Introduzca una primera cadena de texto sin números o caracteres especiales")

val 1<- false

mientras que val 1 diferente de true, repetir

​	texto1 <- Leer(Teclado)

​	si texto1 es texto sin números o caracteres especiales, entonces

​		val1 <- true

​	si no, entonces

​		print("No se admiten números ni caracteres especiales")

​	finsi

fin mientras

print("Introduzca una segunda cadena de texto sin números o caracteres especiales")

val 2<- false

mientras que val 2 diferente de true, repetir

​	texto2 <- Leer(Teclado)

​	si texto2 es texto sin números o caracteres especiales, entonces

​		val2 <- true

​	si no, entonces

​		print("No se admiten números ni caracteres especiales")

​	finsi

fin mientras

###

cadena1 <- subalgCadena(texto1)

cadena2 <- sugalg(texto2)

#SubalgoritmoDepuración

para i = 0 hasta i=longitud(cadena1)

​	si cadena1(i) = "", entonces

​	eliminar(cadena1(i))

​	fin si

​	i <- i+1

fin para

para j = 0 hasta j=longitud(cadena2)

​	si cadena2(j) = "", entonces

​		eliminar(cadena2(j))

​	fin si

​	j <- j+1

fin para

#Fin subalgoritmo depuración

si longitud(cadena1) diferente longitud(cadena2), entonces

​	print("Los textos no son anagramas.")

para k=0 hasta k=longitud(cadena1), repetir // (a,j,o,s) y (s,o,j,a,s)

​	para l=0 hasta l=longitud(cadena2) 

​		si cadena1(k) = cadena2(l), entonces // (a,j,o,s) y (s,o,j,"",) -->  (a,j,o,s) y (s,o,"","",) --> (a,j,o,s) y (s,"","","") --> (a,j,o,s) y ("","","","")

​			cadena2(l) <- ""

​			l <- longitud(cadena2)#break

​		si no, entonces
			l <- l+1
		fin si

​	fin para

​	k <- k+1

fin para

contador <- 0

para m = 0 a m=longitud(cadena2), repetir

​	si cadena(2m) distinto de "", entonces

​		contador <- contador +1

​	finsi

​	m <- m+1

fin para

###

si contador = 0, entonces

​	print("Los textos son anagramas")

si no, entonces

​	print("Los textos no son anagramas")

fin si

Fin Algoritmo
```



###	19.Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

***Paso 1:*** Definir el problema

El programa se define a sí mismo en el anunciado del ejercicio

***Paso 2:*** Planteamiento del problema

Lo primero sería que el usuario introduzca su lista de números, después crear un bucle que vaya pasando por esa lista número por número eliminándolo si es igual a cualquier número igual al de esa lista. Como no se puede eliminar mientras se comprueba, se hace en un paso a parte y se pone como espacio en blanco mientras se modifica la cadena. 

Entrada

* Introducir una lista de números separados por comas y comprobar

Proceso

* Un primer bucle que pase por toda la lista, con otro bucle dentro que compare con el resto de la lista y ponga la entrada como "". Después eliminar todos los ""

Salida

* Devolver la lista ya depurada.

***Paso 3:*** Pseudocódigo

```
Algoritmo eliminación repetidos

###

print ("Introduzca una serie de números enteros separados por comas")

val <- false

mientras que val diferente de true, repetir

listaNum <- Leer(Teclado)

​	si listaNum solo está conformada por números enteros, entonces

​		val <- true

​	si no, entonces

​		print("Solo se admiten números enteros")

​	fin si

fin mientras

###

i  <- 0

j <- 0

para i=0 hasta i=longitud(listaNum), repetir

​	para j=i hasta j=longitud(listaNum), repetir

​		si listaNum(i) = listaNum(j+1) , entonces

​			listaNum(i) <- ""
			j <- longitud(listaNum) #break

​		fin si

​		j <- j+1

​	fin para

i <- i+1

fin para

k  <- 0

para k=0 hasta k = longitud(listaNum), repetir

​	si listaNum(k) = "", entonces,

​		eliminar(listaNum(k))

​	finsi

finpara

###

print("Su lista sin números repetidos sería")
print(+listaNum)

Fin Algoritmo
```



###	20.Crea un algoritmo que determine si un número es capicúa o no.

***Paso 1:*** Definir el problema

Que un número sea capicúa significa que se lee de la misma manera en ambos sentidos, similar al ejercicio de saber si una palabra es un palíndromo.

***Paso 2:*** Planteamiento del problema

Entrada

* Pedir que el usuario introduzca un número y comprobar que sea un número

Proceso

* Pasar por todos los números para saber si es igual al opuesto, si no es igual, no es capicúa. Si es igual al opuesto, es capicúa.

Salida

* Devolver el resultado de si es capicúa o no. 

***Paso 3:*** Pseudocódigo

```
Algoritmo capicua

###

print("Introduzca su numero.")

val<-false

hasta val = true, repetir

​	numero <- Leer(Teclado)

​	si numero = numero, entonces
​		val <- true

​	si no, entonces

​		print ("Solo se admiten numeros")

​	finsi

fin hasta

###

arrayNum <- convertirArray(num)

n=longitud(arrayNum)

resultado <- "es capicúa"

i<-0

para i=0, repetir hasta i=n

​	si arrayNum (i) es diferente de arrayTexto(n-i), entonces

​		resultado<- "no es capicúa"

​		i <- n #break

​	si no, entonces

​		i <- i+1

​	finsi

fin para

###

print("El número" +num +resultado)

Fin algoritmo


```



























​	





```longitudNif = 8