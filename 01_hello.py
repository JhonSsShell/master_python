from colorama import Fore, Style

# El hola mundo desde python
print("Hola mundo desde Python")

# Imprimir otro mensaje en la consola
print("Esto es otro mensaje en consola ")

# Este es el ultimo mensaje de la consola
print("Mensaje final de python para mostrarlo en la consola")

# Imprimir multiples mensajes separados por coma
print("Hola", "Mensaje", "Separado", 3)

# Imprime en consola pero no separa por espacios si no por guiones
print("Mensaje", "Separado", "Por", "Guiones", sep="-")

# Toma un salto de linea y toma el ultimo print
print("Hola", end=" ")
print("Mundo")

# Con el format puedo colocar los datos en el orden como estan las "{}"
print("Hola mi nombre es {} y tengo {} años".format("Jhon", 19))

# Concatenar string con variables
print(f"Mi nombre es {"Jhon"} y tengo {19} años")

# El \n genera un salto de linea con el otro mensaje
print("Linea 1 \n Linea 2")

# Imprimir sin salto de linea
print("Hola", end="")
print(" Mundo")

# Crea un archivo y lo coloca en el directorio local donde lo esta creando
with open("salida.txt", "w") as archivo:
  print("Este texto ira a un archivo", file=archivo)


# Imprimir en la terminal con colores
print(Fore.RED + "Este texto es rojo")
print(Fore.GREEN + "Este texto es verde")
print(Fore.YELLOW + "Este texto es amarillo")
print(Style.RESET_ALL)