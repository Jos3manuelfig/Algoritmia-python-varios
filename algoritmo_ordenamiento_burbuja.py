def ordenamiento(lista:list)->list:
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):  # Ajuste aquí
                if lista[j] > lista[j + 1]:
                       lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
    return lista
my_lista1=[4,78,5,2,10,67]
print(ordenamiento(my_lista1))
   