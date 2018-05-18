print("""
En Python Existen algunos tipos simples de variables
-----------------------------------------------
int
string
Boolean
Set
List
Dictionary
""")

# esto es una cadena
c = "Hola Mundo"

# int 
Numeros_Enteros ="""
Los números enteros son aquellos que no tienen decimales, tanto positivos como negativos (además del cero). 
En Python se pueden representar mediante el tipo int (de integer, entero) o el tipo long (largo). 
La única diferencia es que el tipo long permite almacenar números más grandes. 

El tipo long de Python permite almacenar números de cualquier precisión, limitado por la memoria disponible en la máquina.
Al asignar un número a una variable esta pasará a tener tipo int, 
a menos que el número sea tan grande como para requerir el uso del tipo long.
"""

# y esto es un entero
e = 23

# La funcion type nos permite comprobar el tipo de una variable
type(c)
type(e)
print(type(c))

# Python no requiere que se defina el tipo de variable al momento de declararlas

# De esta manera se declararian la variables en JAVA
    # String c = "Hola Mundo";
    # int e = 23;
    
# Si se le asinga un numero, una variable toma como tipo "int"     
# type(entero) devolvería int
entero = 23     

# Podemos indicar a Python que un número se almacene usando long añadiendo una L al final:
# type(entero) devolvería long
entero = 23L

# La variable también se puede expresar como un octal, anteponiendo un cero:
# 027 = 23 en base 10
entero = 027

# o bien en hexadecimal, anteponiendo un 0x:
# 0x17 = 23 en base 10
entero =  0x17

# String
""" Las cadenas no son más que texto encerrado entre comillas simples (‘cadena’) o dobles (“cadena”). 
Dentro de las comillas se pueden añadir caracteres especiales escapándolos con ‘\’, como ‘\n’, el carácter de nueva línea, o ‘\t’, el de tabulación.
"""

# Las cadenas también admiten operadores como la suma (concatenación de cadenas) y la multiplicación.

a = "uno"
b = "dos"
c = a + b # c es "unodos"
c = a * 3 # c es "unounouno"  

# Comillas simples
cadenaa = 'Texto entre comillas simples'
print(cadenaa)
print(type(cadenaa))

# Comillas dobles
cadenab = "Texto entre comillas dobles"
print(cadenab)
print(type(cadenab))

# Cadena con codigo escapes
cadenaesc = 'Texto entre \n\tcomillas simples'
print(cadenaesc)
print(type(cadenaesc))

# Cadena multilinea
cadenac = """Texto linea 1
linea 2
linea 3
linea 4
.
.
.
.
.
linea N
"""

print(cadenac)
print(type(cadenac))

# Repeticion de cadena
cadrep = "Cadena" * 3
print cadrep
print type (cadrep)

# Concatenacion de cadena
nombre = "Leonardo"
apellido = "Caballero"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
print type((nombre_completo))

print("Tamano de cadena '", nombre_completo, "' es:", len(nombre_completo))

# acceder a rango de la cadena
print(nombre_completo[3:13])

# Bool
"""
el tipo booleano sólo puede tener dos valores: True (cierto) y False (falso). 
Estos valores son especialmente importantes para las expresiones condicionales y los bucles, como veremos más adelante.
"""

Verdadero = True
Falso = False

aT = True
print("El valor es Verdadero:", aT, ", el cual es de tipo", type(aT), "\n")
aF = False
print("El valor es Falso:", aF, ", el cual es de tipo", type(aF))

# set
"""
Un conjunto, es una colección no ordenada y sin elementos repetidos.  
Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas.
"""

comida = {'arroz', 'habichuelas', 'arroz', 'carne', 'carne', 'queso'}
print(comida)
print(type(plato))

bebida = {'refresco', 'malta', 'jugo', 'cafe'}
print(bebida)
print(type(bebida))

# notese que los datos duplicados no se muestran 

# establece un conjunto a una variable
para_comer = set(comida)
print(para_comer)

para_tomar = set(bebida)
print(para_tomar)

# Listas
"""
La lista en Python son variables que almacenan arrays, internamente cada posición puede ser un tipo de datos distinto.
"""

a = ['pan', 'huevos', 100, 1234]
print(a)

l = [2, "tres", True, ["uno", 10]]
print(l)

# Accesar a un elemento especifico
l2 = l[1]
print(l2)

# Accesar a un elemento dentro de una lista anidada
l3 = l[3][0]
print(l3)

# establecer nuevo valor de un elemento de lista
l[1] = 4
print(l)
l[1] = "tres"

# Obtener un rango de elemento especifico
l3 = l[0:3]
print(l3)

# Obtener un rango con saltos de elementos especificos
l4 = l[0:3:2]
print(l4)

l5 = l[1::2]
print(l5)




