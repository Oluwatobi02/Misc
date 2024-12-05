from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, college, major):
        super().__init__(first_name, last_name, age)
        self.college = college
        self.major = major
    
    def get_all(self):
        return f"{self.fname}, {self.lname}, {self.age}, {self.college}, {self.major}"