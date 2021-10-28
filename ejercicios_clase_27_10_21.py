#Ejercicio 6
#Pedir una palabra que se introduzca en el teclado. Contar cuantas veces aparece cada vocal.
#Usar una estructura de datos tipo dict con una key para cada vocal que va a contener el
# numero de veces que aparece esa vocal en la palabra


vocales = ["a","e","i","o","u" ] #defino las vocales

palabra = input("Introduce la palabra: ")  # pido que se introduzca una palabra

frecuencia_vocales = {"a":0, "e":0, "i":0, "o":0, "u":0 } #Reseteo a 0 la frecuencia aparece cada vocal
#Se pone entre llaves {} los DICCIONARIOS. Cada elemento está entre comillas "a" y le doy el valor de 0 (:0)

for letra in palabra: #Defino letra en el momento, y le digo que cuando se encuentre dentro de palabra haga...

    if letra in vocales: #Le digo que si "letra" se encuentra detro de las vocales entonces

        frecuencia_vocales[letra] += 1 #Por cada vocal le asigno un valor de +1

print("La frecuencia de las vocales en" ,palabra, "es:\n"  ,frecuencia_vocales,)
#primera manera de hacerlo, sin emplear {}

print(f"La frecuencia de las vocales en{palabra} es:\n {frecuencia_vocales}")
#segunda manera de hacerlo, empleando{} dentro de las ""
#pongo "f" delante para que me muestre lo que esta dentro de las {} dentro de ""
#le pido que imprima el texto "la frecuencia..."
#pongo palabra entre llaves, para que imprima la palabra que he utilizado dentro de las comillas
#para que lo incluya junto al texto
#\n se utiliza para saltar una linea y poner {frecuencia_vocales} en otra linea, se llama guía de estilo




