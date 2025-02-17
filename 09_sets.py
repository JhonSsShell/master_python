# Sets en python
# ? Creacion de un set vacio
mi_set = set() # Esta es la manera correcta de poder crear un set en python, ya que si se crea con "{}" python interpreta esto como un diccionario

# Set con valores
mi_set = {1, 2, 3, 4, 5}
print(mi_set)

# Set con diferentes tipos de datos
mi_set = {True, "Hola", "Python", 3, False} # Tiene una particularidad y es que no se pueden agregar diccionarios o listas en el set

# ? Metodos y operaciones con los sets
# Agregar elementos al set
mi_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
mi_set.add(10)
print(mi_set) # Salida -> (1, 2, 3, 4, 5, ..., 10)

# Eliminar elementos de un set
mi_set.remove(5) # Si no se encuentra este elemento en el set, genera un error
mi_set.discard(10) # No genera un error si no encuentra el elemento

elemento = mi_set.pop() # Este metodo elimina un elemento aleatorio del set
print(mi_set)

# Vaciar un set
mi_set.clear()
print(mi_set)

# ? Operaciones entre sets
# Uniones entre sets
set_a = {1, 2, 3}
set_b = {3, 4, 5, 6}
print(set_a | set_b) # Primer manera de realizar una union entre sets
print(set_a.union(set_b)) # Segunda manera de realizar un union entre sets

# Interseccion entre los sets
print(set_a & set_b) # Encuentra las coincidencias que existen entre el set_a y el set_b
print(set_a.intersection(set_b)) # En este ocurre lo mismo pero de una manera diferente

# Diferencias entre los sets
print(set_a - set_b) # Busca los elementos que estan en set_a pero no en set_B
print(set_a.difference(set_b)) # Realiza lo mismo solo que con una sintaxis diferente

# Diferencias simetricas
print(set_a ^ set_b) # Busca los elementos que estan en los sets, pero no en ambos
print(set_a.symmetric_difference(set_b)) # Realiza lo mismo

# ? Otras operaciones importantes para los sets
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5, 6}
print(set_a.issubset(set_b)) # Verifica si un set es un subconjunto de otro

print(set_b.issuperset(set_a)) # Verifica si un set es un superconjunto de otro

set_c = {7, 8, 9}
print(set_a.isdisjoint(set_c)) # Veriifica si los sets no tienen elementos en comun

# ? Recorrer un set
mi_set = {"Pyhton","Java","C++"}
for language in mi_set:
  print(language)

# ? Convertir entre listas tuplas y sets
mi_lista = list([1, 2, 2, 2, 3, 3,4, 5, 4, 5, 7, 4, 4,2])
mi_set = set(mi_lista) # Convertir la lista en un set
print(mi_set)

# Convertir de set a tupla o lista
mi_tupla = tuple(mi_set)
mi_lista = list(mi_set)

# ? Sets inmutables
set_inmutable = frozenset([1,0,9,9,7,3,7,5,0,1])
# set_inmutable.add(2) # Esto genera un error, ya que no se puede cambiar