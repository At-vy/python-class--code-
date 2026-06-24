# OOP in python - Polymorphism Example
# Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even though they share the same name.
# it has two types 
# 1. compile time polymorphism (method overloading)
# 2. run time polymorphism (method overriding)
class calclulator: # base class 
    def add( self , a, b = 0, c = 0): # method with three parameters
        return a + b + c
# another method
    def adding(self, *num):
        return sum(num)
c = calclulator()
print("---- compile time polymorphism (method overloading) ----")
print(c.add(2))
print(c.add(2,3))
print(c.add(2,3,4))
print("----------------------- using *args -------------------")
print(c.adding(2))
print(c.adding(2,3))
print(c.adding(2,3,4))
#  run time polymorphism (method overriding)
class animal: # base class 
    def sound(self): # method of base class
        return " animal makes a sound "
class dog(animal): # derived class
    def sound(self): # overriding method of base class
        return "dog barks"
class cat(animal): # derived class
    def sound(self):
        return "cat meows "
a = animal()
d = dog()
c = cat()
print("---- run time polymorphism (method overriding) ----")
print(a.sound())
print(c.sound())
print(d.sound())
#  operator overloading
print("---- operator overloading ----")
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    def __add__(self,other): # overloading + operator
        return point(self.x + other.x , self.y + other.y)
    def __str__(self): # printing object in a readable format
        return f"point({self.x}, {self.y})"
p1 = point(2,3)
p2 = point(4,5)
p3 = p1 + p2 # internally calls p1.__add__(p2)
print(p3) # here + operator is overloaded to add two point objects
# similarly we can overload other operators like -, *, / etc.





    


    