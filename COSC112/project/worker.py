from person import Person

class Worker(Person):
    def __init__(self, first_name, last_name, age, company, position):
        super().__init__(first_name, last_name, age)
        self.company = company
        self.position = position
    
    def get_all(self):
        return f"{self.fname} {self.lname} {self.age} {self.company} {self.position}"   