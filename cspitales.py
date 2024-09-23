ciudades = {
    'peru': 'lima',
    'Argentina': 'buenos aires',
    'venezuela': 'caracas'
}

puntos = 0
for ciudad, capital in ciudades.items():
    print('Capital de', ciudad)
    resp = input('Respuesta: ').lower()
    if resp == capital:
        puntos += 10
    else:
        print(f'Lo siento, la capital era {capital}')
    
    print(f'Tu puntuación es {puntos}')

print('Juego terminado. Tu puntuación final es', puntos)