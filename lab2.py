def load_address_book(filename="address_book.txt"):
    address_book = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, email = line.strip().split(',')
                address_book[name] = email
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist yet
    return address_book


def save_address_book(address_book, filename="address_book.txt"):
    with open(filename, "w") as file:
        for name, email in address_book.items():
            file.write(f"{name},{email}\n")


def add_contact(address_book):
    name = input("Enter name: ")
    email = input("Enter email: ")
    address_book[name] = email
    print("Contact added successfully!")


def search_contact(address_book):
    name = input("Enter name to search: ")
    email = address_book.get(name)
    if email:
        print(f"Email for {name}: {email}")
    else:
        print(f"Contact for {name} not found.")


def list_contacts(address_book):
    print("Contacts:")
    for name, email in address_book.items():
        print(f"{name} - {email}")


def main():
    address_book = load_address_book()
    while True:
        print("\nAddress Book Program")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. List all contacts")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(address_book)
            save_address_book(address_book)
        elif choice == '2':
            search_contact(address_book)
        elif choice == '3':
            list_contacts(address_book)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()