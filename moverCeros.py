"""
    Dado un arreglo de números enteros nums , escriba una función para reorganizar el arreglo moviendo 
    todos los ceros al final mientras mantiene el orden de los elementos distintos de cero sin cambios. 
    Realice esta operación en el lugar sin crear una copia del arreglo.
    
    EJEMPLO:
    Entrada:
    nums = [2,0,4,0,9,7,0,6,0,5]
    Salida:
    nums = [2,4,9,7,6,5,0,0,0,0]
    
    
"""


def moverCeros(nums: int) -> list:
    paso = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[paso], nums[i] = nums[i], nums[paso]
            paso += 1
    return nums


numeros = [2, 0, 4, 0, 9, 7, 0, 6, 0, 5]
print(moverCeros(numeros))
