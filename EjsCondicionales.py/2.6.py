renta = int(input("¿Cuál es su renta aproximada?: "))

if renta <10000:
    print("5%")
elif 10000 < renta <20000:
    print("15%")
elif 20000 < renta < 35000:
    print("20%")
elif 35000 < renta < 60000:
    print("30%")
else:
    print("45%")

#PORQUE CUANDO SE PONE EL 5 HAY QUE PONERLO TB ENTRE COMILLADO??


