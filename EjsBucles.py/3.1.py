#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

#palabra = input("Inserte una palabra: ")
#print((palabra + "\n")*10)
#IMPORTANTE PONER EL *10 DENTRO DEL PARÉNTESIS PQ SINO TE DA ERROR

#PARA HACERLO CON BUCLES SERÍA:

word = input("Inserte palabra: ")
for i in range(1, 10):  #AQUÍ SE PUEDE PONER O RANGE(10)
    print(word)         # O TAMBIÉN RANGE(1, 10)DEL 1 AL 10
