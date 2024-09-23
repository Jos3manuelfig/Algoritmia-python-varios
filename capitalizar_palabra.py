def capitalizar_palabras(texto):
    return ' '.join(palabra.capitalize() for palabra in texto.split())

# Ejemplo de uso:
texto = "hola mundo"
print(capitalizar_palabras(texto))

