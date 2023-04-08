""""
Programa que solicita una serie de numero esntresos positivos digitados por el usuario
y se almacena en una lista hasta que se digite el numero de salida cero 0, este numero no se 
-Almacena en una lista
-Imprima la lista digitada
-Atraves de una unica funcion calcula la media aritmetica de la lista y la cantidad de numeros 
 que son multiplos de 3
-Nota: si el usuario digita un numero negativo debe pedirsele que vuelva a escribir un numero 
 y recuerde que el cero es el numero de salida o el que deja de pedir mas numeros al usuario
"""

lista, n = [], 0    # creo la lista y una variable de entrada

def uFuncion(lista):    #creo la funcion que me solicitan
    aux, aux2 = 0,0     #inicializo variables auxiliares
    for i in lista:
        aux = aux+i     #inicializo una variable que me ira sumando los valores de la lista
    media = aux/len(lista)    #inicializo una variable que me dividira la suma entre la longitud de la lista -->len()
    print("La media Aritmetica es: ",media)

    for i in lista:
        if i%3 == 0:    # Condicion para saber si un numero es divicible por 3
            aux2= aux2 +1   # cuenta cuantos numeros son divicibles por 3
    print("Cantidad de Numeros divisbles entre 3: ", aux2)

    return aux2, media

n = int(input("digite un numero a ingresar: "))

while n != 0:
    if n < 0:
        n = int(input("Solo puedes ingresar numero positivos: "))
    else:        
        lista.insert(len(lista),n) #
        n = int(input("ingresa otro numero: "))
if n == 0:    
    print(lista)    #imprimir lista
    uFuncion(lista) #imprimir funcion

    