def agregar_contactos(agenda):
    nom = input('nombre: ')
    telf = input('telefono: ')
    contac = {'nombre': nom, 'telefono': telf}
    agenda.append(contac)  # Corregido de 'contact' a 'contac'
    print('Contacto añadido..!')

def mostrar_contactos(agenda):
    for index, conta in enumerate(agenda):
        print(index, '...', conta)

def eliminar_contacto(agenda):
    nom = input('nombre: ')
    for contac in agenda:
        if contac['nombre'] == nom:
            agenda.remove(contac)
            print('Registro eliminado')
            return  # Salimos después de encontrar y eliminar el contacto
    print('Registro no encontrado')  # Solo se ejecuta si no se encuentra el contacto

def mostrar_menu(agenda):
    while True:
        print('\n1..)Agregar ')
        print('2..)Mostrar')
        print('3..)Eliminar')
        print('4..)Salir')

        opt = int(input('Seleccione una opción: '))  # Convertir input a entero
        if opt == 1:
            agregar_contactos(agenda)  # Pasar 'agenda' como parámetro
        elif opt == 2:
            mostrar_contactos(agenda)  # Pasar 'agenda' como parámetro
        elif opt == 3:
            eliminar_contacto(agenda)  # Pasar 'agenda' como parámetro
        elif opt == 4:
            print('\nGracias...')
            break
        else:
            print('Opción inválida')

def main():
    agenda = []
    mostrar_menu(agenda)

if __name__ == '__main__':
    main()