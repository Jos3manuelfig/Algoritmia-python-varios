import random 

def ordenamiento(lista):
    n=len(lista)
    for i in range (n):
        for j in range(0,n-i-1):
            if lista[j] >lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
        
my_lista=[random.randint(1,20) for _ in range (20)]

resultado=ordenamiento(my_lista)
if resultado:
    print(f'Lista Ordenada:  {resultado}')


