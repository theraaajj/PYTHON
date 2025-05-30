class Animal:

    def __init__(self, a, b):              # each constructor has a parameter. self points out the current calling object
        self.height=a
        self.weight=b
    def display(self):
        print(self.height, self.weight)

class Dog(Animal):              # Inheritance : dog is the subclass, and animal the superclass

    def speak(self):
        print("bhaw bhaw")    
 
d = Dog(1, 50)
d.display()
d.speak()

hog = Animal(2, 100)
hog.display()
# print(dog.height, dog.weight)

cat = Animal(0.5, 50)
cat.display()
# print(cat.height, cat.weight)