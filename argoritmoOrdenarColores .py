def ordenarLista(lista: list) -> list:
    ini = 0
    fin = len(lista) - 1
    i = 0
    while i <= fin:
        if lista[i] == 0:
            lista[i], lista[ini] = lista[ini], lista[i]
            i += 1
            ini += 1
        elif lista[i] == 2:
            lista[i], lista[fin] = lista[fin], lista[i]
            fin -= 1
        else:
            i += 1
    return lista

my_lista = [2, 1, 2, 0, 1, 0, 1, 0, 1, 2, 1, 2, 0, 1, 0, 1, 0, 1, 2, 1, 2, 0, 1, 0, 1, 0, 1,0,1,1,2]
print(ordenarLista(my_lista))