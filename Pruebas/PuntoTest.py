import unittest
from Punto import Punto


class PuntoTest(unittest.TestCase):

    def test_distancia(self):
        p = Punto(3, 4)
        self.assertEqual(p.distancia(Punto(0, 0)), 5.0)

    def test_getx(self):
        p = Punto(3, 4)
        self.assertEqual(p.get_x(), 3)




