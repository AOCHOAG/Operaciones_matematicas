import datos_web as dw

pais = input("Introduce el pais del que quieres consultar la hora: ")
ciudad = input("Introduce la ciudad de la que quieres consultar la hora: ")

url = "https://www.timeanddate.com/worldclock/" + pais + "/" + ciudad
parser = '//span[@class = \'h1\']/text()'

web = dw.GetWebData(url)
print("La hora de",ciudad,"en",pais, "es: ",web.get_data(parser))