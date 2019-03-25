#Escribir un programa que pida al usuario un número entero 
#y muestre por pantalla si es un número primo o no.

#numero = int(input("Introduce un número: "))
#while numero//numero != 1:
#    input("vuelve a introducir un númoer, ese no es primo")
#print("Es primo")

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")