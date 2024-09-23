class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def __actualizar_saldo(self, cantidad):  # Método privado
        self.__saldo += cantidad

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__actualizar_saldo(cantidad)
            print(f"Se han depositado {cantidad} unidades.")
        else:
            print("La cantidad debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__actualizar_saldo(-cantidad)
            print(f"Se han retirado {cantidad} unidades.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo

# Uso de la clase
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())  # Muestra: 1500
cuenta.retirar(200)
print(cuenta.obtener_saldo())  # Muestra: 1300