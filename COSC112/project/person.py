class Person:
    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.feeling = None
        self.quote = None
        self.link = None
    
    def get_name(self):
        return self.fname + " " + self.lname
    
    def set_feeling(self, feeling):
        self.feeling = feeling


    def set_quote(self, quote):
        self.quote = quote
    
    def set_link(self, link):
        self.link = link