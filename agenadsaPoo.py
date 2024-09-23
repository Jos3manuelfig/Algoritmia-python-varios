# Definimos la estructura de un contacto
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Lista para almacenar los contactos
contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    print("Contact added successfully!")

def modify_contact():
    name = input("Enter the name of the contact to modify: ")
    for contact in contacts:
        if contact.name == name:
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")

            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email

            print("Contact modified successfully!")
            return
    print("Contact not found!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def display_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        for contact in contacts:
            print(contact)

def main_menu():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Modify Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            modify_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()