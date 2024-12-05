class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)

   
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if 20 < value < 100:
            self._age = value
        else:
            raise ValueError('Age must be between 20 and 100')
