 import math

def log_circu(funct):
    def calculo(radio):
        area = funct(radio)
        print(f'El área del círculo es {area}')
        return area
    return calculo

@log_circu
def calcular(radio):
    return math.pi * radio**2

r = 7
area = calcular(r)  