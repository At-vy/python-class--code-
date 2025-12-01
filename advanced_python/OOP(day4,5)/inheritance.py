# OOP in python - Inheritance Example

class Animal: #parent class
    def __init__(self,name):
        self.name  = name
    def speak(self):
        pass
class dog(Animal): #child class
    def speak(self):
        return f"{self.name} Barks"
class cat(Animal): #child class 
    def speeak(self):
        return f"{self.name} meows"
# creating objects of child classes
d = dog("pluto")
print(d.speak())
c = cat("Tom")
print(c.speeak())
