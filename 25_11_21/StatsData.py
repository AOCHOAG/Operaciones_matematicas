"""Defino la clase Data, para representar datos estadisticos"""
import statistics
class StatsData:
    def __init__(self, lista):
        self.l_data = lista
        self.mean = statistics.mean(self.l_data) #Poner stat.mean(lista) es lo mismo
        self.median = statistics.median(self.l_data)
        self.varance = statistics.variance(lista)

