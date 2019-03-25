#Escribir un programa que almacene los vectores 
# (1,2,3) y (-1,0,2) en dos listas y muestre por 
# pantalla su producto escalar.

a = (1,2,3,)
b = (-1,0,2)
producto = 0
for i in range(len(a)):
    producto += a[i]*b[i]
#IMPORTANTÍSIMO, CUANDO QUIERES SELECCIONAR UN CARACTER CONCRETO
#DE LA CADENA, PONES EL VETOR Y ENTRE [] PONES LA i,
#DESPUES CLARO DE HABER PUESTO UN BUCLE FOR.
print("El producto escalar de los vectores a y b da como resultado " + str(producto))