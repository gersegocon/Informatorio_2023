# Ejercicio 1
# Crea una clase Persona con los atributos nombre, apellido y edad.
# Crea un método para saludar que recibiendo otro objeto de la clase Persona
# muestre un mensaje de saludo para esa persona.
# Crea un método para presentarse.
# Crea dos objetos de la clase Persona
# y llama a los métodos creados.
# La salida debe ser algo así:
# Juan: Hola!
# Juan: Mi nombre es Juan Perez y tengo 25 años.
# Maria: Hola Juan!
# Maria: Mi nombre es Maria Garcia y tengo 30 años.

class Persona():

  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def saludar(self, persona):
    return f"Hola {persona.nombre}! ¿Como estas?"

  def presentarse(self):
     return f"Me llamo {self.nombre} {self.apellido} y tengo {self.edad} años."


p1 = Persona("Germán", "Segovia", 29)
p2 = Persona("Juan", "Perez", 30)

print(p1.saludar(p2))
print(p1.presentarse())
print(p2.saludar(p1))
print(p2.presentarse())

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}"

    def saludar(self, persona = None):
        if persona is None:
            print(f"{self.nombre}: Hola!")
        else:
            print(f"{self.nombre}: Hola {persona.nombre}!")

    def presentarse(self):
        print(f"{self.nombre}: Mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años.")

persona1 = Persona("Juan", "Perez", 25)
persona2  = Persona("Maria", "Garcia", 30)

persona1.saludar()
persona1.presentarse()
persona2.saludar(persona1)
persona2.presentarse()

# Ejercicio 2
# Escribir una clase llamada Producto con los siguientes atributos:
# nombre, precio, descuento y stock.
# y contenga los siguientes metodos:
# __str__: para mostrar el nombre y precio del producto
# precio_descuento: para calcular el precio con descuento
# agregar_stoc: que recibe "cantidad" para agregar stock
# restar_stock(cantidad): que receibe "cantidad" para restar stock
# si no hay suficiente imprimir un error

class Producto():
  def __init__(self, nombre, precio, descuento, stock):
    self.nombre = nombre
    self.precio = precio
    self.descuento = descuento
    self.stock = stock

  def __str__(self):
    return f"Producto: {self.nombre}\nPrecio: ${self.precio}"

  def precioDescuento(self):
    return f"Descuento: {self.descuento}%\nPrecio con descuento: ${self.precio*(100-self.descuento)/100}"

  def agregarStock(self,cantidad):
    self.stock += cantidad
    return f"Stock disponible: {self.stock} unidades"

  def restarStock(self,cantidad):
    if self.stock < cantidad:
      return f"No hay disponible suficiente stock."
    else:
      self.stock -= cantidad
      return f"Stock disponible: {self.stock} unidades"

p1 = Producto("Arveja", 455, 10, 5)
print(p1)
print(p1.precioDescuento())
print(p1.agregarStock(10))
print(p1.restarStock(2))

# Ejercicio 3
# Escribir una clase llamada Autor, que contenga los atributos nombre y nacionalidad.
# Escribir una clase llamada Libro, que contenga los atributos autor, título, género y páginas.
# Crear por lo menos dos autores y dos instancias de libros asociadas a éstos.

class Autor():
  def __init__(self, nombre, nacionalidad):
    self.nombre = nombre
    self.nacionalidad = nacionalidad

  def __str__(self):
    return (f"Nombre: {self.nombre}\nNacionalidad: {self.nacionalidad}")


class Libro():
  def __init__(self, autor, titulo, genero, paginas):

    self.autor = autor
    self.titulo = titulo
    self.genero = genero
    self.paginas = paginas

  def __str__(self):
    return f"{self.autor}\nTítulo: {self.titulo}\nGénero: {self.genero}\nPáginas: {self.paginas}"


a1 = Autor("Germán", "Argentino")
a2 = Autor("Kim", "Japonesa")
l1 = Libro(a1,"Libro 1", "Drama", 305)
l2 = Libro(a2, "Libro 2", "Terror", 432)

print(l1)
print("------")
print(l2)

"""Escriba un programa de Python para crear una clase de persona. Incluye atributos como nombre,país y fecha de nacimiento. Implementa un método para determinar la edad de la persona.

"""

import datetime

class Persona():
  def __init__(self, nombre, pais, f_nacimiento):
    self.nombre = nombre
    self.pais = pais
    self.f_nacimiento = f_nacimiento

  def __str__(self):
    return f"Nombre: {self.nombre}\nPais: {self.pais}\nFecha de Nacimiento: {self.f_nacimiento}"

  def edad(self):
    fecha_actual = datetime.date.today()
    año = int((self.f_nacimiento.rsplit("/")[::-1])[0])
    mes = int((self.f_nacimiento.rsplit("/")[::-1])[1])
    dia = int((self.f_nacimiento.rsplit("/")[::-1])[2])
    f_nacimiento = datetime.date(año, mes, dia)

    resta_años = fecha_actual.year-f_nacimiento.year

    if fecha_actual.month > f_nacimiento.month:
      return resta_años
    elif fecha_actual.month == f_nacimiento.month:
      if fecha_actual.day >= f_nacimiento.day:
        return resta_años
      else:
        return resta_años-1
    else:
      return resta_años-1



p1 = Persona("Ger","Arg","21/11/1993")

print(p1)
print(f"La edad de {p1.nombre} es {p1.edad()} años")

"""Escriba un programa de Python para crear una clase de calculadora. Incluya métodos para
operaciones aritméticas básicas.
"""

