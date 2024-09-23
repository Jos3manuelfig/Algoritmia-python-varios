def conjuntos(bool,array1,array2):
    
    resultado=[]
    if bool:
        for elemento in array1:
            if elemento in array2 and elemento not in resultado:
                resultado.append(elemento)
    else:
         for elemento in array1+array2:
                 if (elemento in array1)!=(elemento in array2) and elemento not in resultado:
                     resultado.append(elemento)
                     
    return resultado
         
arrayA= [1,6,7,9,12,20]
arrayB=[2,3,4,5,6,7,20]

matriz1=(conjuntos(True, arrayA,arrayB))

matriz2=(conjuntos(False, arrayA,arrayB))


print('ArrayA: ', arrayA)
print('ArrayB: ', arrayB)
print(matriz1)
print(matriz2)
                     
                 
        