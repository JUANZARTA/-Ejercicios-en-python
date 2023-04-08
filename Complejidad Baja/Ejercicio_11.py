"""
Programa que solicita al usuario que ingrese por teclado 5 números enteros
positivos y distintos de cero y los almacena en una lista. Si se ingresa un valor
que no cumpla con la condición se debe volver a pedir el número.

a. Imprima la lista
b. Calcule e imprima el resultado de la suma de los elementos que ocupan
   posiciones impares.
c. Calcule e imprima el número mayor de la lista e indique el número de veces
   que aparece ese número en la lista.
"""

lista = []
print("porfavor ingrese 5 numeros mayores a 0: ")
while num != 0 :
    if num < 0:
        print("El numero debe ser un entero positivo, intente nuevamente: ")
    elif len(lista) < 4:
        num = int(input("porfavor ingrese el siguiente numero: "))
        lista.insert(len(lista), num)

if num == 0:    
    print("la lista",lista)
    len(lista)

