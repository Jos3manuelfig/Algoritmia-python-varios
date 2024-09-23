def sumapar(lista:list,n:int):
    for i in range (len(lista)):
        for j in range(i+1,len(lista)):
            suma=lista[i]+lista[j]
            if suma==n:
                return True
           
        return False
                 

miList=[1,2,3]


print(sumapar(miList,9))