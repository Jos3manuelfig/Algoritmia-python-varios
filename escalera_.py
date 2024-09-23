def escalera_sube(n:int):
    print(' ' *10, end=' ')
    print('_')
    for i in range((2*n-2),-1,-2):
        print( ' ' * i, end='')
        print('_|')


def escalera_baja(n:int):

    for i in range(2,- n* 2,2):
        print( ' ' * i, end= '')
        print('|_')
      #  print(' ' * 10, end= '')
      
def main():
    n= int(input('Introduzca un Numero: '))
    if n>0:
        escalera_sube(n)
    elif n<0:
         escalera_baja(n)
    elif n==0:
         print('_____')



if __name__== '__main__':
    main()