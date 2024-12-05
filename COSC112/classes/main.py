from person import Person

class Teacher(Person):
    def __init__(self, name, age, location):
        super().__init__(name, age)
        self.locaaion = location

    def display(self):
        super().display()
        print(self.locaaion)
    
t = Teacher('Kanye', 30, 'New York')
t.display()
t.display()