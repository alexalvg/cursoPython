Q = float(input("¿Cuánto dinero desea invertir?: "))
t = float(input("Interés anual?: "))
y = int(input("¿Durante cuántos años?: "))

for i in range(1, y+1):
    print("El capital obtenido tras "+ str(y) + " años de inversión será de " + str((Q + (t/100 + 1)**y))
