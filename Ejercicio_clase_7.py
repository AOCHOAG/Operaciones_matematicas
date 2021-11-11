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



#Quiero guardar los datos que he recopilado en la lista en un archivo
archivo_coches = open("coches.txt", "w") #Abrir archivo en modo escritura "w"
                                         #Si es una a, hace de append, añade a la lista.
for coche in lista_coches:#Creo la variable coche, para cada diccionario en lista_coches
    #archivo_coches.write(str(datos_coche))
    archivo_coches.write(coche["Marca del coche"] + "," + coche["Modelo del coche"] + "," +\
                         coche["Tipo de combustible"] + "," + coche["Cilindrada"] + "\n")
                         #Escribo en archivo_coches cada diccionario de la lista, los llamo escribiendo
                         #Cada campo del diccionario individualmente, separado por comas.

archivo_coches.close()#Cierro el archivo

#Quiero leer la información del archivo y almacenarla en la variable [vacia] lista_coches
lista_coches = [] #Vacio la lista de coches

c = open("coches.txt","r") #Le digo que abra el archivo en modo lectura "r"

for linea in c: #Al ser un archivo, le pido que ejecute el bucle una vez por cada linea{diccionario} del archivo
    coche = {} #Creo un diccionario vacio
    #Tengo un string (texto), quiero asignar cada dato del string
    #separado con "," al campo correspondiente del diccionario

    # Va llenando la lista y le pido que asigne
    # cada valor separado por "," a Marca del coche
    # Modelo del cocche, Combustible, cilindrada
    # Uno detras de cada uno
    coche["Marca del coche"], coche["Modelo del coche"], \
    coche["Tipo de combustible"], coche["Cilindrada"] = linea.split(',') #Linea.split(",") se encarga de
                                                                         #cada vez qye hay una "," separarlo
                                                                         #en un campo independiende

    lista_coches.append(coche)#Añado cada coche a la lista de coches
for coche in lista_coches: #Por cada diccionario en la lista, lo imprimo por pantalla
    print("Coche: ", coche)



