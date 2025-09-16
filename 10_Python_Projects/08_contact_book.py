# contact_book.py

contacts = {}

def show_menu():
    print("\n📒 Contact Book")
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Delete a contact")
    print("4. Search a contact")
    print("5. Exit")

def view_contacts():
    if not contacts:
        print("📭 No contacts yet!")
    else:
        print("\nYour Contacts:")
        for name, phone in contacts.items():
            print(f"👤 {name} : 📞 {phone}")

def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print("⚠️ Contact already exists!")
        return
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"✅ Contact '{name}' added.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"❌ Contact '{name}' deleted.")
    else:
        print("⚠️ Contact not found!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"👤 {name} : 📞 {contacts[name]}")
    else:
        print("⚠️ Contact not found!")

def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    main()
