import math


class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clonar(self, p):
        self.x = p.x
        self.y = p.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distancia(self, p):
        return math.hypot(self.x - p.x, self.y - p.y)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p1 = Punto(2, 3)
print(p1.get_x())
p2 = Punto(4, 5)
p1.clonar(p2)
print(p1.get_x())
p3 = Punto(3, 4)
print(p3.distancia(Punto(0, 0)))
print(p1, p2, p3)
