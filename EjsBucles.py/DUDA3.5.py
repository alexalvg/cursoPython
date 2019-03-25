#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

Q = float(input("¿Cuánto dinero desea invertir?: "))
t = float(input("Interés anual?: "))
y = int(input("¿Durante cuántos años?: "))

for i in range(1, y+1):
    print("El capital obtenido tras "+ str(y) + " años de inversión será de " + str((Q + (t/100)**y))
print("hasta luego")