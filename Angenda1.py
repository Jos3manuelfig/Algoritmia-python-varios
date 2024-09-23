def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Agregar Contacto")
    print("2. Editar Contacto")
    print("3. Eliminar Contacto")
    print("4. Mostrar Contactos")
    print("5. Salir")

def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    agenda.append(contacto)
    print("Contacto agregado exitosamente.")

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            nuevo_nombre = input("Nuevo Nombre: ")
            nuevo_telefono = input("Nuevo Teléfono: ")
            nuevo_email = input("Nuevo Email: ")
            contacto["nombre"] = nuevo_nombre
            contacto["telefono"] = nuevo_telefono
            contacto["email"] = nuevo_email
            print("Contacto editado exitosamente.")
            return
    print("Contacto no encontrado.")

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            print("Contacto eliminado exitosamente.")
            return
    print("Contacto no encontrado.")

def mostrar_contactos(agenda):
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        for i, contacto in enumerate(agenda, start=1):
            print(f"Contacto {i}:")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            print("-------------------------")

def main():
    agenda = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            editar_contacto(agenda)
        elif opcion == "3":
            eliminar_contacto(agenda)
        elif opcion == "4":
            mostrar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda. Hasta luego.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()