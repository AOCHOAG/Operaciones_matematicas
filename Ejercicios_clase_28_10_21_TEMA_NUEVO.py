"""ficheros"""
f_o = open("archivo.data","w") #con esta función creo un archivo que llamo "archivo.data"
#pongo , "w" para indicar que voy a escribir sobre ese archivo que he creado.

f_o.write("Texto para guardar 1\n") #con la funcion.write, le pido que escriba lo que pongo a continuacion
#pongo \n para hacer un salto de linea.
f_o.write("Texto para guardar 2")

f_o.close() #con este comando.close le indico que hasta aquí va a ocupar nuestro archivo

f_o = open("archivo.data","r") #le indoco que quiero abrir el archivo
# con "r" para modo de lectura unicamente

contenido = f_o.read() #creo una variable contenido en la que le indico que quieeo que lea f_o (mi texto)

print("Contenido archivo: \n",contenido) #le digo que imprima el texto y en la linea siguiente (\n)
#y despues le digo que muestre lo que he llamado contenido anteriormente
f_o.close() #Cierra el archivo