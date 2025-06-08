import unittest
from intro_01_clase_dataframe import Dataframe


class TestDataframe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fr = open("/Users/ppando/Materias/python/proy/intro_datos.csv", 'r')
        lista2 = fr.readlines()
        cls.datos = []
        for elem in lista2:                      
            cls.datos.append(int(elem.replace('\n', '')))
        cls.df = Dataframe(cls.datos)
    
    def test_media(self):
        assert TestDataframe.df.media() == 270
    
    def test_mediana(self):
        assert TestDataframe.df.mediana() == 200
    
    def test_minimo(self):
        assert TestDataframe.df.minimo() == 100
    
    def test_maximo(self):
        assert TestDataframe.df.maximo() == 600

unittest.main()