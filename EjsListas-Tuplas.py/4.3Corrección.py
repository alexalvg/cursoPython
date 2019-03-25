#   Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura, y después las muestre por pantalla 
# con el mensaje En <asignatura> has sacado <nota> 
# donde <asignatura> es cada una des las asignaturas
# de la lista y <nota> cada una de las correspondientes 
# notas introducidas por el usuario.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for a in asignaturas:
    c = input("¿Qué has sacado en " + a + "? ")
    notas.append(c)
for i in range(len(asignaturas)): #i te calcula la length, 3 y entonces range pasa a ser 3
    print("En " + asignaturas[i] + " has sacado " + notas[i])

#for a in asignaturas quiere decir que a va tomando los "valores"
#entonces te va preguntando que has sacado en a1, a2, a3...
#esos valores que tú das los guarda en notas con el notas.append
#para i en longitud de la cadena asignaturas, imprime en 
#el la asignatura que ocupa el valor i junto con has sacado y la nota que ocupe el valor i
#todo junto. MAS O MENOS :)