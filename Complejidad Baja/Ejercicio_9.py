"""
La veterinaria Dogs inc, necesita que usted cree un programa que le permita ingresar
informacion de los perros que llegas al local:
-Nombre del perro
-Raza
-Edad
cada perro sera guardado en una lista. Finalmente usted debera mostrar toda la lista,
para conocer los datos de los perros ingresados

REQUISITOS:
-Debe permitir pedir por separo el nombre, raza y edad del perro.
-debe poder ingresar varios perros. No hay un limite fijo en el numero de animales, 
 este valor lo definira el usuario
-debe hacer uso de clases, cree una clase perro
-debe usar listas
"""
#Creamos la clase:
class Perro:
    nombre = ""
    raza = ""
    edad = 0
    def __init__(self, nombre, raza, edad) :
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    def imprimir(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)
        print("Edad ", self.edad)

def agregarPerro(luesta, objPerro):
    lista.append(objPerro)

def crearPerro():
    nombre = input("ingrese nombre del perro")
    raza = input("ingrese raza del perro")
    edad = input("ingrese edad del perro")
    return Perro(nombre, raza, edad)

listaPerros[]

cantPerros = input("ingrese numero de perros")

for i in range(0, cantPerros):
    agregarPerro(lista,crearPerro())

for perro in listaPerro:
    perro.mostrarInformacion()


