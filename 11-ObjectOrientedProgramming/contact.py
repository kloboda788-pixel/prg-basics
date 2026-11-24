###
# Module with a class describing a single contact
#
class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    # The text representation of a contact - used by print()
    def __str__(self):
        # :<15 and :<20 - columns of a fixed width
        return f'{self.name:<15}{self.email:<20}{self.telephone}'