my_lista=[3,5,7,9,54,1,0,5687,100,21,46,8]

valor_buscado=1000
encontrado=False
for i in my_lista:
    if i == valor_buscado:
            encontrado=True
            break
     
if encontrado:
        print(' El valor  SI se encuentra en la lista')
else:
         print('el valor no se cuenta ')
        