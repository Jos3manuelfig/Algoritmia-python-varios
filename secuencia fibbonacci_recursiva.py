def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Ejemplo de uso:
n = 20  # Obtener los primeros 10 números de Fibonacci
print(f"La secuencia de Fibonacci de los primeros {n} números es: {fibonacci(n)}")
