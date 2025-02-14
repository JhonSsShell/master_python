# Declarar variable tipo String
nombre = "Jhon"

# Declarar variable tipo Integer
edad = 19

# Declarar variable tipo Float
altura = 1.84

# Declarar varibale tipo Boolean
es_estudiante = True

# ? Tipo de datos numericos
# Numeros enteros, estos se destacan por ser numeros como su nombre lo indica, enteros no decimales
numero_entero = 118

# Numeros decimales, estos se destacan por se numeros decimales, aqui se utiliza un . para declarar decimales
numero_flotante = 1478.2

# Numeros complejos, estos son numeros reales e imaginarios
numero_complejo = 2 + 3j

# ? Puede convertir un valor de string siempre y cuando su valor en string sea un numero
# En este caso convierte el string a numero entero
numero_string = int("2")

# Convierte el string a numero flotante
numero_flotante_string = float("4.8")

# ? Cadenas de texto
# Estas son cadenas de texto sencillas, no multilineas
mensaje = "Esto es una cadena de texto"
nombre = "Python"

# Estas son cadenas multiples de texto es decir multilinea
multiline = '''
  Esta es una variable de texto
  que es multilinea, pero funciona
  igual que una sencilla
'''

# ? Tipo de dato Booleano, sencillamente esto se basa en un True o un False
adulto = True
permiso = False

# Existe una particularidad y es que en python los booleanos se comportan como numeros
print(True + True) # Salida -> 2
print(False + True) # Salida -> 1
print(False * 5) # Salida -> 0

# ? Colecciones en python
# Declaracion de una nueva coleccion en python
skills = ["HTML", "CSS", "JS", "TS", "React", "NextJs", "PostgreSql", "ExpressJs", "Java", "SpringBoot", "Python"]

# Est variable toma la primera posicion de la coleccion
primera_posicion = skills[0]

# Esta variable toma la ultima posicion de la coleccion
ultima_posicion = skills[-1]

# Esta variable pone en reversa el posicionamiento de los elementos
alreves = skills[::-1]

# Agregar un nuevo elemento a la lista con .append
skills.append("php")

# Modificacion de un valor de acuerdo a la posicion de ese elemento
skills[0] = "JSP"

# ? Este metodo sirve para casi todo, es la propiedad len, que le muestra la longitud a uno
# En este caso con las colecciones muestra la cantidad de posiciones que tiene la coleccion
longitud = len(skills)

# ? Objetos en python o mejor conocido como diccionarios
# Declaracion de un diccionario que almacena la informacion de una persona
info_persona = {
  "nombre": "Jhon",
  "edad": 18,
  "trabajo": True,
  "habilidades": ["React", "Python"]
}

# Modificar datos de un diccionario, debes ingresar por decirlo asi por su clave para poder modificar su valor
info_persona["nombre"] = "Jhon Carreño"

# ? Los set en python, no se declaran como en JS, si no que aqui simplemente son como una coleccion solo que
# ? No se repiten datos
# Declaracion de un nuevo set, en este set, imprime el 5 pero una unica vez igual con el 8
numeros = {1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8}

# ? En python como tal no existe algo que se pueda definir como una constante, sin embargo
# ? por convension las constantes se definen en mayusculas
# Constantes
PI = 3.141632
URL = "http://localhost:8080/api/v1/swagger-ui/index.html"
PORT = 8080