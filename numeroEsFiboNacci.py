def es_fibonacci(n):
    a,b=0,1
    while b<=n:
        if b==n:
            return True
        a,b=b,a+b
    return 
    
    
def main():
       try:
            numero=int(input('introdusza un numero: ')) 
            if numero<0:
                print('ingrese un numero positivo')
            else:
                    resul=(es_fibonacci(numero))
            if resul:
                print(f' Numero {numero}, si Pertenece a la Secuencia Fibonacci')
            else:
                 print(f' Numero {numero}, No es  Fibonacci')
            
                
       except ValueError:
            print('se espera un numrro valido')
            
            
if __name__ =='__main__':
    main()