def esPar(n):
    return n % 2 == 0

def esPrimo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def esFibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    num = int(input('Introduzca un número: '))
    resultado = f'El número ingresado: {"par" if esPar(num) else "no es par"}, {"primo" if esPrimo(num) else "no es primo"} y {"es parte de la secuencia de Fibonacci" if esFibonacci(num) else "no es parte de la secuencia de Fibonacci"}.'
    print(resultado)

if __name__ == '__main__':
    main()
