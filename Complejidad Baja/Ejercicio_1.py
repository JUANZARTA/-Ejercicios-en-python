"""Teniendo encuenta la cadena denominada: iniciales = JKLMNPQ,  REALICE UN PROGRAMA 
   QUE IMPRIMA LOS SIGUIENTE NOMBRES:
   jack
   kack
   lack
   mack
   nack
   pack
   qack
   """

letras = "JKLMNPQ" #inicializo las letras

for i in letras: #creo un recorrido 
   nombre = i + "ack" #creo una variable nueva y le asigno la posicion del recorrido mas "ack"
   print(nombre) #imprimo los nombre
   #print(nombre.lower())      #lower() me permite cambiar de mayuscula a minuscula