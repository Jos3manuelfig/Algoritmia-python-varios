def sumapar(lista:list,objetivo:int):
    inicio=0
    final =len(lista)-1
    while inicio < final:
         suma=lista[inicio]+lista[final]
         if suma==objetivo:
             return True
         if suma < objetivo:
             inicio+=1
         else:
             final-=1
             
             
             
    return False
    
    
    
miList=[1,2,3,6,7,9,4]


print(sumapar(miList,10))
         