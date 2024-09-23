from random import randint

numeros=[randint(1,100)  for _ in range(100)]
print(numeros)
print('\n')

def Numeros_pares(lista):
    pares=[]
    for n in lista:
        if n %2==0:
           pares.append(n)
           
    return pares
           
print(Numeros_pares(numeros))                  
                     
         