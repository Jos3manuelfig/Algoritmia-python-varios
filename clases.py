class Carro:
    ruedas = 4
    
    def __init__(self, color, modelo):
        self.color = color
        self.modelo = modelo
        self.velocidad = 0  # Inicializamos la velocidad en 0
    
    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print(f'Vehículo acelera a {self.velocidad} km/h')
         
    def frenar(self):
        self.velocidad = 0  # Detenemos el vehículo
        print('Vehículo detenido')
                  
carro1 = Carro('blanco', 'chevrolet')
class carroDeportivo(Carro)
     def __init__(self, color, modelo,tipo):
     super()._(color,modelo)
self.tipo=tipo
carro1.acelerar(50)
carro1.acelerar(50)
carro1.acelerar(50)


  # Vehículo acelera a 50 km/h
carro1.frenar()      # Vehículo detenido
print(f'Ruedas: {carro1.ruedas}')
