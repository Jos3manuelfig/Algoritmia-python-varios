import random
import string

def generate_password():
    # Solicitar longitud de la contraseña
    while True:
        try:
            length = int(input("¿Cuántos caracteres desea que tenga la contraseña? "))
            if length <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Preguntar al usuario sobre la inclusión de números, letras y símbolos
    include_numbers = input("¿Desea que la contraseña contenga números? (sí/no) ").strip().lower() == 'sí'
    include_letters = input("¿Desea que la contraseña contenga letras? (sí/no) ").strip().lower() == 'sí'
    include_symbols = input("¿Desea que la contraseña contenga símbolos? (sí/no) ").strip().lower() == 'sí'

    if not include_numbers and not include_letters and not include_symbols:
        print("Debe seleccionar al menos una opción para la contraseña (números, letras o símbolos).")
        return None
    
    # Crear el conjunto de caracteres a usar
    characters = ""
    if include_numbers:
        characters += string.digits
    if include_letters:
        characters += string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    
    # Generar la contraseña
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ejemplo de uso
password = generate_password()
if password:
    print(f"Su nueva contraseña es: {password}")