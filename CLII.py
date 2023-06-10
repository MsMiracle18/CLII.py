from collections import UserDict
contacts = {}


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter a command."
    return inner


@input_error
def add_contact(contact_info):
    name, phone = contact_info.split()
    contacts[name] = phone
    return "Contact added successfully."


@input_error
def change_phone(contact_info):
    name, phone = contact_info.split()
    contacts[name] = phone
    return "Phone number changed successfully."


@input_error
def get_phone(name):
    return contacts[name]


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self):
        super().__init__()
        self.value = []

    def add_number(self, number):
        self.value.append(number)

    def remove_number(self, number):
        if number in self.value:
            self.value.remove(number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = Phone()

    def add_phone_number(self, number):
        self.phone.add_number(number)

    def remove_phone_number(self, number):
        self.phone.remove_number(number)


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record


def main():
    address_book = AddressBook()

    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            contact_info = input("Enter name and phone number: ")
            name, phone = contact_info.split()
            record = Record(name)
            record.add_phone_number(phone)
            address_book.add_record(record)
            print("Contact added successfully.")
        elif command.startswith("change"):
            name = input("Enter contact name: ")
            if name in address_book.data:
                new_phone = input("Enter new phone number: ")
                record = address_book.data[name]
                record.remove_phone_number(record.phone.value[0])
                record.add_phone_number(new_phone)
                print("Phone number changed successfully.")
            else:
                print("Contact not found.")
        elif command.startswith("phone"):
            name = input("Enter contact name: ")
            if name in address_book.data:
                record = address_book.data[name]
                phone_numbers = ", ".join(record.phone.value)
                print(f"Phone number(s) for {name}: {phone_numbers}")
            else:
                print("Contact not found.")
        elif command == "show all":
            if address_book.data:
                for name, record in address_book.data.items():
                    phone_numbers = ", ".join(record.phone.value)
                    print(f"Name: {name}, Phone number(s): {phone_numbers}")
            else:
                print("No contacts found.")
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
