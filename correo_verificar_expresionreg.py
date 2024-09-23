import re

def validar_regular(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, correo):
        print(f'El correo: {correo} Es Valido')
    else:
          print('Correo Invalido')




# Ejemplo de u
        




