"""
    Escriba una función para ordenar una matriz de números enteros dada nums en el lugar 
    (sin usar la función de ordenación incorporada),
    donde la matriz contiene n números enteros que son 0, 1 y 2 
    y representan los colores rojo, blanco y azul.
    Organice los objetos de modo que los del mismo color estén adyacentes, 
    en el orden rojo, blanco y azul (0, 1, 2).
    
    EJEMPLO
    dada  nums = [2,1,2,0,1,0,1,0,1]
    
    salida:
    [0,0,0,1,1,1,1,2,2]
    

    """


def ordenaColor(lista: list):
    inicio = 0
    final = len(lista) - 1
    i = 0

    while i <= final:
        if lista[i] == 0:
            lista[i], lista[inicio] = lista[inicio], lista[i]
            inicio += 1
            i += 1
        if lista[i] == 2:
            lista[final], lista[i] = lista[i], lista[final]
            final -= 1
        else:
            i += 1
    return lista


mi_lista = [2, 1, 2, 0, 1, 0, 1, 0, 1]
print(ordenaColor(mi_lista))
