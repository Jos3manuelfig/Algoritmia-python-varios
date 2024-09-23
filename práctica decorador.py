def log(func):
    def mensaje(a, b):
        resul = func(a, b)  # Ejecuta la función original
        return f'La suma de {a} + {b} es {resul}...'
    return mensaje

@log
def sumaDosnum(a, b):
    return a + b

resultado = sumaDosnum(2, 4)
print(resultado)  