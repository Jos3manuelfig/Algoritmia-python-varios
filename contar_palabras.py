def contar_frecuencia_palabras(texto):
    # Eliminar la puntuación del texto
    puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in puntuacion:
        texto = texto.replace(char, "")

    # Convertir el texto a minúsculas para hacer el conteo insensible a mayúsculas
    texto = texto.lower()

    # Dividir el texto en palabras
    palabras = texto.split()

    # Inicializar un diccionario para almacenar el conteo de palabras
    conteo_palabras = {}

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1

    # Devolver el diccionario de conteo de palabras
    return conteo_palabras

# Ejemplo de uso
texto_ejemplo = "¡Hola mundo! Esto es una prueba. Hola de nuevo, mundo."
frecuencia_palabras = contar_frecuencia_palabras(texto_ejemplo)
for palabra, cantidad in frecuencia_palabras.items():
    print(f"La palabra '{palabra}' aparece {cantidad} veces.")
