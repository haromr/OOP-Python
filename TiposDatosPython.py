print("""
En Python Existen 5 tipos simples de variables
-----------------------------------------------
int
string
Boolean
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



   




