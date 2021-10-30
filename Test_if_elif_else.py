"""ejemplo bucles"""
data = list()
while True:
    entrada = float(input("siguiente dato (-999 para terminar)?"))
    if entrada != -999.0:
        data.append (entrada)
    else:
        break
print("Los numeros de la lista son: ", " ", data)
#for numero in data:
 #   print("Números: ", numero)
