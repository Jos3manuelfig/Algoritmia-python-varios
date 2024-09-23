import re

texto = "¡Hola, mundo! ¿Cómo estás? Python 3.8 es genial :)"

# Buscar todos los caracteres que no sean letras, números, guiones bajos o espacios en blanco
patron = re.compile(r'[^\w\s]')
resultados = patron.findall(texto)

print(resultados)