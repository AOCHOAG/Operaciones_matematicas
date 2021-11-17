"""Car class"""

class Car:
    def __init__(self, marca_coche, modelo_coche, combustible, cilindrada):
        self.marca = marca_coche
        self.modelo = modelo_coche
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


    def move_incr(self, x, y):
        self.pos_x = self.pos_x + x #poner esto
        self.pos_y += y             #Y poner esto, es lo mismo!

    def get_pos(self):
        return self.pos_x, self.pos_y