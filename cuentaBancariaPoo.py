class Bancaria:
    def __init__(self, nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo
        
    def depositar(self, monto):
        self.saldo += monto
        
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print('Saldo insuficiente')
            
    def mostrar_info(self):
        print(f'Titular: {self.nombre}\nSaldo: {self.saldo}')
        
class cuentaAhorro(Bancaria):
    def __init__(self, nombre, saldo, interes):
        super().__init__(nombre, saldo)
        self.interes = interes
            
    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes
            
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Interés: {self.interes}')
             
# Creación de las cuentas
corriente = Bancaria('Jose', 5000)
ahorro = cuentaAhorro('Ana', 1000, 0.05)

# Mostrar información de las cuentas
corriente.mostrar_info()
ahorro.mostrar_info()