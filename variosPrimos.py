def Esprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def validarVarios(*args):
    for numero in args:
        if Esprimo(numero):
            print(f'El Numero {numero} Es Primo')
        else: 
            print(f'El numero {numero} No es Primo')

numeros = input('Introduzca los numeros separados por (,): ')
listanumeros = [int(x) for x in numeros.split(',')]
validarVarios(*listanumeros)