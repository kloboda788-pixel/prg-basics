###
# Module with a class storing a list of contacts
#
class ContactList:
    def __init__(self):
        # an array of Contact objects
        self.contacts = []

    # 1. Adds a new contact (a Contact object)
    def add_contact(self, contact):
        self.contacts.append(contact)

    # 2. Displays the contact list
    def display(self):
        print('CONTACT LIST')
        print('============')
        for contact in self.contacts:
            # print() uses the __str__ method of the Contact class
            print(contact)