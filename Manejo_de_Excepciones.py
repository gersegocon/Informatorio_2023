"""
Escribe un programa Python que incita al usuario a introducir un número entero y plantea una excepción de ValueError si la entrada no es un número entero válido.
"""

n = input("Ingrese un número entero: ")

try:
  int(n)
except ValueError:
  print("Ingreso un valor erroneo!")
else:
  print("Número entero valido!")

""". Escribe un programa Python que incita al usuario a introducir dos números y aumenta una excepción de TypeError si las entradas no son numéricas."""

n1 = input("Ingrese el 1° número: ")
n2 = input("Ingrese el 2° número: ")
lista = [n1, n2]

for i in lista:
  try:
    float(i)
  except ValueError:
    print(f"Lo ingresado para el {lista.index(i)+1}° número no es númerico!")

# try:
#   float(n2)
# except ValueError:
#   print("Lo ingresado para el 2° número no es númerico!")

""". Escribe un programa Python que ejecuta una operación en una lista y maneja una excepción de IndexError si el índice está fuera de rango."""

from random import randint
lista = [i for i in range(0, randint(0,100), randint(1,20))]
x = randint(0,20)
try:
  lista[x]
except IndexError:
  print("El indice actual obtenido no se encuentra en la lista")
else:
  print(f"El elemento correspondiente al indice {x} es {lista[x]}")

""". Escribe un programa Python que incita al usuario a introducir un número y maneja una excepción de KeyboardInterrupt si el usuario cancela la entrada."""

try:
  num = input("Ingrese un numero: ")
  if not num.isdigit():
    raise ValueError("Debe ingresar un valor númerico")

except ValueError as e:
  print(e)
except KeyboardInterrupt:
  print("\nEntrada cancelada por el usuario.")

""" Escribe un programa Python que ejecuta la división y maneja una excepción de ArithmeticError si hay un error aritmético.

"""

n1 = input("Ingrese un número: ")
n2 = input("Ingrese otro número: ")

try:
  if not n1.isdigit() or not n2.isdigit():
    raise ValueError("Los valores ingresados deben ser númericos")

  elif int(n2) == 0:
    raise ZeroDivisionError("El 2° valor no debe ser 0")
except (ValueError, ZeroDivisionError) as e:
  print("\nError: ",e)

""". Escribe un programa Python que ejecuta una operación de lista y maneja una excepción de AtributeError si el atributo no existe."""



""". Escribe un programa Python que abre un archivo y maneja una excepción de UnicodeDecodeError si hay un problema de codificación."""