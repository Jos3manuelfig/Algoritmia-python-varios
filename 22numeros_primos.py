def es_primo(n):
     if n< 2:   
           return False         
     for  i in range (2,n):
          if n % i ==0:
              return False
     return True    
  
  
primos=[x for x in range(100) if es_primo(x)]
print(f'numeros Primos: {primos}')
  
     