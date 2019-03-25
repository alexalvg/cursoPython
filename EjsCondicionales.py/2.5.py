nombre = input("¿Cuál es tu nombre?: ")
sexo = input("¿Es usted hombre o mujer: ")

if(nombre[0] <= "m" and sexo == "mujer") or (nombre[0] >= "n" and sexo== "hombre"):
    print("grupo A")
else: 
    print ("grupo B")

#para coger solo la primera letra poner los corchetes y el 0 pq empieza a contar desde ahi los caracteres.
#al poner pint siempre poner las mayusculas