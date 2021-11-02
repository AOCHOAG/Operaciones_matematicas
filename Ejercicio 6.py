
numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce otro número: "))
numero3 = float(input("Introduce un último número: "))

lista_numeros = [numero1, numero2, numero3]

def mean(data):
    return sum(data) / len(data)

Media = mean(lista_numeros)
print("La media es: ", Media )

def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2

Mediana = median(lista_numeros)
print("La mediana es: ", Mediana)

def variance(data, xbar=None):

    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 2:
        raise StatisticsError('variance requires at least two data points')
    T, ss = _ss(data, xbar)
    return _convert(ss / (n - 1), T)
Varianza = variance(lista_numeros)
print("La varianza es: ", Varianza)
