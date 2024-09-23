class Motor:
    def arrancar(self):
        print('Motor Arrancando')

class MotorElectrico(Motor):
    def arrancar(self):
        print('Arrancando Motor Eléctrico')

class MotorDiesel(Motor):
    def arrancar(self):
        print('Arrancando Motor Diesel con Ruido')


class Vehiculo:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        print('Arrancando Vehículo')
        self.motor.arrancar()

    def frenar(self):
        print('Frenando Vehículo')



class Carro(Vehiculo):
    def arrancar(self):
        print('Arrancando Carro')
        super().arrancar()

class Camion(Vehiculo):
    def arrancar(self):
        print('Arrancando Camión')
        super().arrancar()

class Motocicleta(Vehiculo):
    def arrancar(self):
        print('Arrancando Motocicleta')
        super().arrancar()

class Flota:
    def __init__(self):
        self.flota = []

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