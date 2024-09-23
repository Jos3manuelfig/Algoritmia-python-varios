def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

mi_lista = [1, 2, 3, 4, 5]
print(suma_lista(mi_lista))  # Salida: 15
