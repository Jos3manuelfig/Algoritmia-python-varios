class Operaciones:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        return self.n1 + self.n2

    def restar(self):
        return self.n1 - self.n2

    def multiplicar(self):
        return self.n1 * self.n2

    def dividir(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Error: División por cero"

# Ejemplo de uso
operacion = Operaciones(10, 5)
print(operacion.sumar())       # Salida: 15
print(operacion.restar())      # Salida: 5
print(operacion.multiplicar()) # Salida: 50
print(operacion.dividir())     # Salida: 2.0