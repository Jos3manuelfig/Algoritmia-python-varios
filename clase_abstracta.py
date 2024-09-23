from abc import ABC, abstractmethod

# Clase abstracta
class Pago(ABC):

    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

    def imprimir_recibo(self, cantidad):
        print(f"Recibo: Pago de ${cantidad}")

# Clase concreta para pago con tarjeta de crédito
class PagoTarjetaCredito(Pago):

    def __init__(self, numero_tarjeta, titular_tarjeta):
        self.numero_tarjeta = numero_tarjeta
        self.titular_tarjeta = titular_tarjeta

    def procesar_pago(self, cantidad):
        # Lógica para procesar el pago con tarjeta de crédito
        print(f"Procesando pago con tarjeta de crédito de ${cantidad} para {self.titular_tarjeta}")
        self.imprimir_recibo(cantidad)

# Clase concreta para pago con PayPal
class PagoPayPal(Pago):

    def __init__(self, email):
        self.email = email

    def procesar_pago(self, cantidad):
        # Lógica para procesar el pago con PayPal
        print(f"Procesando pago con PayPal de ${cantidad} para {self.email}")
        self.imprimir_recibo(cantidad)

# Uso de las clases
metodo_pago1 = PagoTarjetaCredito("1234-5678-9876-5432", "Juan Pérez")
metodo_pago1.procesar_pago(100)

metodo_pago2 = PagoPayPal("juan.perez@example.com")
metodo_pago2.procesar_pago(200)