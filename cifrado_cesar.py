def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():  # Solo cifra letras (ignora espacios, números, etc.)
            base = ord('A') if letra.isupper() else ord('a')
            cifrada = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado += cifrada
        else:
            resultado += letra  # Mantén caracteres no alfabéticos sin cambios
    return resultado

mensaje_original = "HELLO"
desplazamiento = 3
mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)

print(f"Mensaje original: {mensaje_original}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
