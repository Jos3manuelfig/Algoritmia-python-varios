"""Dada una matriz ordenada de números enteros nums , determine si existe un par de números que sumen un objetivo dado.

Ejemplo : Entrada: nums = [1,3,4,6,8,10,13], objetivo = 13 Salida: Verdadero (3 + 10 = 13)

Entrada: nums = [1,3,4,6,8,10,13], objetivo = 6 Salida: Falso"""


def SumaObjetivo(nums: list, objetivo: int) -> bool:

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            suma_objetivo = nums[j] + nums[i]
            if suma_objetivo == objetivo:
                return True
        else:
            return False


mi_lista = [1, 2, 3, 4, 5, 6, 7, 9]
print(SumaObjetivo(mi_lista, 8))
print(SumaObjetivo(mi_lista, 20))
print(SumaObjetivo(mi_lista, 4))
