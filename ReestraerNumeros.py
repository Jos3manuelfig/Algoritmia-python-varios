import re

# Expresión regular para encontrar números en una cadena
regex = r'\d+'

# Ejemplo de cadena
text = "En 2021, la población era de 7.8 billones y en 2023, se espera que sea 8 billones."

# Encuentra todas las ocurrencias de números en la cadena
numbers = re.findall(regex, text)

print("Números encontrados:", numbers)