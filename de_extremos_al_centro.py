"""Dada una matriz ordenada de números enteros nums , determine si existe un par de números que sumen un objetivo dado.

Ejemplo : Entrada: nums = [1,3,4,6,8,10,13], objetivo = 13 Salida: Verdadero (3 + 10 = 13)

Entrada: nums = [1,3,4,6,8,10,13], objetivo = 6 Salida: Falso"""


def SumaObjetivo(nums: list, objetivo: int) -> bool:
    inicio, fin = 0, len(nums) - 1
    while inicio < fin:
        suma = nums[inicio] + nums[fin]
        if suma == objetivo:
            return True

        if suma < objetivo:
            inicio += 1
        else:
            fin -= 1

    return False


mi_lista = [1, 3, 4, 6, 8, 10, 13]
print(SumaObjetivo(mi_lista, 14))
print(SumaObjetivo(mi_lista, 18))
print(SumaObjetivo(mi_lista, 27))
print(SumaObjetivo(mi_lista, 32))
