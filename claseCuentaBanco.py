class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositó: {cantidad}")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se retiró: {cantidad}")
        else:
            print("Saldo insuficiente para retirar esa cantidad.")

    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

# Crear una instancia de la clase Cuenta
cliente = Cuenta('Jose Figuera', 1000)

# Mostrar los detalles iniciales
cliente.mostrar()

# Realizar un depósito
cliente.depositar(500)

# Mostrar los detalles después del depósito
cliente.mostrar()

# Intentar retirar más dinero del saldo actual
cliente.retirar(1500)

# Mostrar los detalles después del intento de retiro
cliente.mostrar()
