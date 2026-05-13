def contact_book():

    contacts = {}

    print("-------Contact Book App-------")

    total_contacts = int(input("Enter the total number of contacts you want to add: "))
    for i in range(1, total_contacts + 1):
        name = input(f"Enter contact name {i}: ")
        phone = input(f"Enter 10-digit phone number for {name}: ")
        contacts[name] = phone
    print(f"Today's contacts are\n{contacts}")

contact_book()
    