import pickle

lista_coches = [] #Creamos una lista vacía
while True: #creamos un bucle, para introducir varios elementos
    marca_coche = input("Introduce la marca del coche: ") #Creo variable marca coche y le pido que intruduzca
    if marca_coche == "fin": #le digo que si se escribe "fin" finalice el bucle (con break)
        break
    modelo_coche = input("Introduce el modelo del coche: ")
    combustible = input("introduce el tipo de combiustible: ")
    cilindrada = input("Introduce la cilindrada: ")


    datos_coche = {} #Creo un diccionario vacio
    datos_coche ["Marca del coche"] = marca_coche #añado "palabras" al diccionario
    datos_coche ["Modelo del coche"] = modelo_coche
    datos_coche ["Tipo de combustible"] = combustible
    datos_coche ["Cilindrada"] = cilindrada
    lista_coches.append(datos_coche) #Con el .append, le digo que a la lista_coches
    #le añada el diccionario en el que he ordenado las respuestas dadas, con la pregunta que he ehcho
    #datos_coche ["Cilindrada: "] = cilindrada. Es una manera de tener ordenadas las respuestas.

for datos_coche in lista_coches: #por cada nuevo diccionario en la lista de coches le pido que lo ponga por
                                 #Separado. De esta manera lo añade a otr
    print("Caracteristicas del coche: \n", datos_coche) #Le pido que imprima Lista... lista_coches


pickle.dump(pickle.dumps(lista_coches), open("coche.txt", "wb"))
lista_coches = []
print("Lista de coches: ", lista_coches)
lista_coches = pickle.loads(pickle.load(open("coche.txt", "rb")))
print("Lista de coches: ", lista_coches)