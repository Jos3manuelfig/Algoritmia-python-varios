def dibujar_cuadrado(lado):
    for i in range(lado):
        print("*" * lado)

def dibujar_triangulo(lado):
    for i in range(1, lado + 1):
        print("*" * i)

# Solicitar al usuario el tamaño del lado y la figura deseada
tamaño_lado = int(input("Ingresa el tamaño del lado: "))
figura = input("¿Quieres dibujar un cuadrado o un triángulo? (c/t): ")

if figura.lower() == "c":
    dibujar_cuadrado(tamaño_lado)
elif figura.lower() == "t":
    dibujar_triangulo(tamaño_lado)
else:
    print("Opción no válida. Por favor, elige 'c' para cuadrado o 't' para triángulo.")

 