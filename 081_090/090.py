class Animal:
    def sound(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def sound(self):
        return ("Woof!")
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())