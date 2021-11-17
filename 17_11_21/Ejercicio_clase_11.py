"""Ejercicio Clase 11 (main)"""
import Persistencia_pickle as pp
import car_class
import random as rd
file = "coches_obj.txt"
lista_coches = pp.retrieve(file)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    coche = car_class.Car(marca, modelo, combustible, cilindrada)
    lista_coches.append(coche)
    coche.move_to(rd.random()*100, rd.random()*600)
    print("Posición: ", coche.get_pos())
    coche.move_incr(rd.random()*10,rd.random()*60)
    print("Posición: ", coche.get_pos())
    del (coche)

pp.store(lista_coches, file)
lista_coches = []
print(lista_coches)
lista_coches = pp.retrieve(file)
for Car in lista_coches:
    print("Marca, Modelo, Combustible, Cilindrada", \
          Car.marca, Car.modelo, Car.combustible, Car.cilindrada)
    print("Posición: ", Car.get_pos(), "\n")


mercedes_1 = Car('Mercedes', 'r350', 'gas', '3500')
Audi_1 = Car("Audi", "RS6", "Gasolina", "4200")
print("Marca ", mercedes_1.marca, 'pos_x ', mercedes_1.pos_x)
print("Marca ", Audi_1.marca, 'pos_x ', Audi_1.pos_x)

mercedes_1.move_to(100, 200, 2000)
Audi_1.move_to(300, 100, 4000)

print("Marca ", mercedes_1.marca, 'pos_x ', mercedes_1.pos_x)
print("Posición Audi_1 ", Audi_1.get_pos())