import random

def ruleta_rusa():
    # Crear una lista con 6 posiciones, una de ellas es una bala (True) y las demás están vacías (False)
    tambor = [False, False, False, False, False, True]
    # Revolver el tambor
    random.shuffle(tambor)
    
    # Girar el tambor y disparar
    posicion = random.randint(0, 5)
    if tambor[posicion]:
        print("¡Bang! Te has disparado.")
    else:
        print("Clic. Estás a salvo.")
    
# Ejecutar el juego
ruleta_rusa()