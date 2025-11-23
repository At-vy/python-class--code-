# functions 
# a greeting function 
def greet(name): 
    return "Hello, " + name + "!"
print(greet("Alice")) # Hello, Alice!
# a function to find lrgest of two numbers 
def largest(a,b):
    if(a>b):
        return a
    else:
        return b
def oddeven(a):
    if(a%2 == 0):
        print("the given number is even")
    else:
        print("the given number is odd")
# function that returns the sum of list of numbers 
def sumofarr( arr: list[int]) -> int:
    return sum(arr)
# a function to calculate factorial of a number
def factorial(n: int) -> int:
    if n < 0:
        print("factorial() not defined for negative values")
        return None
    if n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5)) # 120
        



