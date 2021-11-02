"""Ejercicio 6 versión 2.0 AOG"""
import statistics

numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce otro número: "))
numero3 = float(input("Introduce un último número: "))

numeros = [numero1, numero2, numero3]

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
varianza = statistics.variance(numeros)

print("La media de los números es: ", media)
print("La mediana de los números es: ", mediana)
print("La varianza de los numros es: ", varianza)
