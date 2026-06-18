class ContactManager:

    def __init__(self):
        self.contacts = []

    def validate_phone(self, phone):
        allowed = "+-0123456789"

        for char in phone:
            if char not in allowed:
                return False

        clean_phone = phone.replace("-", "")

        if len(clean_phone) == 10 and clean_phone.isdigit():
            return True

        if (
        len(clean_phone) == 13
        and clean_phone.startswith("+")
        and clean_phone[1:].isdigit()
        ):
            return True

        return False

    def validate_email(self, email):

        if email == "":
            return True

        return "@" in email and "." in email


    def add_contact(self, name, phone, email=""):

        if not self.validate_phone(phone):
            print("Error: Invalid phone number.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        self.contacts.append(contact)

        print("Contact added successfully.")

    def list_contacts(self):

        if not self.contacts:
            print("No contacts available.")
            return

        print("\n===== CONTACT LIST =====")

        for index, contact in enumerate (self.contacts, start=1):  #Enumerate () adds counter while looping.

            print(f"\nContact {index}")
            print("-------------------")
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

    def update_contact(self, name, new_phone, new_email):

        if not self.validate_phone(new_phone):
            print("Error: Invalid phone number.")
            return

        if not self.validate_email(new_email):
            print("Error: Invalid email address.")
            return

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():

                contact["phone"] = new_phone
                contact["email"] = new_email

                print("Contact updated successfully.")
                return

        print("Contact not found.")

    def delete_contact(self, name):

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():

                self.contacts.remove(contact)

                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    def search_contacts(self, keyword):

        results = []

        for contact in self.contacts:

            if (
                keyword.lower() in contact["name"].lower()
                or keyword in contact["phone"]
                or keyword.lower() in contact["email"].lower()
            ):
                results.append(contact)

        if not results:
            print("No matching contacts found.")
            return

        print("\n===== SEARCH RESULTS =====")

        for contact in results:

            print("-------------------")
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

    def view_contact(self):

        self.list_contacts()




def main():

    manager = ContactManager()

    while True:

        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":

            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            manager.add_contact(name, phone, email)

        elif choice == "2":

            manager.view_contact()

        elif choice == "3":

            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            manager.update_contact(name, phone, email)

        elif choice == "4":

            name = input("Enter contact name to delete: ")

            manager.delete_contact(name)

        elif choice == "5":

            keyword = input("Enter name, phone, or email to search: ")

            manager.search_contacts(keyword)

        elif choice == "6":

            manager.list_contacts()

        elif choice == "7":

            print("Exiting Contact Manager...")
            break

        else:

            print("Invalid option. Please choose between 1 and 7.")
