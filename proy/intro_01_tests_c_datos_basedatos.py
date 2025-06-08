import unittest
import sqlite3
from intro_01_clase_dataframe import Dataframe


class TestDataframe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = sqlite3.connect("/Users/ppando/Materias/python/proy/intro_datos.db") # si no existe, la crea
        cur = cls.con.cursor()
        cur.execute("CREATE TABLE datos(id INTEGER PRIMARY KEY AUTOINCREMENT, value INTEGER NOT NULL)")
        cur.execute("INSERT INTO datos (value) VALUES (100), (200), (200), (250), (600)")
        cls.con.commit()
        cls.datos = []
        for row in cur.execute("SELECT value FROM datos"):                      
            cls.datos.append(row[0])
        cls.df = Dataframe(cls.datos)
    
    def test_media(self):
        assert TestDataframe.df.media() == 270
    
    def test_mediana(self):
        assert TestDataframe.df.mediana() == 200
    
    def test_minimo(self):
        assert TestDataframe.df.minimo() == 100
    
    def test_maximo(self):
        assert TestDataframe.df.maximo() == 600
    
    @classmethod
    def tearDownClass(cls):
        cls.con.cursor().execute("DROP TABLE datos")
        cls.con.close()

unittest.main()