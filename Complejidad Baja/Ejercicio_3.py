"""
Cree un programa que utilizando funciones y listas le permita generar la siguiente tabal de 
multiplicar. Haga uso de ciclos si asi lo requiere. No es valido colocar la representacion
fija de la tabla
"""

def tablaM(numero):
    lista = []
    for i in range(1,8,1):
        lista.append(str(numero*i))
    print(", ".join(lista))
    
for i in range(1,11,1):
    tablaM(i)

#Se a modificado la lista para convertir cada elemento en una cadena de texto usando la función str().

#Luego se a usado la función join() para unir los elementos de la lista separados por comas en una sola 
# cadena. La cadena resultante se imprime usando la función print(). De esta manera, los elementos de la 
# lista se imprimen sin los corchetes "[" y "]" que rodean a la lista completa.