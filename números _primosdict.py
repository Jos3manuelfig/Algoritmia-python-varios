def es_primo(*numeros):
    resultados = {}
    for num in numeros:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    resultados[num] = False
                    break
            else:
                resultados[num] = True
        else:
            resultados[num] = False
    return resultados

# Prueba de la función con los números 10, 7 y 2
print(es_primo(10, 7, 2))
