#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

A = float(input("Introduce el dividendo: "))
B = float(input("Introduce el divisor: "))

if B == 0:
    print("Error")
else: 
    print(A/B)

#POR QUE SE PUEDE HACER CON INT Y ALF LO HACE CON FLOAT??
#HAY QUE PONER FLOAT PORQUE SI INTRODUCES UN 3.14 TE MANDA ERROR PORQUE NO ES UN NUMERO SIN DECIMALES.