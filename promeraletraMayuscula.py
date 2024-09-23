def capitalizar_primera_letra(texto):
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Capitalizar la primera letra de cada palabra
    palabras_capitalizadas = []
    for palabra in palabras:
        if palabra:  # Verificar que la palabra no esté vacía
            primera_letra = palabra[0].upper()
            # Reconstruir la palabra con la primera letra en mayúscula
            palabra_capitalizada = primera_letra + palabra[1:]
            palabras_capitalizadas.append(palabra_capitalizada)
        else:
            palabras_capitalizadas.append(palabra)
    
    # Unir las palabras capitalizadas en una cadena de texto
    texto_capitalizado = ' '.join(palabras_capitalizadas)
    
    return texto_capitalizado

# Ejemplo de uso
cadena_entrada = "hola mundo! esto es un ejemplo."
print(capitalizar_primera_letra(cadena_entrada))
