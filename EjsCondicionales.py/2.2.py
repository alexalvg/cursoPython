#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

#Se pone el x.lower() donde el if, para que lo que introduzca el usuario se cambie directaente a minusc.
x = input("Introduce la Constraseña: ")

if x.lower() == "contraseña":
    print("true")
else:
    print("Fuera de mi computer")