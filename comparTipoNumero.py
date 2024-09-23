def comprobador(num):
    
    try:
            int(num)
            return True
             
        
    except ValueError:
            return False
            
num= input('introduzca un numero: ')
            
if comprobador(num):
    print('Datos Validos')
else:
     print('El tipo dato es invalido ')