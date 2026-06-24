# Lamdba function in Python: streamlining code
square = lambda x: x**2
print(square(5)) # 25
# lambda functions are inline functions that are defined using the lambda keyword.
# They can take any number of arguments but can only have a single expression.
# don't use lambda functions for complex operations or multiple statements.
add = lambda a,b : a+b 
print(add(3,4)) #7
greet = lambda : "Hello"
print(greet()) # Hello
# using lambda with filter() function
number = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x : x%2 == 0, number))
print(even) # [2,4,6,8,10]
# using lambda with map() function
# map function applies a given function to all items in an iterable (like list) and returns a map object (which is an iterator).
nums = [1,2,3,4]
squared = list(map(lambda x : x**2 , nums))
print(squared ) # [1,4,9,16]
# taking user input 
n = list(map(int , input("enter the numbers: ") .split())) # here split function splits the input strings int list 
doubled = list(map(lambda x : x*2, n)) 
print(doubled) # prints the doubled values of the input numbers
# using lambda with reduce() function
from functools import reduce 
product = reduce(lambda x,y : x*y , nums)
print(product) # 24 (1*2*3*4)
# using lambda with sorted() function
pair = [(1, 'one'), (2, 'two'), (3,'three'), (4,'four')]
sorted_pair = sorted(pair, key = lambda x : x[1])
print(sorted_pair) # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')](this one is sorted in alpahabetic order based on second element of each tuple)
sorted_pair_num = sorted(pair, key = lambda x: x[0], reverse= True)   
print(sorted_pair_num) # [(4, 'four'), (3, 'three'), (2, 'two'), (1, 'one')] (this one is sorted in descending order based on first element of each tuple)
# multiple arguments in lambda function
grade = lambda marks : 'pass' if marks >= 33 else 'fail'
print(grade(45)) # pass
print(grade(25)) # fail
# nested lambda functions
multiply = lambda a : lambda b : a * b 
print(multiply(3)(4)) # 12