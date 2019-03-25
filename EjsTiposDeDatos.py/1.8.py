#Escribir un programa que pida al usuario dos números 
# enteros y muestre por pantalla la <n> entre <m> 
# da un cociente <c> y un resto <r> donde <n> y <m> 
# son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la 
# división entera respectivamente.

A = input("Introduce un número: ")
a = input("Introduce un segundo número: ")
c = (int(A)/int(a))
r = (int(A)%int(a))

print(str(A) + "\n" + str(a) + "\n")