#Escribir un programa que pida al usuario una palabra
# y muestre por pantalla si es un palíndromo.

word = list(input("Introduce una palabra: "))
#LIST te hace una lista separandote cada uno de las letras
#ejemplo: word = list(input(introduce la palabra...))
#print(word) --> ["h", "o", "l", "a"]
print(word)
word_al_reves = word 
word_al_reves.reverse()
reves = word_al_reves
print(reves)
if word == reves:
    print("Es un palíndromo")
else:
    print("no es un palíndromo")