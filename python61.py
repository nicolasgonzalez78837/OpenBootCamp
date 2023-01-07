class Vehiculo():
    # inicializamos los atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return 'Color {}, {} ruedas'.format( self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return 'Color {}, {} km/h, {} ruedas, {} puertas, {} cc'.format(self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada)
coche = Coche("Verde", 4, 4, 250, 1300)
print(coche)
