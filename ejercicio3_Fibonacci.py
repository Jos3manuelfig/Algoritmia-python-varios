# escribir los primetos 50 numeros de la serie Fibonacci

anterior=0
siguiente=1

for i in range (1,51):
    '''
    fibo= anterior + siguiente
    anterior=siguiente
    siguiente=fibo
    '''
    anterior,siguiente=siguiente,anterior+ siguiente
    
    
    print(anterior)