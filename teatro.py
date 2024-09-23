
filas=10
asientos=10
mapa=[['L' for _ in range(filas)] for _ in range(asientos)]
def mostrar_asientos():
    for i in range(filas):
        print('')
        for j in range(asientos):
            print(mapa[i][j] ,end=' ')
    
           
             
              
print('\n')
print('seleccione su numeronde fila y su nimero de adiento...!')
while True:
    mostrar_asientos()
    print('\n')
    fila= int(input('seleccione una fila: '))
    silla= int(input('seleccione un aisento: '))
    if mapa[fila][silla]=='L':
        mapa[fila][silla]='X'
        print('Reservado Satisfactorismente')
    else:
        print('Lonsiento ')
        
    info=input('Desea Finalizar su Reseevacion')
    if info =='s':
         break 
     
