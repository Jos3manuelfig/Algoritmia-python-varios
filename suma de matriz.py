# Crear matrices a y b (sin usar numpy)
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

# Inicializar una matriz c con ceros
c = [[0, 0], [0, 0]]

# Sumar las matrices a y b para obtener la matriz c
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]

# Imprimir las matrices
print("Matriz a:")
for row in a:
    print(row)

print("\nMatriz b:")
for row in b:
    print(row)

print("\nMatriz c (suma de a y b):")
for row in c:
    print(row)
