"""Class y object (Código estructurado I)"""
#Class "paquetizar" datos y funciones en una misma entidad
#Define el tipo de dato
#Object: variables y metodos dentro de las clases
#Ej: datos_coche es una clase y lista_coches es el obajeto
#Podemos tener variables que las compartan todos los objetos de una clase.
#Función de clase 1: __init_
#Función de clase 2:
#Variable self(hace referencia al objeto)
"""Ejercicio Clase 10"""
class Car:
    def __init__(self, marca_coche, modelo_coche, combustible, cilindrada):
        self.marca = marca_coche
        self.modelo = modelo_coche
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, pos_x, pos_y, cilindrada):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cilindrada = cilindrada

    def move_incr(self, x, y):
        self.pos_x = self.pos_x + x #poner esto
        self.pos_y += y             #Y poner esto, es lo mismo!

    def get_pos(self):
        return self.pos_x, self.pos_y

mercedes_1 = Car('Mercedes', 'r350', 'gas', '3500')
Audi_1 = Car("Audi", "RS6", "Gasolina", "4200")
print("Marca ", mercedes_1.marca, 'pos_x ', mercedes_1.pos_x)
print("Marca ", Audi_1.marca, 'pos_x ', Audi_1.pos_x)

mercedes_1.move_to(100, 200, 2000)
Audi_1.move_to(300, 100, 4000)

print("Marca ", mercedes_1.marca, 'pos_x ', mercedes_1.pos_x)
print("Posición Audi_1 ", Audi_1.get_pos())