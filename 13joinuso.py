numeros =[1,2,3,5,7]
# usarlo con lista dd numeros
print(''.join([str(n) for n in numeros]))

var=["uno","dos","tres","cuatro"]

print(''.join(var))

def  Emular_join(lista):
    resul=" "
    for n in lista:
         resul+= str(n)
        
    return resul
#numeros=[1,2,3,4,5]     
        
print(Emular_join(numeros)  )