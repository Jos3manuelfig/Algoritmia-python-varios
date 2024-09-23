def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth number.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
    
    Returns:
        list: A list containing the first n Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Solicita al usuario ingresar un número
try:
    user_input = int(input("Ingresa un número para generar la lista de Fibonacci: "))
    if user_input < 0:
        print("Por favor ingresa un número positivo.")
    else:
        fibonacci_numbers = fibonacci_sequence(user_input)
        print(f"Los números de Fibonacci hasta {user_input} son: {fibonacci_numbers}")
except ValueError:
    print("Por favor ingresa un número válido.")
