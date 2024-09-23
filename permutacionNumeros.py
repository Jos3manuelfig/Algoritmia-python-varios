def factorial(n:int):
    if n==0:
        return 1
    return n * factorial(n-1)


def generar_permutaciones(lista, paso=0):
    if paso == len(lista):
        print(lista)
    for i in range(paso, len(lista)):
        # Intercambiar números en la posición actual con el paso
        lista[paso], lista[i] = lista[i], lista[paso]
        # Llamada recursiva para el siguiente paso
        generar_permutaciones(lista, paso + 1)
        # Backtrack y deshacer el intercambio anterior
        lista[paso], lista[i] = lista[i], lista[paso]

# Ejemplo de uso
numeros = [1, 2, 3]
generar_permutaciones(numeros)
r=len(numeros)
comb=factorial(r)
print(' Posibles combinaciones:', comb)