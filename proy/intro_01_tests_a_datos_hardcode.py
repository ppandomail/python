'''
Son los tests que validan el correcto
funcionamiento de la clase Dataframe
'''

import unittest
from intro_01_clase_dataframe import Dataframe


class TestDataframe(unittest.TestCase):

    def test_media(self):
        df = Dataframe([100, 200, 200, 250, 600])
        assert df.media() == 270
    
    def test_mediana_n_impar(self):
        df = Dataframe([100, 200, 900, 250, 600])
        assert df.mediana() == 250
    
    def test_mediana_n_par(self):
        df = Dataframe([100, 200, 900, 250, 600, 350])
        assert df.mediana() == 300
    
    def test_minimo(self):
        df = Dataframe([100, 200, 900, 250, 600])
        assert df.minimo() == 100
    
    def test_maximo(self):
        df = Dataframe([100, 200, 900, 250, 600])
        assert df.maximo() == 900
    
    @unittest.skip('demostrando skipping')
    def test_resumen(self):
        self.assertEqual(True, True)
    
unittest.main()