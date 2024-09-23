array = [[0 for _ in range(5)] for _ in range(5)]

def mostrar_array():
    for elemento in array:
        print(' '.join(map(str, elemento)))

def rellenar_array():
    for i in range(len(array)):
        for j in range(len(array[i])):
            valor = input(f'Ingrese un valor en la posición ({i}, {j}): ')
            array[i][j] = valor
            mostrar_array()  # Muestra el array después de cada entrada

def main():
    mostrar_array()  # Muestra el array inicial (todo en ceros)
    rellenar_array()  # Permite al usuario rellenar el array

if __name__ == '__main__':
    main()