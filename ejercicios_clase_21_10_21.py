#matrix = [
   # [1, 2, 3, 4],
    #[10, 11, 12, 13, 14],
    #[20,21,22,23,24],
    #[30,31,32,33,34]
    #]

#print("Matrix: \n", matrix)

n = int(input("Dimensión matrices a sumar: ")) #Defino n como las filas x columnas de mis matrices

m1 = [] #Defino m1 como una matriz en blanco

print("Introduce los elementos de la matriz1: ") #Le pido que imprima los elementos de la matriz 1

for i in range(n): #Desde i = 0 hasta el rango que he introducido anteriormente.

    fila = [] #Creo la variable fila, una matriz en horizontal [] vacia

    for j in range(n): #Dentro del bucle for i... creo un nuevo bucle que me hace las columnas ej:(2x * 2y)

        print("Elemento", i,",", j,) #Le pido que me muestre que casilla de la matriz estoy rellenando
                                     #Empezando por la [0,0] Fila 0, Columna 0

        elem = float(input("Elem: ")) #Defino elemento, le pido que introduzca un numero
                                      #(float = con decimal)  en la pantalla Elem:

        fila.append(elem) #Elem lo introduzco (append) en la fila, en la posicion que me marca i,j

    m1.append(fila) #Le pido que añada fila (con append) a m1

print("Matriz 1 leida: \n", m1) #Le pido que ponga matriz leida, y imprima m1 (matriz1)


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

m_suma = [] #Defino m_suma [matriz vacía]
for i in range(n):
    fila = []           #Empleo el mismo bucle de antes, pero ahora en vez de pedir que cree una matriz
                        #Le pido que sume una matriz con la otro, pasando uno por uno por todas las casillas
                        #de la matriz
    for j in range(n):
        elem = m1[i][j] + m2[i][j] #elem = m1(0,0) + m2(0,0)

        fila.append(elem) #Asigno la posición en la matriz en la que introduzco cada elem, la cual está
                          #Designada por el propio bucle
                          #Añado el resultado de la suma de las dos matrices (elem) a su posición en
                          #la matriz resultado

    m_suma.append(fila) #A la matriz suma, le añado la fila que acabo de rellenar de elem
print("Matrix suma: \n", m_suma)
