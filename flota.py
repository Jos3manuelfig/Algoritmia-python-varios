class Motor:
    def arrancar(self):
        print('Motor Arrancando')

class MotorElectrico:
    def arrancar(self):
        print('Arrancando Motor Eléctrico')

class MotorDiesel:
    def arrancar(self):
        print('Arrancando Motor con Ruido')

class Carro:
    def __init__(self, motor: Motor):
        self.motor = motor
    
    def arrancar(self):
        print('Arrancando Carro')
        self.motor.arrancar()

    def frenar(self):
        print('Frenando Carro')

class Camion:
    def __init__(self, motorE: MotorElectrico):
        self.motorE = motorE
    
    def arrancar(self):
        print('Arrancando Camión')
        self.motorE.arrancar()

    def frenar(self):
        print('Frenando Camión')

class Motocicleta:
    def __init__(self, motorD: MotorDiesel):
        self.motorD = motorD
    
    def arrancar(self):
        print('Arrancando Motocicleta')
        self.motorD.arrancar()

    def frenar(self):
        print('Frenando Motocicleta')

class Flota:
    def __init__(self):
        self.flota: List = []
    
    def agregar_vehiculo(self, vehiculo):
        self.flota.append(vehiculo)
    
    def arrancar_todos(self):
        for vehiculo in self.flota:
            vehiculo.arrancar()

    def frenar_todos(self):
        for vehiculo in self.flota:
            vehiculo.frenar()

# Ejemplo de uso:
motor_gasolina = Motor()
motor_electrico = MotorElectrico()
motor_diesel = MotorDiesel()

carro = Carro(motor_gasolina)
camion = Camion(motor_electrico)
motocicleta = Motocicleta(motor_diesel)

flota = Flota()
flota.agregar_vehiculo(carro)
flota.agregar_vehiculo(camion)
flota.agregar_vehiculo(motocicleta)

flota.arrancar_todos()  # Arrancar todos los vehículos
flota.frenar_todos()    # Frenar todos los vehículos