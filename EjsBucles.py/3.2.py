#Escribir un programa que pregunte al usuario su edad y muestre 
#por pantalla todos los años que ha cumplido 
#(desde 1 hasta su edad).

edad = input("¿Cuántos años tienes?: ")
for i in range(1, int(edad)+1):
    print(i)

#AQUÍ HACE FALTA PONER EL +1 EN RANGE AUNQUE TAMBIÉN SE PUEDE
#PONER DENTRO DEL () DE PRINT AÑADIENDOLE 1.
#   ALF PONE: PRINT("HAS CUMPLIDO" + STR(I + 1) + " AÑOS")