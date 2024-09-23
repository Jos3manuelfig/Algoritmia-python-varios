agenda=[]
class contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
        
    def imprimir(self):
          return f' Nombre: {name} Telefono: {phone} Email: {email}'
          
def agregar_contacto():
         name=input('Ingrese Nombre:')   
         phono=input('Ingrese Telefono: ')
         email= input('Ingrese Correo: ')
         contacto=contact(name,phono,email)  
         agenda.append(contacto)
         
def mostrar_contacto():
    if not agenda:
        print('No hay registros')
    else:     
        for contact in agenda:
            print('*',contact.imprimir())                                      
     
def menu():
    
    while True:
        print('\n1..)Agregar ')
        print('2..)Mostrar')
        print('3..)Eliminar')
        print('4..)Salir')

        opt = input('Seleccione una opción: ')
        if opt =='1':
            agregar_contacto()
        elif opt=='2':  
            mostrar_contacto()
        elif opt=='3':
             pass
        elif opt=='4':
             pass
        elif opt =='5':
             print('\n Gracias...')
             break
        else:
              print('ingrese una opcion valida')
              
       
if __name__=='__main__':
       menu()
       