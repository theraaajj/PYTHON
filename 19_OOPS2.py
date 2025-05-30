class Animal:

    def __init__(self, a, b):              # each constructor has a parameter. self points out the current calling object
        self.height=a
        self.weight=b
    def display(self):
        print("Her height is ", self.height, "cms")
        print("Her weight is ", self.weight, "kgs")

    def speak(self):
        print("ha ha ha")

class Dog(Animal):            

    def speak(self):
        print("bhaw bhaw")  

class Panda(Animal):            

    def speak(self):
        print("She sounds like moan moan")  

# Polymorphism : same method defined in each class.


x = input("Is Mitali your friend?\n")
y = input("Do you want to know about her?\n")
c = Panda(166, 63.2)
c.display()
c.speak()