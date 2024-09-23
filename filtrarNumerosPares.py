def pares(lista):
    
    p=[]
    for i in lista:
        if i %2 ==0:
            p.append(i)
            
            
    return p
numeros=list(range(1,100))
print(pares(numeros))



print(pares=[x for x in range(100) if x%2==0])
