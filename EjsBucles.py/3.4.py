#   Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
#la cuenta atrás desde ese número hasta cero separados por comas.

number = input("Introduzca un número (positivo): ")
contador = int(number)
while contador != 0:
    print(contador)
    contador -=1
print("Cuenta atrás")