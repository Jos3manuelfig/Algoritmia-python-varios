def comprobar_entero(x,y):
        if isinstance(x, int) and  isinstance(y, int):
    
               return x+y
               
        else:
                raise TypeError('numero invalido') 
try: 
      print(comprobar_entero(3,4))
      print(comprobar_entero('y',4))
      
except TypeError as a:
                print('numeros invalidos')
       
                
            
        
            
        
                                                                     
           