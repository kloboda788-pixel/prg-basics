###
# Class describing an employee with a special text representation
#
class C:
    # data in the given order: name, surname, age, seniority
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    # surname + first letter of the name + seniority;
    # uppercase for adults (18+), lowercase otherwise
    def __str__(self):
        text = f'{self.surname}{self.name[0]}{self.seniority}'
        if self.age >= 18:
            return text.upper()
        return text.lower()

if __name__ == "__main__":
    print(C("Anna", "May", 17, 7))        # maya7
    print(C("George", "Brown", 21, 4))    # BROWNG4