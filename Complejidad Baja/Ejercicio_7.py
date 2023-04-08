""" 2) solicite 3 numeros enteros e indicar cual es el 
    numero central basad en la recta numerica """
aux = 0
num1 = int(input("ingrese el primer numero :"))
num2 = int(input("ingrese el segundo numero :"))
while num1 == num2:
    num2 = int(input("Error, intente nuevamente :"))
    num3 = int(input("ingrese el tercer numero :"))
while (num3 == num1) or (num2 == num3):
    num3 = int(input("Error, intente nuevamente :"))
#para num1 como numero del medio  
if (num1<num2 and num1>num3) or (num1>num2 and num1<num3) :
    aux=num1
#para num2 como numero del medio  
elif (num2<num1 and num2>num3) or (num2>num1 and num2<num3):
    aux=num2 
#para num3 como numero del medio
elif (num3<num1 and num3>num2) or (num3>num1 and num3<num2):
    aux=num3
"""else:
    aux=num3"""

print("el numero dle medio es: ", aux)

    


