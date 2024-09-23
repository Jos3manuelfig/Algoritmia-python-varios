"""
 * Crea una función que ordene y retorne una lista de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 """
def ordenar_matriz(matriz, orden):
    """
    Ordena una matriz de números.

    Args:
        matriz (list): La matriz de números a ordenar.
        orden (str): Puede ser "Asc" para ordenar de menor a mayor o "Desc" para ordenar de mayor a menor.

    Returns:
        list: La matriz ordenada.
    """
    if orden == "Asc":
        for i in range(len(matriz)):
            for j in range(i + 1, len(matriz)):
                if matriz[i] > matriz[j]:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
    elif orden == "Desc":
        for i in range(len(matriz)):
            for j in range(i + 1, len(matriz)):
                if matriz[i] < matriz[j]:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
    else:
        raise ValueError("El parámetro 'orden' debe ser 'Asc' o 'Desc'.")

    return matriz

# Ejemplo de uso:
mi_matriz = [2, 4, 6, 8, 9]
orden_ascendente = ordenar_matriz(mi_matriz, "Asc")
orden_descendente = ordenar_matriz(mi_matriz, "Desc")

print("Matriz original:", mi_matriz)
print("Matriz ordenada (ascendente):", orden_ascendente)
print("Matriz ordenada (descendente):", orden_descendente)
