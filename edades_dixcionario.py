# Programa para calcular la edad de 3 personas usando diccionarios

# Importamos la biblioteca necesaria
from datetime import datetime

# Pedimos al usuario que ingrese el año actual
anio_actual = int(input("Por favor, ingresa el año actual: "))

# Inicializamos un diccionario vacío para almacenar los datos
datos_personas = {}

# Creamos un bucle para pedir los datos de las 3 personas
for i in range(1, 4):
    nombre = input(f"Ingresa el nombre de la persona {i}: ")
    anio_nacimiento = int(input(f"Ingresa el año de nacimiento de {nombre}: "))
    # Calculamos la edad y la almacenamos en el diccionario
    datos_personas[nombre] = anio_actual - anio_nacimiento

# Imprimimos las edades de las personas
for nombre, edad in datos_personas.items():
    print(f"{nombre} tiene {edad} años.")

# Fin del programa
