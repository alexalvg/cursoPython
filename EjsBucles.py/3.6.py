#Escribir un programa que pida al usuario un número entero 
#y muestre por pantalla un 
#triángulo rectángulo como el de más abajo, 
#de altura el número introducido.

triangulo = int(input("¿Qué altura quieres que tenga el triángulo?: "))

for i in range (1, triangulo + 1):
    print("*"*i)