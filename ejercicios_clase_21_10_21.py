#matrix = [
   # [1, 2, 3, 4],
    #[10, 11, 12, 13, 14],
    #[20,21,22,23,24],
    #[30,31,32,33,34]
    #]

#print("Matrix: \n", matrix)

n = int(input("Dimensión matrices a sumar: "))
m1 = []
print("Elementos de la matriz 1: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Elemento", i,",", j,)
        elem = float(input("Elem: "))
        fila.append(elem)
    m1.append(fila)
print("Matriz 1 leida: \n", m1)

m2 = []
print("Elementos de la matriz 2: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Elemento", i,",", j,)
        elem = float(input("Elem: "))
        fila.append(elem)
    m2.append(fila)
print("Matriz 2 leida: \n", m2)

m_suma = []
for i in range(n):
    fila = []
    for j in range(n):
        elem = m1[i][j] + m2[i][j]
        fila.append(elem)
    m_suma.append(fila)
print("Matrix suma: \n", m_suma)
