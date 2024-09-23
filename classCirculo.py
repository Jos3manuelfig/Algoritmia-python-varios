import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * (self.radio ** 2)
        
    def perimetro(self):
        return 2 * math.pi * self.radio
        
c1 = Circulo(1)
print("Área:", c1.area())
print("Perímetro:", c1.perimetro())