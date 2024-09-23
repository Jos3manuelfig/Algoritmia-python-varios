def contar_vocales(texto):
    # Creamos un diccionario para almacenar la frecuencia de cada vocal
    frecuencia_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convertimos el texto a minúsculas para evitar problemas de mayúsculas/minúsculas
    texto = texto.lower()

    # Recorremos cada caracter del texto
    for char in texto:
        if char in 'aeiou':
            # Si es una vocal, incrementamos su contador en el diccionario
            frecuencia_vocales[char] += 1

    # Buscamos la vocal con la mayor frecuencia
    vocal_mas_repetida = max(frecuencia_vocales, key=frecuencia_vocales.get)
    cantidad_repeticiones = frecuencia_vocales[vocal_mas_repetida]

    return vocal_mas_repetida, cantidad_repeticiones

# Pedimos al usuario que ingrese un texto
texto_usuario = input("Ingresa un texto: ")

# Obtenemos la vocal más repetida y su frecuencia
vocal, repeticiones = contar_vocales(texto_usuario)

print(f"La vocal más repetida en el texto es '{vocal}' con {repeticiones} repeticiones.")
