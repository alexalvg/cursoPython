altura = input("¿Cúanto mides?: ")

#El índice de masa corporla se calcula dividiendo los kg de peso por el cuadrado de la estatura en m

imc = (int(peso)/(float(altura)**2))
#hay que pasar el "70" de cadena(str) a número con int
#también hay que pasar el numero "1.90" a numero pero como es un decimal usamos float

#print("Tu índice de masa corporal es " + str(imc))

print("Tu índice de masa corporal es " + str(round(imc, 2)))
#round lo que hace es como redondear, y es round( valor, numero de decimales que quieres)
