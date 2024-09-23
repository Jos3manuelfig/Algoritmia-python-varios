def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth number.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
    
    Returns:
        list: A list containing the first n Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Genera los primeros 17 números de Fibonacci
n = 17
fibonacci_numbers = fibonacci_sequence(n)

# Imprime los números de Fibonacci
print(f"Los primeros {n} números de Fibonacci son: {fibonacci_numbers}")

        