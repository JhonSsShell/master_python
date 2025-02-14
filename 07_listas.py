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