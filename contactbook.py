contacts = []

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print("Contact added successfully!\n")

# View Contacts
def view_contacts():
    if not contacts:
        print("No contacts found!\n")
        return
    
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

# Search Contact
def search_contact():
    search = input("Enter name or phone to search: ").lower()
    
    found = False
    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            print("\nContact Found:")
            print(contact)
            found = True
    
    if not found:
        print("No contact found!\n")

# Update Contact
def update_contact():
    name = input("Enter name to update: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Enter new details:")
            contact['phone'] = input("New Phone: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")
            print("Contact updated successfully!\n")
            return
    
    print("Contact not found!\n")

# Delete Contact
def delete_contact():
    name = input("Enter name to delete: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    
    print("Contact not found!\n")

# Main Menu
def menu():
    while True:
        print("==== Contact Management System ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

# Run Program
menu()
