import json

contact_list = []

def add_contact():
    c_dict = {}
    print("Add a Contact")
    try:
        name = input("Name: ")
        phone = input("Number: ")
        email = input("Email: ")
        if "@" not in email:
            print("invalid email")
        else:
            c_dict["Name"] = name
            c_dict["Phone"] = phone
            c_dict["Email"] = email
            contact_list.append(c_dict)
            save_contacts()
    except ValueError:
        print('Invalid format')
    



def view_contacts():
    for index, contact in enumerate(contact_list):
        print(f"{index + 1} - {contact["Name"]} | {contact["Phone"]} | {contact["Email"]}")
    
def search_contact():
    name = input("Name: ")
    found = False
    for index, contact in enumerate(contact_list):
        if name.lower() == contact['Name'].lower():
            found = True
            print(f"{index + 1} - {contact["Name"]} | {contact["Phone"]} | {contact["Email"]}")
            break
    if not found:
        print("contact not found")

def delete_contact():
    phone = input("Phone: ")
    for contact in contact_list:
        if phone == contact["Phone"]:
            contact_list.remove(contact)
            save_contacts()
            print("Succesfully deleted")
            break
    else:
        print("contact not found")


def update_contact():
    phone = input("Phone: ")
    
    found = False
    for contact in contact_list:
        if phone == contact['Phone']:
            found = True
            try:
                new_name = input("Name: ")
                new_phone = input("Number: ")
                new_email = input("Email: ")
                if "@" not in new_email:
                    print("invalid email")
                else:
                    contact["Name"] = new_name
                    contact["Phone"] = new_phone
                    contact["Email"] = new_email
                    save_contacts()
                    break
            except ValueError:
                print("Invalid Format")
    if not found:
        print("contact not found")




def save_contacts():
    with open("contacts.json", 'w') as f:
        json.dump(contact_list, f)

def load_contacts():
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
    contact_list.extend(contacts)

def main():
    try:
        load_contacts()
    except FileNotFoundError:
        pass

    while True:
        print("\n--- Contacts Menu ---")
        print("1. Add contacts")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Update contacts")
        print("5. Delete contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()    

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()
