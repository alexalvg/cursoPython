#Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad).

edad = int(input("¿Cuántos años tienes?: "))

n = 1
while n <= edad:
    print(n)
    n = n + 1
print("Hasta ahora que tienes " + str(n) + " años")