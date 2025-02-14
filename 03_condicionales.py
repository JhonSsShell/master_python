# Declaracion de variable para una condicional, que usa un tipado fuerte
edad = int(10)

# ? Evalua que si la primera condicion retorna un True, entre en ese bloque e ignora los otros
# ? De lo contrario entra a la segunda condicion y pasa lo mismo, si no cumple ninguna de los
# ? Dos entonces se va al else que seria por decirlo asi una condicion si no se cumple ninguna
if edad >= 18:
  print("Es mayor de edad")
elif edad >= 13:
  print("Es adolecente")
else:
  print("Es un menor de edad")

# ? Operadores de comparacion
'''
  == -> Igual a -> x == y
  != -> Diferente a -> x != y
  > -> Mayor que -> x > y
  < -> Menor que -> x < y
  >= -> Mayor o igual que -> x >= y
  <= -> Menor o igual que -> x <= y
'''

# Declaracion de una nueva variable para ejemplo de operadores de comparacion
num = int(10)

# Ejemplo con operador igual a
if num == 10:
  print("El numero es 10")

# Ejemplo con operador diferente a
if num != 5:
  print("El numero es diferente a 5")

# Ejemplo con operador mayor a
if num > 5:
  print("El numero es mayor que 5")

# ? Operadores Logicos
'''
  and -> Ambas condiciones deben ser "True" -> x > 5 and x < 10
  or -> Al menos una condicion debe ser "True" -> x > 5 or x < 3
  not -> Niega una condicion ("True" -> "False") -> not x > 5
'''

# Declaracion de una nueva variable para ejemplo de operadores logicos
nombre = str("Jhon")
tiene_licencia = bool(True)

dia = str("sabado")

llueve = False

# Ejemplo con and, las dos condiciones se deben cumplir
if nombre == "Jhon" and tiene_licencia == True:
  print("Puede conducir")

# Ejemplo con or, al menos una condicion se debe cumplir
if dia == "sabado" or dia == "domingo":
  print("Es fin de semana")

# Ejemplo con not, niega el True o False dependiendo el caso
if not llueve:
  print("Puedes salir con paraguas")

# ? Condicionales anidadas
edad_persona = int(25)
licencia = bool(False)

# Ejemplo de las condicionales anidadas
# Si se van a anidar muchas condiciones es mejor usar el operador logico "and"
if edad_persona >= 18:
  if licencia:
    print("Esta persona puede manejar")
  else:
    print("No tienes licencia, no puedes manejar")
else:
  print("Eres menor de edad no puedes manejar")

# ? Operadores ternarios
num_edad = int(19)

# Operador ternario
mensaje = str("Mayor de edad") if num_edad >= 18 else str("Menor de edad")

# ? Switch case en python mejor conocido como Match
color = str("verde")

# Estructura del match, se coloca un _, para identificar que es un valor por defecto si no se encuentra ninguno
match color:
  case "rojo":
    print("El color es rojo")
  case "azul":
    print("El color es azul")
  case _:
    print("Color desconocido")

# ? Valores evaluados como "False"
'''
  0 -> (cero) -> False
  "" -> (cadenas vacias) -> False
  [] -> (lista vacia) -> False
  {} -> (diccionario vacio) -> False
  None -> False
  False -> False
'''

# Ejemplo de valores evaluados como False
nombre = str("")

# Verifica si existe nombre, como es False, con el not lo vuelve True y se cumple la condicion
if not nombre:
  print("No ingresaste ningun nombre valido")

# ? Comparacion de cadenas
# Variables para el ejemplo
a = str("apple")
b = str("banana")

# Imprime por orden alfabetico True o False
print(a < b) # True (orden alfabetico)

# ? Ignorar mayusculas en una condicional o lo que sea
if "Python".lower() == "python":
  print("Las palabras son iguales")