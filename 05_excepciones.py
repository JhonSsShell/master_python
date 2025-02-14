# Manejo de excepciones con python utilizando el try: except:
# ? Manejo basico de una excepcion en python
# Suponiendo que el usuario no sabe que no se puede dividir por 0, se controla con un error aritmetico que es "ZeroDivisorError"
try:
  print(5 / 0)
except ZeroDivisionError:
  print("No se puede dividir por 0")

# ? Captura de multiples errores
# Manejo de varias excepciones diciendole al usuario que ingrese un numero
try:
  numero = int(input("Ingrese el numero: ")) # Pedir al usuario que ingrese un numero
  print(f"El resultado es {10 / numero}") # Si es diferente a 0 divide con 10
except ZeroDivisionError:
  print("No se puede dividir por cero") # Si ingresa el 0 retorna el error
except ValueError:
  print("No ingresaste un numero valido") # Si ingresa una letra, retorna el error

# ? Capturar cualquier error con exception
try:
  print(10 / 0)
except Exception as e:
  print(f"Error al dividir por 0: {e}")

# ? Uso del else y el finally en el manejo de las excepciones
try:
  num = int(input("Vuelve a ingresar otro numero: "))
  resultado = float(10 / num)
except ZeroDivisionError:
  print(f"Error, no se puede dividir por 0")
except ValueError:
  print("Ingresaste algo que no es un numero")
else:
  print(f"El resultado de la division es: {resultado}") # Si no hay errores se imprime el resultado en la consola
finally:
  print("Este bloque siempre se ejecuta exista o no un error") # Este codigo siempre se ejecuta exista o no un error en el programa 

# ? Retornando errores con raise
# Crear una funcion para verificar las edades y lanzar un error con el raise
def verificar_edad(edad):
  if edad < 18:
    raise ValueError("No puedes acceder, eres menor de edad")
  return "Accesso permitido"

# Manejo de la funcion
try:
  print(verificar_edad(17))
except ValueError as e:
  print(f"Error -> {e}")

# ? Personalizacion de las excepciones
# Se crea una clase para poder capturar el error personalizado
class MiError(Exception):
  pass

# Se maneja la excepcion y el error personalizado
try:
  raise MiError("Esto es un error personalizado")
except MiError as error:
  print(f"Se capturo el error {error}")

# ? Tipos de excepciones
'''
  ZeroDivisionError -> Division por 0 (numero / 0)
  ValueError -> Conversion invalida (int("hola"))
  TypeError -> Operacion entre tipos incompatibles (5 + "hola")
  IndexError -> Indice fuera de rangos de listas (lista[10])
  KeyError -> Clave inexistente en un diccionario (dict["clave"])
  FileNotFoundError -> Archivo no encontrado
  AttributeError -> Intento de acceder a un atributo inexistente
'''