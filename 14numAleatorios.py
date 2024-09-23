#from random import randint
import random
num= [random.randint(1,100) for _  in range(100)]
print(num)
print('\n')
print('\n')
def Filtrar_impares(lista):
    impares=[]
    for n in lista:
        if n % 2==1:
            impares.append(n)
           
    return impares
  
print(Filtrar_impares(num))
print('\n')
print('\n')

#aleatorios = filter(lambda n: n%2==1,num)
aleatorios=(Filtrar_impares(num),num)
print(list(aleatorios))

