###
# Class describing a student - with a third attribute
#

# class definition
class Student():
    # __init__ - the constructor: runs automatically when a new object is created
    def __init__(self):
        # self - the object itself; self.name is an attribute of THIS object
        self.name = ""
        self.age = 0
        self.major = ""     # the third attribute (field of study)

def main():
    # object creation based on the class - three separate objects
    student1 = Student()
    student2 = Student()
    student3 = Student()

    # every object has its own copy of the attributes
    student1.name = "Dominic"
    student1.age = 19
    student1.major = "Applied Computer Science"

    student2.name = "Olivia"
    student2.age = 21
    student2.major = "Finance and Accounting"

    student3.name = "Kamil"
    student3.age = 28
    student3.major = "Applied Computer Science"

    print('LIST OF STUDENTS')
    print('================')
    # a list of objects lets us print all students with one loop
    for student in [student1, student2, student3]:
        print(f'{student.name}, {student.age} years old, {student.major}')

if __name__ == "__main__":
    main()