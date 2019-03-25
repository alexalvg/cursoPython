asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []


for i in asignaturas:
    c = float(input("¿Qué nota has sacado en " + i + "?: "))
    if c >=5:
        aprobadas.append(i)
print(aprobadas)
for passed in aprobadas:
    aprobadas.remove(passed)
print(aprobadas)