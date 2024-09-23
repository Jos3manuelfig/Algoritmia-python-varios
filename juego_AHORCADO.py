import random

# Dibujo del ahorcado
AHORCADO = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

# Lista de palabras para el juego
palabras = 'valor aprenderpython comida jugar python web programacion videojuegos computador perros mascota pies arbol libros dinero lapiz telefono amor discos software libre propio cancion collar sol luna juguete españa escuela universidad'.split()

def buscarPalabraAleat(listaPalabras):
    # Devuelve una palabra elegida aleatoriamente
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def main():
    palabra_secreta = buscarPalabraAleat(palabras)
    intentos = 6
    letras_adivinadas = []
    
    while intentos > 0:
        letra = input("Ingresa una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("¡Ya adivinaste esa letra!")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto! Letras adivinadas:", " ".join(letras_adivinadas))
        else:
            intentos -= 1
            print(AHORCADO[6 - intentos])
            print(f"Te quedan {intentos} intentos")
        
        if set(palabra_secreta) == set(letras_adivinadas):
            print(f"¡Ganaste! La palabra era '{palabra_secreta}'.")
            break
    
    if intentos == 0:
        print(f"¡Perdiste! La palabra era '{palabra_secreta}'.")

if __name__ == "__main__":
    main()
