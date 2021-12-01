import stats_data as sd

# res = sd.StatsData([1,2,8.5,3.1])
# print("Lista de numeros: ", res.l_data)
# print("Media: ", res.mean)
# print("Mediana: ", res.median)
# print("Varianza: ", res.varance)

lista = []
while True:
    numeros = input("Introduce numeros: ")
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista.append(numeros)
calculo_stats = sd.StatsData(lista) #Creo una variable de tipo objeto calculo_stats
                                    #El objeto  creado de tipo sd.StatsData se almacena
                                    #en la variable calculo_stats

print("Lista de numeros: ", calculo_stats.l_data) #Se trata de una lista dentro de un objeto
                                                  #l_data es un
print("Media: ", calculo_stats.mean)
print("Mediana: ", calculo_stats.median)
print("Varianza: ", calculo_stats.varance)


