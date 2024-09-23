def fibonacci(n):
    if n < 0:
        return "La serie de Fibonacci solo acepta números positivos"
    
    lista_fibonacci = [0, 1]
    
    def recursion(numero, lista):
        if lista[-1] + lista[-2] > n:
            return lista
        else:
            lista.append(lista[-1] + lista[-2])
            return recursion(numero, lista)
    
    return recursion(n, lista_fibonacci)

if __name__ == "__main__":
    try:
        num = int(input("Ingresa un número para calcular la serie de Fibonacci: "))
        resultado = fibonacci(num)
        print(f"La serie de Fibonacci hasta el {num}-ésimo término es: {resultado}")
    except ValueError:
        print("Se espera un número entero positivo.")
