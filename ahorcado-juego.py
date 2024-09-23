import random
import os

MAX_FALLOS = 5
paises = ['Barbados', 'Belice', 'Bolivia', 'Brasil', 'Colombia', 'Costa Rica', 'Cuba', 'Chile', 'Ecuador', 'El Salvador', 'Guatemala', 'Guayana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Peru', 'Argentina', 'Venezuela']

def crear_cadenas():
    pais = random.choice(paises).lower()
    secreto = '_' * len(pais)
    return pais, secreto

def reemplazar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos + 1:]
        inicio = pos + 1
    return secreto

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def ahorcado():
    original, secreto = crear_cadenas()
    fallos = 0
    while secreto != original and fallos < MAX_FALLOS:
        limpiar_pantalla()
        print(f'Palabra: {secreto}')
        s = input('¿Qué símbolo quieres? ').lower()
        if len(s) != 1 or not s.isalpha():
            print('Por favor, introduce un solo carácter válido.')
            input('Presiona Enter para continuar...')
            continue
        if s in original:
            secreto = reemplazar_simbolo(original, secreto, s)
            print('¡Bien hecho!')
        else:
            print('Lo siento, no es parte de la palabra.')
            fallos += 1
        input('Presiona Enter para continuar...')

    limpiar_pantalla()
    if secreto == original:
        print(f'¡Felicidades! Es la palabra: {secreto}')
    else:
        print(f'Lo siento, el país era {original}. ¡Vuelve a intentarlo!')

def main():
    ahorcado()

if __name__ == '__main__':
    main()