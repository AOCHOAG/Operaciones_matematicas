import statistics

Lista_numeros = []
while True:
    numeros = float(input("Introduce un nuevo numero para calcular datos: "))
    if numeros == -999:
        break
    Lista_numeros.append(numeros)

media = statistics.mean(Lista_numeros)
mediana = statistics.median(Lista_numeros)
varianza = statistics.variance(Lista_numeros)

print("La media es: ", media)
print("La mediana es: ",mediana)
print("La varianza es: ", varianza)