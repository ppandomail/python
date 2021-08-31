class Automovil:

    def __init__(self, marca, color, velocidad_maxima):
        self.marca = marca
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def acelerar(self, velocidad):
        if self.encendido:
            if self.velocidad_actual + velocidad > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual += velocidad
        self.mostrar_velocimetro()

    def frenar(self, velocidad):
        if self.encendido:
            if self.velocidad_actual - velocidad < 0:
                self.velocidad_actual = 0
            else:
                self.velocidad_actual -= velocidad
        self.mostrar_velocimetro()

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def mostrar_velocimetro(self):
        print('La velocidad actual es de ' + str(self.velocidad_actual) + ' de ' + str(self.velocidad_maxima))


mi_auto = Automovil('Ford', 'gris', 180)
print(mi_auto.marca)
print(mi_auto.color)
mi_auto.encender()
mi_auto.mostrar_velocimetro()
mi_auto.acelerar(190)
mi_auto.acelerar(20)
mi_auto.frenar(50)
mi_auto.acelerar(20)
mi_auto.apagar()
