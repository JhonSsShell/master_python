# Funciones y las builting functions
# ?  Declaracion de una funcion basica, se utiliza la palabra reservada def
def saludar() -> None:
  print("Hola desde una funcion")

# Llamar a la funcion para ejecutarla
saludar()

# ? Funcion con parametro
def saludo(nombre: str) -> None:
  print(f"Hola {nombre} mucho gusto")

# Llamar la funcion
saludo(str("Jhon"))

# ? Funcion con multiples parametros, recibe dos numeros enteros
def sumar(a: int, b: int) -> int:
  return a + b

# Se hace llamado a la funcion y como retorna un valor se imprime directamente
print(sumar(int(15), int(25)))

# ? Funcion con parametros opcionales
def presentar(nombre: str = "Invitado") -> None:
  print(f"Bienvenido {nombre}")

# Llamar la funcion sin enviar un parametro, imprime la variable -> invitado
presentar()

# Llamar la funcion enviandole el parametro, imprime la variable -> Jhon
presentar("Jhon")

# ? Funcion con parametro arbitrales
# E8sta funcion recibe cierta cantidad de parametros, desde que sean numeros
def sumar_todo(*numeros: int)-> int:
  return sum(numeros) # Retorna la suma de todos esos numeros entrantes

# Llamar la funcion y imprimir las suma de todo ellos
print(sumar_todo(1,2,3,4,5,6,7,8,9,10))

# ? Funcion con parametros kwargs
# Esta funcion convierte los parametros como clave valor es decir si le paso 3 argumentos, espera a tenerlos todos y los convierte en un diccionario
def mostrar_info(**datos)-> None:
  for clave, valor in datos.items():
    print(f"Clave {clave} -> {valor}")

# Llamar la funcion y pasarle dato por dato
mostrar_info(nombre="Jhon", edad=19, ciudad="Bucaramanga")

# ? Funciones con retorno
# Una funcion que retorna algun valor independientemente de lo que retorne
def cuadrado(numero: int) -> int:
  return numero**2

# Llamar la funcion y pasarle el numero a calcular
print(cuadrado(int(25)))

# ? Funciones recursivas
# Estas funciones son de esas que se llaman a si misma
def factorial(n: int) -> int:
  if n == 1:
    return 1
  return n * factorial(n - 1)

# Llamar la funcion recursiva y imprimir el retorno en consola
print(factorial(4))

# ? Funciones lambda
# Es una forma de escribir funciones en una linea que recibe un parametro x, y retorna ese parametro multiplicado * 2
doblar = lambda x: x * 2

# Imprimir el valor de retorno de la funcion
print(doblar(4))

# Lista para el ejemplo con el map
numeros = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Funcion lambda para mapear los elementos del listado de numeros
doblados = list(map(lambda x: x * 2, numeros))

# Funcion lambda para mapear y retornar los numeros pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimir los valores de las funciones lambda
print(pares)
print(doblados)

# ? Funciones en built-it en python
# Funciones matermaticas
print(abs(int(-5))) # Valor absoluto de -5 -> Salida -> 5
print(round(float(3.6))) # Redondear al entero mas cercano hacia arriba -> Salida -> 4
print(pow(2, 3)) # Elevar al cubo el 2 -> Salida -> 8

# Conversiones de tipos
print(int("54")) # Convierte la cadena a numero entero -> Salida -> 54
print(float("4.5")) # Convierte la cadena a numero flotante -> Salida -> 4.5
print(str(100)) # Convierte el numero a cadena de texto -> Salida -> "100"

# Funciones sobre listas y seuencias
numbers = list([3, 1, 4, 5, 2, 4, 3, 4])
print(len(numbers)) # Imprime la longitud de la lista -> Salida -> 8
print(sorted(numbers)) # Imprime la lista pero ordenada -> Salida [1, 2, 3, 3, 4, 4, 4, 5]
print(sum(numbers)) # Imprime la suma de sus elementos -> Salida -> 26

# Funciones de cadenas de textos
text = str("Hola mundo desde Python")
print(len(text)) # Salida -> 26
print(text.upper()) # Salida -> HOLA MUNDO DESDE PYTHON
print(text.lower()) # Salida -> hola mundo desde python
print(text.replace("Python", "Java")) # Salida -> Hola mundo desde Java

# Funciones de diccionarios
datos = dict({
  "nombre": "Jhon Carreño",
  "edad": 19
})
print(datos.keys()) # Retorna el arreglo de las claves del diccionario -> Salida -> ["nombre", "edad"]
print(datos.values()) # Retorna el arreglo de los valores del diccionario -> Salida ->  ["Jhon Carreño", 19]

# Funciones de los conjuntos
conjunto = {1, 2, 3}
conjunto.add(4) # Agrega un nuevo elemento al conjunto
print(conjunto)

# Funciones de entrada y salid
name = input("Ingrese el nombre del usuario: ")
print(f"Hola {name} como estas?")
