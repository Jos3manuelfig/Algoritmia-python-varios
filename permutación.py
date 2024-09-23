def permutar(cadena, paso=0):
    if paso == len(cadena):
        print("".join(cadena))
    for i in range(paso, len(cadena)):
        # Intercambiar caracteres en la posición actual con el paso
        cadena[paso], cadena[i] = cadena[i], cadena[paso]
        # Llamada recursiva para el siguiente paso
        permutar(cadena, paso + 1)
        # Backtrack y deshacer el intercambio anterior
        cadena[paso], cadena[i] = cadena[i], cadena[paso]

# Ejemplo de uso
permutar(list("abc"))