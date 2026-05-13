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
            
        
            if operation == 1:
                add()
contact_book()
    