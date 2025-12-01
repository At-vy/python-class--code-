# basic concepts of oop 
class dog: # a cass is created that acts as a blueprint for objects
    # constructor: a special method that is called when an object is instantiated it is like a welcome function of a class that runs automatically when an object is created
    def __init__(self, name , breed ): # __init__ is a syntax for constructor in python
        self.name = name # attributes
        self.breed = breed
    # method: a function defined inside a class that describes the behavior of the object
    def description(self): # method of the class
            return f"{self.name} is a {self.breed}"
# creating objects of the class
dog1 = dog("pluto", "bulldog") # instantiation of the class
print(dog1.description())

