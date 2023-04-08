"""
1) cree e imprima un diccionario d en Python dond elos valores asociados a la clave son los nombres de
las peliculas y los directores son las claves

2) imprima solamente el nombre de los directores

3) adicione al diccionario la pelicula Toy Story con director Lee Unkrich e imprima nuevamente el diccionario

4) Elimine del diccionario toda informacion de la pelicula y su director cuando un usuario digite por 
   teclado el nombre especifico de un director

5) cambie el nombre de la pelicula de toy story por toy story 3 e imprima nuevamente el diccionario

6) compruebe si esta o no esta en el diccionario en el director Joaquin Acosta, para ellos muestre los 
   mensajes de la siguiente manera: El director si se encuentra o el director no se encuentra
   
Harry Potter --> David Yates
Avengers EndGame --> Anthony Russo
The Batman --> Matt Reeves
Joker --> Todd Phillips
"""
#1 Crear diccionario
diccionario = {
    "David Yates":"Harry Potter",  
    "Anthony Russo" : "Avengers EndGame",
    "Matt Reeves":"The Batman",
    "Todd Phillips":"Joker" ,"Joaquin Acosta": "Ligaw Liham"
}
#imprimir diccionario
print("1) Diccionario Completo ")
for clave, valor in diccionario.items():
   print(valor,",",clave)
print(" \n")
   
#2 Imprimir unicamente productores
print("2) Productores ")
for clave in diccionario:
   print(clave)
print(" \n")

#3 Agregar Nuevo director y pelicula
print("3) Diccionario (Agregando Nuevo director y pelicula)")
diccionario ["Lee Unkrich"] = "Toy Story"
# Imprimir diccionario
for clave, valor in diccionario.items():
   print(valor,",",clave)
print("\n")

#4 EL Usuario elimina Autor y Pelicula digitando el nombre especifico del productor
eliminarD = (input("4) ingrese el el nombre especifico del director a eliminar: "))
del(diccionario[eliminarD])

#5 Actualizar  la pelicula de Toy Story por Toy Story 3
print("5) Diccionario Actualizado")
diccionario["Lee Unkrich"] = "Toy Story 3"
for clave, valor in diccionario.items():
   print(valor,",",clave)
print("\n")

#6 Comprobando si Joaquin Acosta esta en el diccionario 
comp = "Joaquin Acosta"
print("El director de la pelicula: ", diccionario.get(comp, "No se encuentra"), "Si se encuentra")