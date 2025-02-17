# Escribe un programa que pida un número al usuario e indique si es par o impar.
# def numero_par(numero: int) -> None:
#   if numero % 2 == 0:
#     print("Es par")
#     return
#   print("Es impar")

# number = int(input("Ingrese el numero: "))
# numero_par(number)

# Pide dos números al usuario e imprime cuál es el mayor o si son iguales.
# def major_number(numberOne: int, numberTwo: int) -> None:
#   if number_one > number_two:
#     print(f"El numero -> {numberOne} es mayor que -> {number_two}")
#     return
#   print(f"El numero -> {numberTwo} es mayor que -> {numberOne}")

# number_one = int(input("Ingrese el numero 1 -> "))
# number_two = int(input("Ingrese el numero 2 -> "))
# major_number(number_one, number_two)

# Escribe un programa que pida dos números, los sume y muestre el resultado en pantalla.
# def sum_numbers(numOne: int, numTwo: int) -> None:
#   print(f"El resultado de los dos numeros es -> {numOne + numTwo}")

# numberOne = int(input("Ingrese el numero 1 -> "))
# numberTwo = int(input("Ingrese el numero 2 -> "))
# sum_numbers(numberOne, numberTwo)

# Pide al usuario una palabra e imprime cuántas letras tiene.
# def count_letters(word: str) -> None:
#   print(f"La palabra tiene -> {len(word)} caracteres")

# pad = input("Ingrese la palabra a calcular la longitud -> ")
# count_letters(pad)

# Pide un número al usuario e imprime su tabla de multiplicar del 1 al 10.
# def table_mult(number: int) -> None:
#   for i in range(10):
#     print(f"{number} X {i + 1} -> {(i + 1) * number}")

# num = int(input("Ingrese el numero para la tabla -> "))
# table_mult(num)

# Escribe una función que calcule el factorial de un número ingresado por el usuario.
def factory(num: int) -> int:
  if num == 1:
    return 1
  return num * factory(num - 1)

number = int(input("Ingresa el numero a sacar factorial -> "))
print(factory(number))