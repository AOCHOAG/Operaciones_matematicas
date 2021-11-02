n = int(input("Introduce el tamaño de la matriz cuadrada: "))

matriz1 = []
print("Introduce los elementos de la matriz 1: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Fila: ", i, "Columna: ", j)
        numero = int(input("Introduce un número: "))
        fila.append(numero)
    matriz1.append(fila)
print("Esta es la matriz 1: ", matriz1)

matriz2 = []
print("Introduce los elementos de la matriz 2: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Fila: ", i, "Columna: ", j)
        numero = int(input("Introduce un número: "))
        fila.append(numero)
    matriz2.append(fila)
print("Esta es la matriz 2: ", matriz2)

matriz_suma = []
for i in range(n):
    fila = []
    for j in range(n):
        suma = matriz1[i][j] + matriz2[i][j]
        fila.append(suma)
    matriz_suma.append(fila)


print("Este es el resultado de sumar ambas matrices: ", matriz_suma)




