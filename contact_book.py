# Python Contact Book
import json
import os

filename = "Projects//contact_info.json"

def load_contacts():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        with open(filename, 'w') as file:
            json.dump([], file)
        print("File created successfully!")
        return []

def view_contacts():
    contacts = load_contacts()
    print("---CONTACTS---")
    
    for i,contact in enumerate(contacts,1):
        print(f"{i}. NAME: {contact['Name']} PHONE: {contact['Phone']} EMAIL: {contact['Email']}")

def add_contacts():
    contacts = load_contacts()
    contact = {
        "Name": input("Enter the name: "),
        "Phone": input("Enter the phone number: "),
        "Email": input("Enter the email id: ")
    }
    contacts.append(contact)

    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
    print("Contact Added Successfully!!!")

def search_contacts():
    contacts = load_contacts()
    found = False
    search = input("Enter the name to look for: ").strip().lower()
    for contact in contacts:
        if contact['Name'].lower() == search:
            found = True

            print("--INFO--")
            
            print(f"{contact['Name']} {contact['Phone']} {contact['Email']}")

    if not found:
        print("Contact Not Found!!")
def delete_contacts():
    contacts = load_contacts()

    deleted = False

    name = input("Enter the name to delete the info: ").strip().lower()

    for i, contact in enumerate(contacts):
        if contact['Name'].lower() == name:
            print("Removed")
            removed = contacts.pop(i)
            print(f"{removed['Name']}: Deleted")
            deleted = True
            with open(filename,'w') as file:
                json.dump(contacts,file,indent=4)
                print("File Updated Successfully!!!")

    if not deleted:
        print("Contact Not Found!!!")

def edit():
    contacts = load_contacts()
    view_contacts()
    print("--EDIT--")
    print("1. Edit Name")
    print("2. Edit Phone")
    print("3. Edit Email")
    ask = int(input("Choose any one of the above options: "))

    def edit_field(field):
        try:
            num = int(input("Enter the SNO: "))
            value = input("Enter the new value: ")
            contacts[num-1][field] = value

            with open(filename,'w') as file:
                json.dump(contacts,file,indent=4)
                print(f"{contacts[num-1][field]}: Changed successfully!")
        except (ValueError, IndexError):
            print("The num value is out of the index's bounds...Please enter a valid number")


    match ask:
        case 1:
            edit_field('Name')
        case 2:
            edit_field('Phone')
        case 3:
            edit_field('Email')
        case _:
            print("Invalid choice...Please try again!")
            

def main():
    is_running = True
    while is_running:

        print("----CONTACT BOOK----")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Edit")
        print("6. Exit")

        choice = int(input("Enter the action you wanna perform: "))
        match(choice):
            case 1:
                view_contacts()
            case 2:
                add_contacts()
            case 3:
                search_contacts()
            case 4:
                delete_contacts()
            case 5:
                edit()
            case 6:
                print("Thank you for using me!!")
                is_running = False
            case _:
                print("Invalid choice. Try again")

main()
