def contact_book():

    contacts = {}

    print("-------Contact Book App-------")

    total_contacts = int(input("Enter the total number of contacts you want to add: "))
    for i in range(1, total_contacts + 1):
        name = input(f"Enter contact name {i}: ")
        phone = input(f"Enter 10-digit phone number for {name}: ")
        contacts[name] = phone
    print(f"Today's contacts are\n{contacts}")


    while True:
        operation = int(input("Enter 1-Add\n2-search\n3-update\n4-view\n5-delete\n6-Exit/stop/"))

        def add():
            name = input("Enter the contact name you want to add: ")
            phone = input(f"Enter 10-digit phone number for {name}: ")
            contacts[name] = phone
            print(f"Contact {name} has been successfully added...")
            
        def search():
            name = input("Enter the contact name you want to search: ")
            
            if name in contacts:
                print(f"{name}'s phone number is {contacts[name]}")
            else:
                print(f"Contact {name} not found.") 

        def update():
            name = input("Enter the contact name you want to update: ")
            
            if name in contacts:
                new_phone = input(f"Enter the new 10-digit phone number for {name}: ")
                contacts[name] = new_phone
                print(f"Contact {name} has been successfully updated...")
            else:
                print(f"Contact {name} not found.")


        def view():
            print("All contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

        def delete():
            name = input("Enter the contact name you want to delete: ")  
            if name in contacts:
                del contacts[name]
                print(f"Contact {name} has been successfully deleted...")
            else:
                print(f"Contact {name} not found.")

        def exit():
            print("Exiting the contact book app. Goodbye!")
            

        if operation == 1:
            add()

        elif operation == 2:
            search()

        elif operation == 3:
            update()

        elif operation == 4:
            view()

        elif operation == 5:
            delete()

        elif operation == 6:
            exit()
            
        else:
            print("Invalid operation. Please enter a number between 1 and 6.")
            break

contact_book()
    