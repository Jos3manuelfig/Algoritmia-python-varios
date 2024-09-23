agenda = []

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def imprimir(self):
        return f'Nombre: {self.name} Telefono: {self.phone} Email: {self.email}'
          
def agregar_contacto():
    name = input('Ingrese Nombre:')   
    phone = input('Ingrese Telefono: ')
    email = input('Ingrese Correo: ')
    contacto = Contact(name, phone, email)  
    agenda.append(contacto)
         
def mostrar_contacto():
    if not agenda:
        print('No hay registros')
    else:     
        for contacto in agenda:
            print('*', contacto.imprimir())
            
            
def eliminar_contacto():
           name = input('Ingrese Nombre:')
           for contac in agenda:
                 if contac.name==name:
                    agenda.remove(contac)
                    print('Eliminado')
                 else:
                    print('Registro Eliminado')
                
def editar_contacto():
    pass                      
def menu():
    while True:
        print('\n1..)Agregar ')
        print('2..)Mostrar')
        print('3..)Eliminar')
        print('4..) Editar')
        print('5..)Salir')

        opt = input('Seleccione una opción: ')
        if opt == '1':
            agregar_contacto()
        elif opt == '2':  
            mostrar_contacto()
        elif opt == '3':
            eliminar_contacto()
        elif opt == '4':
            editar_contacto()   
        elif opt == '5':
            print('\n Gracias...')
            break
        else:
            print('Ingrese una opción válida')
              
if __name__ == '__main__':
    menu()