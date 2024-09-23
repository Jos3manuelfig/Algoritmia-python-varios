def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12, 22, 11, 90]
mi_lista_ordenada = ordenamiento_burbuja(mi_lista)
print(mi_lista_ordenada)
