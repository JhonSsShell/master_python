# Listas en python
# ? Definiendo una nueva lista
mi_lista = list([1, 2, 1, 4, 4, 5, 7])
print(mi_lista)

# ? Creacion de las listas en python
lista = list([]) # Esta es una manera de lista vacia 
lista = [] # Esta es otra manera de lista vacia

# ? Listas con valores
numeros = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
nombre = list(["Ana", "Andres", "Felipe", "Jhon"])
mixta = list([1, "Jhon", True, 3.14])

# ? Listar a partir de un rango
rango = list(range(5))

# ? Acceder a los elementos de una lista
lista = list(["a", "b", "c", "d"])
print(lista[0]) # Imprime el valor de la primera posicion del arreglo
print(lista[-1]) # Imprime el valor de la ultima posicion del arreglo
print(lista[1:3]) #  Imprime el valor de las posiciones 1 hasta la 3 excluyendo el 3
print(lista[::1]) # Imprime la lista pero al reves es decir empieza por la d

# ? Metodos importantes para los listados
my_list = list([1, 2, 3])
my_list.append(4) # Agregar un nuevo elemento en una posicion adicional
my_list.insert(1, 10) # Inserta el numero en la posicion 1 de la lista
my_list.extend([5, 6, 7, 8, 9]) # Agregar multiples elementos a la lista

my_list.remove(3) # Este elimina el primer elemento que tenga como valor 3
my_list.pop() # Elimina el ultimo elemento de la lista
my_list.pop(1) # Elimina el elemento en dicha posicion especificada
del my_list[0] # Elimina el primer elemento
my_list.clear() # Limpia o elimina toda la lista y queda vacia
print(my_list)

# ? Buscar elementos en una sola linea
lista_example = list([10, 20, 30, 40, 50])
print(20 in lista_example) # Verifica que el 20 exista en la lista, devuelve True o False dependiendo
print(lista_example.index(30)) # Devuelve la posicion del valor si lo encuentra, si no retorna el error
print(lista_example.count(40)) # Realiza un contador de la cantidad de veces que se encuentra en la lista

# ? Ordenar listas
lista_ordenar = list([3,1,4,3,4,5,8,9])
lista_ordenar.sort() # Ordena la lista de manera ascendente
print(lista_ordenar) # Imprime la lista, ordenada

# Tambien se puede ordenar de una manera descendente
lista_ordenar.sort(reverse=True) # Esto ordena la lista de manera descendente
print(lista_ordenar) # Imprime la lista ordenada, descendentemente

# Tambien se puede retornar una lista totalmente nueva si no quieres ordenar y modificar la original
print(sorted(lista_ordenar)) # Imprime la nueva lista, pero no la que ya existe

# ? Copiar las listas correctamente
lista_copy = list([1, 2, 3, 4, 5])
copia_lista = lista_copy.copy() # Con este metodo la lista se copia y se asigna a otra

# Existe otra manera de copiarla
copia_lista = lista_copy[:] # Esta es la otra manera de copiarla correctamente

# ? Recorrer una lista
lista_languages = list(["Python", "Java", "C++"])

# Con bucle for
for language in lista_languages: # Recorre la lista elemento, por elemento
  print(language) # Imprime el lenguaje de programacion

# Con bucle while
i = int(0) # Contador inicial para recorrer los elementos de la lista
while i < len(lista_languages):
  print(lista_languages[i]) # Imprime el elemento de la lista en la posicion donde vaya el contador
  i += 1 # Incremento del contador

# Con un enumerate
for indice, valor in enumerate(lista_languages): # El enumerate retorna el indice y el valor de la lista que se va a iterar
  print(f"Indice -> {indice}, Valor -> {valor}") # Imprimir la clave y el valor de la lista

# ? Listas por comprension (List comprehension)
numeros = [x for x in range(10)] # Crea una lista de numeros del 0 al 9
print(numeros) # Salida -> [0, 1, 2, 3, 4, ..., 9]

pares = [x for x in range(10) if x % 2 == 0] # Crear una lista con los numeros pares
print(pares) # Salida -> [0, 2, 4, 6, 8]

cuadrados = [x**2 for x in range(5)] # Crea una lista con numeros elevados al cuadrado
print(cuadrados) # Salida -> [0, 1, 4, 9, 16]

# ? Mas funciones utiles
lista_adicional = list([3, 4, 5, 7, 8, 4, 1, 7, 9, 7])
print(max(lista_adicional)) # Imprime el numero mayor de la lista -> Salida -> 9
print(min(lista_adicional)) # Imprime el numero menor de la lista -> Salida -> 1
print(len(lista_adicional)) # Imprime la longitud que tiene la lista -> Salida -> 10
print(sum(lista_adicional)) # Imrpime la suma de los valores de la lista -> Salida -> 55

# ? Unir listas de una manera adecuada
lista_a = list([1, 2, 3, 4, 5])
lista_b = list([6, 7, 8, 9, 10])
lista_unida = lista_a + lista_b # Une las dos listas no importa de lo que sea
print(lista_unida) # Imprime la lista unificada -> Salida -> [1, 2, 3, 4, 5, 6, ..., 10]

# ? Resumen sobre las lista
'''
  append(x) -> Agrega x al final
  insert(i, x) -> Inserta x en la posicion i
  remove(x) -> Elimina x
  pop(i) -> Elimina el elemento en la posicion i
  clear() -> Vacia la lista
  index(x) -> Encuentra el indice de x
  count(x) -> Cuenta las ocurrencias de x
  sort() -> Ordenar la lista
  reverse() -> Invierte el orden de la lista
  copy() -> Clona perfectamente una lista
'''