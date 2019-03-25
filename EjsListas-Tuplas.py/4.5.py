#Escribir un programa que almacene en una lista los números 
# del 1 al 10 y los muestre por pantalla 
# en orden inverso separados por comas.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
print(numeros)
#EN PRINCIPIO HASTA AQUÍ ESTARÍA BIEN, SIN EMBARGO, PODEMOS HACERLO MEJOR
# Y HACER QUE NO SALGAN LOS CORCHETES IMPRIMMIENDO CADA ELEMENTO DE LA LSTA
#INDIVIDUALMENTE Y SEPARADOS POR UN ESPACIO.
for i in numeros:
    print(i, end = " ")