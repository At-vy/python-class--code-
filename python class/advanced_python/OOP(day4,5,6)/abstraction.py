# object oriented programming - Abstraction Example
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.
from abc import ABC , abstractmethod # importing abstract base class module in form of ABC and abstractmethod
class shape(ABC): # creating an abstract class by inheriting ABC
    @abstractmethod #decorator of abstract method i.e. a method without implementation
    def area(self): # abstract method
        pass
class circle(shape ): # concrete class inheriting abstract class
    def __init__(self, radius):
        self .radius = radius
    def area(self): # implementing abstract method
        return 3.14 * self.radius * self.radius
class square(shape): # concrete class inheriting abstract class
    def __init__(self, side):
        self.side = side
    def area(self): # implementing abstract method
        return self.side ** 2
# creating objects of concrete classes
c = circle(5)
s = square(5)
print(f"arae of circle is :" ,c.area())
print(f"arae of square is :" ,s.area())

# trying to create object of abstract class will raise an error
# sh = shape()  
# The above line will raise TypeError: Can't instantiate abstract class shape with abstract methods area i.e. abstract classes cannot be instantiated directly

