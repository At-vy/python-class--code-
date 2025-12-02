# Object Oriented Programming (OOP) Concepts in Python
# creating a class 
class student:
    # constructor
    def __init__(self, name, age, course):
        self.age = age
        self.course = course
        self.name = name
    # method to display student details
    def display(self):
        print(f"name: {self.name}, age: {self.age}, course: {self.course}")
    # using encapsulation to set marks 
    def set_marks(self,m):
        self.__marks = m # private attribute
        if m < 0 or m > 100:
            print("invalid marks!")
    # method to get marks
    def get_marks(self):
        return self.__marks
# creating objects of the class
s1 = student("Atharva", 18, "B.tech")
s1.display()
s1.set_marks(81)
print(f"marks: {s1.get_marks()}")
