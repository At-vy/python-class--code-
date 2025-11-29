# Modules and Packages in Python
# Modules: A module is a file containing Python code that defines functions, classes, and variables. It allows for code organization and reuse.
# Packages: A package is a collection of related modules organized in a directory hierarchy. It allows for better organization of large codebases.
# Importance of modules and packages:-
# 1. Code Reusability: Modules allow you to reuse code across multiple programs.
# 2. Organization: Packages help in organizing related modules together, making it easier to manage large codebases.
# 3. Namespace Management: Modules and packages provide separate namespaces, preventing naming conflicts.
# inbuilt modules
# math, random, datetime, os, sys, json, re, etc.
import math , random, datetime,pytz ,os, sys, json, re
# using math module
n = int(input("enter the value"))
print("Math Module:")
print("square root of 16 is:", math.sqrt(n))
print("value of pi is:", math.pi)
# using random module
print("\nRandom Module:")
print("random no between 1-100:", random.randint(1,100))
# using datetime module
tz = pytz.timezone('asia/kolkata')
print("\ndatetime module:", datetime.datetime.now(tz))
# using packages
from packages import *
print("\nUsing Packages:")
a = int(input("enter the num:"))
b = int(input("enter the num:"))
print("addition of two numbers:", add(a,b))
print("reverse of a string : ", reverse_string("hello"))
