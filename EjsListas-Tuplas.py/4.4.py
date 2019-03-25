#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

a=[]
for i in range(1, 5):
    loteria = int(input("¿Cuáles son los números ganadores de la lotería: "))
    a.append(loteria)
    a.sort()
print(a)

#HAY QUE ABRIR LA LISTA ANTES DE INICIAR EL BUCLE PORQUE SINO NO HAY SITIO AL QUE AÑADIRLO DURANTE EL BUCLE
#MEJOR EL APPEND PORQUE EL EXTEND ES OCMO SI FUSONARA UA CADENA CON OTRA Y APPEND TE VA AÑADIENDO UNO A UNO.
