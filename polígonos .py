def calculate_polygon_area(polygon_type, *args):
    if polygon_type.lower() == 'triángulo':
        base, height = args
        return (base * height) / 2
    elif polygon_type.lower() == 'cuadrado':
        side = args[0]
        return side ** 2
    elif polygon_type.lower() == 'rectángulo':
        length, width = args
        return length * width
    else:
        return "Polígono no soportado"

# Ejemplos de cálculo de área
print(f"Área de un triángulo: {calculate_polygon_area('triángulo', 10, 5)}")
print(f"Área de un cuadrado: {calculate_polygon_area('cuadrado', 4)}")
print(f"Área de un rectángulo: {calculate_polygon_area('rectángulo', 8, 3)}")
