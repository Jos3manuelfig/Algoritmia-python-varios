'''Crea un programa en Python que analice un texto dado y proporcione las siguientes estadísticas:Número total de palabras.Número total de oraciones.Promedio de palabras por oración.Las 5 palabras más comunes y su frecuencia.Número de palabras únicas (palabras que aparecen una sola vez).'''

import re
from collections import Counter

def analizar_texto(texto):
    # Limpieza del texto
    texto = re.sub(r'[^\w\s]', '', texto).lower()
    palabras = texto.split()
    
    # Cálculo de estadísticas
    num_palabras = len(palabras)
    oraciones = re.split(r'[.!?]', texto)
    oraciones = [oracion.strip() for oracion in oraciones if oracion.strip()]
    num_oraciones = len(oraciones)
    promedio_palabras_por_oracion = num_palabras / num_oraciones if num_oraciones > 0 else 0
    frecuencia_palabras = Counter(palabras)
    palabras_mas_comunes = frecuencia_palabras.most_common(5)
    palabras_unicas = len([palabra for palabra, freq in frecuencia_palabras.items() if freq == 1])
    
    # Resultados
    print(f'Número total de palabras: {num_palabras}')
    print(f'Número total de oraciones: {num_oraciones}')
    print(f'Promedio de palabras por oración: {promedio_palabras_por_oracion:.2f}')
    print(f'Palabras más comunes: {palabras_mas_comunes}')
    print(f'Número de palabras únicas: {palabras_unicas}')

# Texto de prueba
texto = input("Introduce el texto a analizar: ")
analizar_texto(texto)