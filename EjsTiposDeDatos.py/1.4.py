#Escribir un programa que pregunte el nombre del usuario 
# en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario 
# tantas veces como el número introducido.

nombre = input("¿Cúal es tu nombre?: ")
número = input("Introduce un número: ")
print((nombre + "\n") *int(número))