lista_tareas = []
opt = 0

while opt != 3:
    print(' 1) Para Mostrar Tareas')
    print(' 2) Para Agregar Tareas')
    print(' 3) Salir...')
    opt = int(input('Elige: '))

    if opt == 1:
        if lista_tareas:
            for i,btarea in enumerate(lista_tareas):
                print(f'Tarea: {tarea}')
        else:
            print('No hay tareas en la lista.')
    elif opt == 2:
        tarea = input('Agrega una tarea: ')
        lista_tareas.append(tarea)
    elif opt == 3:
        print('Salir')
        break
    else:
        print('Opción no válida, intenta de nuevo.')