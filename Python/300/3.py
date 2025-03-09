class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_data(self):
        return f"Hi {self.name} !, You are {self.age} years old."
    

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

Suresh = Person(name, age)

print(Suresh.display_data())

