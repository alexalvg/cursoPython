inversion = int(input("¿Cúanto dinero quieres invertir?: "))
interes = float(input("¿Qué tipo de interés?: "))
años = int(input("¿Durante cúantos años?: "))

print( inversion*( 1 + interes)**años)

#hay que poner el int donde inversion y años para que pase la cadena a numero, y en tipo de inversion el float para que pase el dec a numero.
#tambien podriamos haber expresado el porcentaje partienddo el interes entre 100 
