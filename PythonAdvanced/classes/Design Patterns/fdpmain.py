from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method"""
        
class Student(IPerson):

    def __init__(self):
        self.name = "this is student"

    def person_method(self):
        return "i am a student method"

class Teacher:
    def __init__(self):
        self.name = "This is a teacher"

    def person_method(self):
        return "This is the teacher method" 


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("INvalid Type")
        return -1

if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    print(person.person_method())