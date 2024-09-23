def orden_reverse(lista):
    inicio=0
    fin=len(lista)-1
    while inicio< fin:
        lista[inicio],lista[fin]=lista[fin],lista[inicio]
        lista[inicio]+=1
        lista[fin]-=1
        
        return lista
        
        
print(orden_reverse([1,2,3,4,5]))