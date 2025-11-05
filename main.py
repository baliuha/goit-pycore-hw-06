from collections import UserDict
from dataclasses import dataclass


@dataclass
class Field:
    value: str


class Name(Field):
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name is required field")
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone: str):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(phone)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_num: str):
        if self.find_phone(phone_num):
            raise ValueError(f"Phone {phone_num} already exists for {self.name.value}")
        self.phones.append(Phone(phone_num))

    def remove_phone(self, phone_num: str):
        phone = self.find_phone(phone_num)
        if phone:
            self.phones.remove(phone)

    def edit_phone(self, old_phone_num: str, new_phone_num: str):
        phone = self.find_phone(old_phone_num)
        if phone:
            phone.value = new_phone_num           

    def find_phone(self, phone_num: str) -> Phone:
        for phone in self.phones:
            if phone.value == phone_num:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]


def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")


if __name__ == "__main__":
    main()
