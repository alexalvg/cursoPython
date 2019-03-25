#Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que contiene 
# cada vocal.


word = list(input("Escribe una palabra: "))
vocales = ["a", "e", "i", "o", "u"]

for i in word:
    if i == vocales:
        word.pop(i)
    

print(word)
