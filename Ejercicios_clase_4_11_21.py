# """Pickle example"""
# import pickle
#
# sens_1 = ["pos_1", "photo_1", "io_1"]
# sens_2 = ["pos_2", "photo_2"]
# cells = [
#         {"robot": "IRB", "sensor": sens_1}
#         {"robot": "UR3", "sensor": sens_2}
#         ]
#     for cell in cells
#         print("\nCell; ","Robot: ", cell["robot"])
#         for sensor in cell ["sensor"]
#             print("  ", "sensor: ", sensor)
#
# pickle.dump(cells, open("cells.data", "wb"))
# cells = []
# print("\ncells:\n", cells)
# cells = pickle.load(open("cells.data", "rb"))
# print("\ncells:\n", cells)

lista_coches = [] #Creamos una lista vacía
while True: #creamos un bucle, para introducir varios elementos
    marca_coche = input("Introduce la marca del coche: ") #Creo variable marca coche y le pido que intruduzca
    if marca_coche == "fin": #le digo que si se escribe "fin" finalice el bucle (con break)
        break
    modelo_coche = input("Introduce el modelo del coche: ")
    combustible = input("introduce el tipo de combiustible: ")
    cilindrada = input("Introduce la cilindrada: ")


    datos_coche = {} #Creo un diccionario vacio
    datos_coche ["Marca del coche: "] = marca_coche #añado "palabras" al diccionario
    datos_coche ["Modelo del coche: "] = modelo_coche
    datos_coche ["Tipo de combustible: "] = combustible
    datos_coche ["Cilindrada: "] = cilindrada
    lista_coches.append(datos_coche) #Con el .append, le digo que a la lista_coches
    #le añada el diccionario en el que he ordenado las respuestas dadas, con la pregunta que he ehcho
    #datos_coche ["Cilindrada: "] = cilindrada. Es una manera de tener ordenadas las respuestas.

for datos_coche in lista_coches: #por cada nuevo diccionario en la lista de coches le pido que lo ponga por
                                 #Separado. De esta manera lo añade a otr
    print("Caracteristicas del coche: \n", datos_coche) #Le pido que imprima Lista... lista_coches

#Abrir archivo en modo escritura "w"
archivo_coches = open("coches.txt", "w") #Si es una a, hace de append, añade a la lista.
for coche in lista_coches:
    archivo_coches.write(coche["Marca del coche: "] + "," + coche["Modelo del coche: "] + "," +\
              coche["Tipo de combustible: "] + "," + coche["Cilindrada: "] + "\n")

archivo_coches.close()
coches = []
c = open("coches.txt","r")
for linea in c:
    coche = {}
    coche["Marca del coche: "], coche["Modelo del coche: "], coche["Tipo de combustible: "], \
    coche["Cilindrada"] = linea.split(',')
    coches.append(coche)
for coche in coches:
    print("Coche: ", coche)
