agenda=[]
def agregar():
    nom=input('nomnbre: ')
    num=input('Numero: ')
    contact = {'Nombre': nom, 'Numero': num}
    agenda.append(contact)
    print('contacto añadido..')

def mostrar():
    for  index, contac in enumerate(agenda):
        print(index ,'---', contac)

while True:
    print('1) Agegar')
    print('2) Mostrar')
    print('3) salir')
    opt= input('ingresar datos: ')
    if opt=='1':
        agregar()
    elif opt=='2':
        mostrar()
    elif opt =='3':
        print('saliendo...!')
        break
    else:
         
         print('ingrese una oocion valida ')