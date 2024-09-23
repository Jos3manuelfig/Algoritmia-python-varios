def busqueda_binaria(n, lista):
    lista.sort()  # Ordenamos la lista primero
    ini = 0
    fin = len(lista) - 1

    while ini <= fin:
        medio = (ini + fin) // 2
        if lista[medio] == n:
            return medio  # Retornamos la posición del elemento

        elif lista[medio] > n:
            fin = medio - 1
        else:
            ini = medio + 1

    return -1  # Si no se encuentra el elemento

my_lista = [3, 5, 7, 9, 54, 1, 0, 5687, 100, 21, 46, 8]

try:
    valor_buscado= int(input('ingrse un numero: '))
    
    resul =         busqueda_binaria(valor_buscado, my_lista)

    if resul != -1:
        print(f'El número {valor_buscado} se encuentra en la lista en la posición {resul}')
    else:
        print(f'El valor {valor_buscado} no se encuentra en la lista')
except TypeError:
     print('se esperabas  numeros')
