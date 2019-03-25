#Escribir un programa que pregunte el nombre del usuario 
# en la consola y después de que el usuario lo introduzca 
# muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas 
# y <n> es el número de letras que tienen el nombre.

nombre = input("¿Cúal es tu nombre?: ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

#Tenemos que poner el str antes del len porque tiene que convertir el número a cadenapara que se pueda sumar con lo demas que es cadena tambien.