# OOP in python - Polymorphism Example
class bird:
    def fly(self):
        return " birds can fly " 
class fish:
    def swim(self):
        return " fish can swim "
    def animal_action(animal):
        print(animal.fly())
        b = bird() 
        f = fish()
    animal_action(b)
    animal_action(f)
    print(b.fly())
    print(f.swim())
    print("This animal can both fly and swim")
    print("This animal can only fly")
    print("This animal can only swim")
    # The function animal_action expects an object with a fly method
    # Passing fish object will raise an AttributeError
    # animal_action(f)  # Uncommenting this line will cause an error
    # The function animal_action expects an object with a fly method
    


    