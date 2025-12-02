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
# creating another object of the class
dog2 = dog("tommy", "pug")
print(dog2.description())
# accessing attributes directly
print(f"dog1 name: {dog1.name}, breed: {dog1.breed}")
# modifying attributes
dog2.name = "max"
print(f"dog2 name: {dog2.name}, breed: {dog2.breed}")
print("---- types of methods -------")

# types of methods in oop 
#  1. instance method: the method that operates on the instance of the class and has access to the instance through the self parameter
class car:
    def __init__(self , brand):
        self.brand = brand 
    def start(self): # instance method
        return f"{self.brand} car is starting"      
c = car("Lamborghini")     
print(c.start())
# 2. class method: the method that operates on the class itself rather than on instances of the class and is defined using the @classmethod decorator and takes cls as the first parameter
class school:
    total_students = 100 # class variable
    @classmethod # decorator for class method
    def show_total_students(cls): # class method
        return f"total students : {cls.total_students}"
print(school.show_total_students())
# 3. static method: the method that does not operate on either the instance or the class and is defined using the @staticmethod decorator and does not take self or cls as the first parameter
class math:
    @staticmethod # decorator for static method
    def add(a,b): # static method
        return a + b
    def mul(a,b): # static method
        return a * b
print(f"addition:{math.add(1,2)}")
print(f"multiplication:{math.mul(3,4)}")
