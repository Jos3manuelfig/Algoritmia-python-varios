from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14 * (self.radio ** 2)

# Crear objetos de las clases Rectangulo y Circulo
mi_rectangulo = Rectangulo(4, 5)
mi_circulo = Circulo(3)

print(mi_rectangulo.area())  # Output: 20
print(mi_circulo.area())     # Output: 28.26