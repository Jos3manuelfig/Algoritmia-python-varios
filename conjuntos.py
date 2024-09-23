def custom_array_operation(arr1, arr2, find_common):
    # Inicializa el array de resultado
    result = []
    
    # Si find_common es True, busca los elementos comunes
    if find_common:
        # Itera sobre el primer array
        for element in arr1:
            # Si el elemento está en ambos arrays y no está en el resultado, agrégalo al resultado
            if element in arr2 and element not in result:
                result.append(element)
    else:
        # Si find_common es False, busca los elementos no comunes
        # Itera sobre ambos arrays
        for element in arr1 + arr2:
            # Si el elemento es único en uno de los arrays, agrégalo al resultado
            if (element in arr1) != (element in arr2) and element not in result:
                result.append(element)
    
    # Retorna el array de resultado
    return result

# Ejemplo de uso:
# Define dos arrays
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

# Llama a la función con find_common como True
print(array1)
print(array2)
elementos_comunes = custom_array_operation(array1, array2, True)
print("Elementos comunes:", elementos_comunes)

# Llama a la función con find_common como False
elementos_no_comunes = custom_array_operation(array1, array2, False)
print("Elementos no comunes:", elementos_no_comunes)
