#   Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
#todos los números impares desde 1 hasta ese número separados por comas.

number = input("Introduce un número positivo: ")
for i in range(1, int(number), 2):
    print(i)

#EXISTE ALGUNA MANERA DE TRANSFORMAR UN NÚMERO NEGATIVO A POSITIVO??
