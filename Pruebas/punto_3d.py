from punto import Punto


class Punto3D(Punto):

    def __init__(self, x, y, z):
        Punto.__init__(self, x, y)
        self.z = z

    def get_z(self):
        return self.z

    def __str__(self):
        return Punto.__str__(self) + ',' + str(self.z) + ')'


p = Punto3D(1, 2, 3)
print(p)
