# Tuplas en python
# ? Crear tuplas en python
tupla_vacia = () # Manera 1 de crear una tupla vacia
tupla_vacia = tuple() # Manera 2 de crear una tupla vacia

# Tupla con elementos
mi_tupla = (1, 2, 1, True, "Adios")
mi_tupla = (False, "Angel")

# Tupla de un solo elemento
tupla_uno = (5, )
print(type(tupla_uno))

# ? Acceder a elementos de una tupla
tupla = (10, 20, 30, 40, 50)
print(tupla[0]) # Acceder a la primera posicion de la tupla
print(tupla[-1]) # Acceder a la ultima posicion de la tupla

# Usando el slice
print(tupla[1:3]) # Toma la posicion 1 y 2 de la tupla
print(tupla[:2]) # Toma las 2 primeras posiciones de la tupla
print(tupla[2:]) # Toma las 3 ultimas posiciones de la tupla
print(tupla[::-1]) # Invertir el orden de la tupla

# ? Tuplas anidad
tupla_anidada = ((1, 2, 3), (4, 5, 6))
print(tupla_anidada[0]) # Accede a la primer tupla -> Salida -> (1, 2, 3)
print(tupla_anidada[1][1]) # Accede a la segunda tupla con la segunda posicion de la tupla es decir -> Salida -> 5

# ? Metodos basicos de las tuplas
'''
  count(x) -> Devuelve cuantas veces aparece x en la tupla
  index(x) -> Devuelve el indice de la primera aparicion de x
'''
my_tupla = (1, 2, 3, 4, 5, 4, 1, 2, 1, 3, 4)
print(my_tupla.count(1)) # Devuelve la cantidad de veces que existe en la tupla el numero 1 -> Salida -> 3
print(my_tupla.index(5)) # Devuelve la posicion de donde se encuentra la primera aparicion de ese numero 5 -> Salida -> 4

# ? Recorrer una tupla
# Con un for
tupla_languages = ("Python", "Java", "C++", "JavaScript")

for language in tupla_languages:
  print(language) # Imprime el lenguaje de programacion que se encuentra en la tupla

# Con un enumerate
for indice, valor in enumerate(tupla_languages):
  print(f"Indice -> {indice}, Valor -> {valor}") # Devuelve la posicion y el valor de esa posicion

# ? Convertir enter tuplas y listas
# Convertir tupla en lista
tupla_convertir = (1, 2, 3)
mi_lista = list(tupla_convertir) # Convierte la tupla a una lista
mi_lista.append(4) # Agregar el 4 en la ultima posicion de la lista
print(mi_lista) # Imprime la lista con el ultimo elemento agregado

nueva_tupla = tuple(mi_lista) # Convierte la lista en una tupla
print(nueva_tupla) # Imprime la la tupla

# ? Desempaquetados de tuplas
tupla_des = (1, 2, 3)
a, b, c = tupla_des # Realizar una destructuracion de la tupla
print(f"Valor a -> {a}, Valor b -> {b}, Valor c -> {c}") # Imprimir los valores de la destructuracion de la tupla

tupla_nueva = (1, 2, 3, 4, 5, 6, 7, 8, 9)
d, *e, f = tupla_nueva # El restante es decir -> [2, 3, 4, 5, 6, 7, 8] -> Lo toma la variable e, ya que d toma la primera posicion y f toma la ultima
print(f"Valor d -> {d}, Valor e -> {e}, Valor f -> {f}") # Imprime los valores de d, e como un arreglo y f

# ? Operaciones con tuplas
tupla_one = (1, 2, 3)
tupla_two = (4, 5, 6)
tupla_unida = tupla_one + tupla_two # Une ambas tuplas y las coloca en una sola
print(tupla_unida) # Imprime la tupla unidad -> Salida -> (1, 2, 3, 4, 5, 6)
  
# Repeticion
tupla_repetida = (0,1) * 5 # Replica la tupla 5 veces y los coloca en la misma tupla
print(tupla_repetida) # Imprime la tupla replicada

# Pertenencia
pertenencia_tupla = (10, 20, 30)
print(20 in pertenencia_tupla) # Verifica si el 20 existe en la tupla, si existe retorna True si no False
print(40 not in pertenencia_tupla) # Verifica si el 40 no existe en la tupla, si no existe retorna True si no False