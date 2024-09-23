import random
palabra =['cuenta','telefono']
secreta=random.choice(palabra)
cadena= '_' *len(secreta)
intentos= 0
while True:
    print(cadena)
    letra=input('Escribe una Letra: ')
    if letra in secreta:
            for i in range (len(secreta)):
                if secreta[i]==letra:
                    cadena=cadena[:i]+letra+cadena[i+1:]
    else:
            intentos+=1
            if intentos ==1:
                print('0')
            elif intentos==2:
                print (' 0')
                print ('/')
            elif intentos==3:
                   print (' 0')
                   print ('/|')
            elif intentos==4:
                    print (' 0')
                    print  ('/|\\')
            elif intentos==5:
                  print    (' 0')
                  print   ('/|\\')
                  print   ( '/'   )
            elif intentos==6:
                  print    (' 0')
                  print   ('/|\\')
                  print   ( '/ \\' )
                  print(f'Has perdido, la palabra era: {secreta} ')
                  break 
                  
    if cadena == secreta:
                  print(f'Felicidades, has Ganado la palabra es {secreta}') 
                  break
                  print(' \n ')
                  
                 
                 