class Calculadora():

  def __init__(self,n1,n2):
    self.n1 = n1
    self.n2 = n2

  def __str__(self):
    return f"Números ingresados: {self.n1} y {self.n2}"

  def suma(self):
    return self.n1 + self.n2

  def resta(self):
    return self.n1 - self.n2

  def multiplicacion(self):
    return self.n1 * self.n2

  def division(self):
    return self.n1/self.n2

c1 = Calculadora(5,2)
print(c1)
print(f"La suma es: {c1.suma()}")
print(f"La resta es: {c1.resta()}")
print(f"La multiplicación es: {c1.multiplicacion()}")
print(f"La división es: {c1.division()}")

"""Escriba un programa de Python para crear una clase que represente un carrito de compras.
Incluya métodos para agregar y eliminar artículos, y calcular el precio total.
"""

class CarroCompras():

  def __init__(self):
    self.carro = {}

  def agregar(self, nombre, precio, cantidad = 1):
    if nombre in self.carro:
      self.carro[nombre]['cantidad'] += cantidad
    else:
      self.carro[nombre] = {'precio': precio, 'cantidad': cantidad}
    print(f"Productos agregados: {nombre}, Precio: ${precio}, Cantidad: {cantidad} unidades, Total: ${precio*cantidad}")


  def eliminar(self, nombre, cantidad = 1):
    if nombre in self.carro:
      if self.carro[nombre]['cantidad'] >= cantidad :
        self.carro[nombre]['cantidad'] -= cantidad
        print(f"{cantidad} unidades de {nombre} eliminadas del carrito")
        if self.carro[nombre]['cantidad'] == 0:
          del self.carro[nombre]
          print(f"{nombre} eliminado del carrito.")
      else:
        del self.carro[nombre]
        print(f"{nombre} eliminado del carrito.")

  def total(self):
        total = 0
        for item in self.carro.values():
          total += item['precio'] * item['cantidad']
        return total

  def verCarrito(self):
    print(f"Carrito Actual: TOTAL CARRITO ${self.total()}\n")
    for nombre, info in self.carro.items():
      print(f"{nombre}: Precio: ${info['precio']}, Cantidad: {info['cantidad']} unidades, Total: ${info['precio']*info['cantidad']}")


carrito = CarroCompras()
carrito.agregar("Arveja",5,9)
carrito.agregar("Leche",2,3)
print("---------------------------------------")
carrito.eliminar("Arveja",4)
print("---------------------------------------")
carrito.verCarrito()

# Ejercicio 8
# 1. Crear una clase Sala con los atributos:
# nombre
# Una vez creada la sala se debe anunciar por consola
# que la sala se ha creado

# 2. Crear una clase Usuario con los atributos:
# nombre y apellido y sala
# Una vez creado el usuario se debe anunciar por consola
# que el usuario se ha unido al chat y con qué rol (nombre de la clase)

# 3. Crear una clase Oyente que herede de Usuario
# Con el método escuchar


# 4. Crear una clase Hablante que herede de Oyente
# Con el metodo hablar

class Sala():
  def __init__(self, nombre_sala):
    self.nombre_sala = nombre_sala
    print(f"La sala {self.nombre_sala} se ha creado.")

  def __str__(self):
    return self.nombre_sala


class Usuario():
  def __init__(self, nombre, apellido, sala):
    self.nombre = nombre
    self.apellido = apellido
    self.sala = sala
    print(f"El usuario {self.nombre} se ha unido al chat de la sala {self.sala} con el rol {self.__class__.__name__}")

  def __str__(self):
    return f"{self.nombre} {self.nombre_sala}{self.__class__.__name__}"

class Oyente(Usuario):
  def __init__(self, nombre_sala, nombre, apellido):
    super().__init__(nombre_sala, nombre, apellido)

  def escuchar(self):
    return f"El Usuario {self.nombre} está escuchando."

class Hablante(Usuario):
  def __init__(self, nombre_sala, nombre, apellido):
    super().__init__(nombre_sala, nombre, apellido)

  def hablar(self):
    return f"El Usuario {self.nombre} está hablando"



sala_1 = Sala("Informatorio")
sala_2 = Sala("General")
usuario_1 = Oyente("Ger", "Segovia",sala_1)
print(usuario_1.escuchar())
usuario_2 = Hablante("Juan", "Perez", sala_2)
print(usuario_2.hablar())

"""Crear una clase Estudiante con encapsulamiento y métodos para calcular el promedio de
calificaciones.

debe tener obtener promedio como metodo

agregar calificacion como metodo


obtener nombre como metodo
"""

class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__nota = []

    def agregar_nota(self, nota):
        self.__nota.append(nota)

    def obtener_promedio(self):
        if len(self.__nota) == 0:
            return "No hay calificaciones cargadas"
        else:
          total = sum(self.__nota)
          return round(total / len(self.__nota),1)

    def obtener_nombre(self):
        return self.__nombre

e1 = Estudiante("Ger")
e1.agregar_nota(9)
e1.agregar_nota(7)
e1.agregar_nota(6.6)
e2 = Estudiante("Pedro")

print(f"Nombre del estudiante: {e1.obtener_nombre()}")
print(f"Promedio de calificaciones: {e1.obtener_promedio()}")
print(f"Promedio de calificaciones: {e2.obtener_promedio()}")

"""Escribe un programa de Python que compruebe si una clase es una subclase de
otra.
"""

class Uno():
  pass

class Dos(Uno):
  pass

if issubclass(Dos, Uno):
  print("Dos es subclase de Uno")
else:
  print("Dos no es subclase de Uno")

