def menu():
  
    print('****************************************Elija una Opcion*******')
    print('1)...Factorial')
    print('2)...Decrece')
    print('2)...Es primo')
def bloque():

    if n==1:
        factorial()
    elif n==2:
         Decrece()
    elif n==3:
          es_Primo()
    
    
    
def factorial(n: int):
    if n ==0:
        return 1
    return n* factorial(n-1)
     
def Decrece(n:int):
     if n==0:
         return
     return Decrece(n-1)
  
def es_Primo(n):
    if n<2:
        return False
    for i in range(50):
        if n% i ==0:
             return f' No es primo'
        return f'Es Primo'
def main():
    
    menu()
    n=int(input('Imgrede un numero: '))
    bloque()



if __name__=='__main__':
    main()