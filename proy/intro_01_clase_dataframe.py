class Dataframe:

    def __init__(self, variable):
        self.variable = variable
    
    # Media aritmética o promedio
    def media(self):
        return sum(self.variable)/len(self.variable)
    
    def minimo(self):
        return min(self.variable)
    
    def mediana(self):
        n = len(self.variable)
        centro = int(n/2)
        ordenada = sorted(self.variable)
        if n%2 != 0:
            return ordenada[centro]
        return Dataframe([ordenada[centro], ordenada[centro - 1]]).media()
    
    def maximo(self):
        return max(self.variable)
    
    def q1(self):
        pass

    def q3(self):
        pass

    def atipicos(self):
        pass
    
    def muy_atipicos(self):
        pass

    def rango_intercuartilico(self):
        pass

    def medidad_resumen(self):
        pass