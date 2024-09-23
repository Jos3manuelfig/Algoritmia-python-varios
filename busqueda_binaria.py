def busqueda_binaria(lista, x):
    """
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en la lista;
    Devuelve p tal que lista[p] == x, si x está en la lista
    """
    izq = 0  # Índice de inicio del segmento
    der = len(lista) - 1  # Índice de fin del segmento

    while izq <= der:
        medio = (izq + der) // 2  # Punto medio del segmento
        print("DEBUG: izq:", izq, "der:", der, "medio:", medio)

        if lista[medio] == x:
            return medio  # Valor encontrado en el punto medio
        elif lista[medio] > x:
            der = medio - 1  # Buscar en el segmento izquierdo
        else:
            izq = medio + 1  # Buscar en el segmento derecho

    return -1  # Valor no encontrado en la lista

# Ejemplo de uso
mi_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
valor_buscado = 21
resultado = busqueda_binaria(mi_lista, valor_buscado)

if resultado != -1:
    print(f"El valor {valor_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no está en la lista.")
