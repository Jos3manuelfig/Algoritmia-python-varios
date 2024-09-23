def imprimir_triangulo(altura):
    if altura > 0:
        for i in range(1, altura + 1):
            print(' ' * (altura - i) + '* ' * i)
    elif altura < 0:
        for i in range(-altura, 0, -1):
            print(' ' * (-altura - i) + '* ' * i)

numero = int(input("Por favor, introduce un número: "))
imprimir_triangulo(numero)
