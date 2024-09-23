def subcadenaMasLargaSinRepetidos(cadena):
    vistos = {}
    longitud_maxima = 0
    inicio = 0

    for fin in range(len(cadena)):
        vistos[cadena[fin]] = vistos.get(cadena[fin], 0) + 1
        while vistos[cadena[fin]] > 1:
            vistos[cadena[inicio]] -= 1
            inicio += 1

        longitud_maxima = max(longitud_maxima, fin - inicio + 1)
    return longitud_maxima

resultado = subcadenaMasLargaSinRepetidos('ascdgejjjjdddd')
print(resultado)