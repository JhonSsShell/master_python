# Aprendizaje basico de los bucles en python
# ? Bucle for

# Este bucle se utiliza mas que todo cuando se sabe cuantas veces se debe iterar cierta cosa
for i in range(5):
  print(i) # Imprime los numeros del 0 al 4

# ? Iterando sobre las listas
# Declarar una lista para recorrerla
frutas = list(["Manzana", "Pera", "Fresa", "Mora"])

# Recorrer con un for, la cantidad de frutas que existen y imprime cada fruta en consola
for fruta in frutas:
  print(fruta)

# ? Iteracion sobre cadenas de texto
# Declaracion de una variable de texto
mensaje = str("Mensaje")

# El bucle for itera por cada letra de la variabel mensaje en este caso imprime -> M e n s a j e -> Linea por linea
for i in mensaje:
  print(i)

# ? Ejemplo de for con range("start", "stop", "step")

# Bucle for, en el cual con el range, se declara como primer parametro el estado inicial
# Hasta cuando debe parar y la cantidad de pasos, es decir de cuanto va a aumentar
for i in range(1, 10, 2):
  print(i)

# ? Iteracion sobre diccionarios
# Declaracion de un diccionario
info_person = dict({
  "nombre": "Jhon",
  "edad": 19,
  "ciudad": "Giron"
})

# Iterar sobre cada valor del diccionario, el metodo items, devuelve pares (clave -> valor)
for clave, valor in info_person.items():
  print(f"{clave} : {valor}")

# ? Bucle while
# Este bucle while se ejecuta siempre y cuando una ejecucion sea True
contador = int(0)

# Recorrer el bucle siempre y cuando el contador sea menor a 5
while contador < 5:
  print(f"Contador {contador + 1}") # Salida -> Contador 1, Contador 2 ...
  contador += 1 # Por cada iteracion aumentar el contador

# Se deben evitar los bucles infinitos los cuales son los siguientes
while True:
  print("Siempre se ejecuta hasta que se coloque un break");
  break

# ? Controlar un bucle con (break, continue y else)

# Controlar un bucle con break, el bucle se detiene cuando el iterador llega a 5
for i in range(10):
  if i == 5:
    print("Rompiendo el bucle en el numero 4")
    break
  print(i)

# Saltar iteraciones con un continue
for i in range(10):
  if i == 6:
    print(f"Saltando el numero {i}")
    continue
  print(i)

# El bucle else se ejecut si el loop no tiene un break, es decir si se coloca un break en el for es innecesario utilizar el else
for i in range(10):
  print(i)
else:
  print("Bucle terminado")

# ? Bucles anidados
# Bucle dentro de un Bucle, esto es mas necesario cuando se trabaja con una matriz
for i in range(5):
  for j in range(5):
    print(f"i = {i} -> j = {j}") # Se debe tener en cuenta que si va en la posicicion 0 la i se ejecuta primero las 5 veces el j

# ? Utilizando bucles de manera avanzada
# Variable de una lista con nombre de personas
nombres = list(["Ana", "Luis", "Jhon", "Alfredo"])

# Bucle con enumerate() el metodo retorna un indice -> 0 y un valor -> Ana
for index, nombre in enumerate(nombres):
  print(f"Posicion = {index} -> {nombre}")

# Variables para ejemplo con bucle zip
nombres_personas = list(["Andres", "Kevin", "Andrea", "Felipe"])
edades = list([19, 20, 14, 19])

# El bucle con Zip toma los dos arreglos eneste caso y que hace toma las primeras posiciones de los arreglos y los setea en el bucle
for nombre, edad in zip(nombres_personas, edades):
  print(f"{nombre} tiene {edad} años")

# ? List Comprehension (Loops en una sola linea)
# Buclea de una sola linea
cuadrados = list([x**2 for x in range(5)]) # Eleva la posicion de la iteracion al cuadrado
print(cuadrados)

# Tambien se puede aplicar ese bucle con una condicional
pares = list([x for x in range(10) if x % 2 == 0]) # Esta manera es mas eficiente que agregarlos con un .append
print(pares)