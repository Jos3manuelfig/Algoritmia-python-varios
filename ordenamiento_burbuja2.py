def ordenamiento(lista):
    n=len(lista)
    for i in range (n):
        for j in range (0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                
    return lista
    
my_lista=[3,5,7,9,54,1,0,5,-32,-1,-56,687,100,21,46,8]
lista_ordenada=ordenamiento(my_lista)
print(lista_ordenada)