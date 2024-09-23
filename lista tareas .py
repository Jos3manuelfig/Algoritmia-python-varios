tareas = []

while True:
    print("\nMenú de opciones:")
    print("1. Agregar una tarea")
    print("2. Mostrar todas las tareas")
    print("3. Eliminar una tarea")
    print("4. Marcar una tarea como completada")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        nueva_tarea = input("Ingresa la nueva tarea: ")
        tareas.append({'tarea': nueva_tarea, 'completada': False})
        print("Tarea agregada.")
        
    elif opcion == '2':
        if not tareas:
            print("No hay tareas en la lista.")
        else:
            for idx, tarea in enumerate(tareas):
                estado = "Completada" if tarea['completada'] else "Pendiente"
                print(f"{idx}. {tarea['tarea']} - {estado}")
                
    elif opcion == '3':
        indice = int(input("Ingresa el índice de la tarea a eliminar: "))
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            print("Tarea eliminada.")
        else:
            print("Índice no válido.")
            
    elif opcion == '4':
        indice = int(input("Ingresa el índice de la tarea a marcar como completada: "))
        if 0 <= indice < len(tareas):
            tareas[indice]['completada'] = True
            print("Tarea marcada como completada.")
        else:
            print("Índice no válido.")
            
    elif opcion == '5':
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida. Inténtalo de nuevo.")