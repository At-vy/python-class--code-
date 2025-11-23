# Strings in python
print("Hello, World!") #'' or "" can only be used for small strings
print("""this is a multi-line string""")
"""
this is a 
multi-line comment
"""
# from  python ver:3 ARE unicode characters 
ord('a') #
print(ord('a')) # 97
print(ord('A')) # 65
# indexing and slicing
s = "Hello, World!"
"""
indexing on s 
H = 0, -13
e = 1, -12
l = 2, -11
l = 3, -10
o = 4, -9
, = 5, -8
' '  = 6, -7
W = 7, -6
o = 8, -5
r = 9, -4 
l = 10, -3 
d = 11, -2 
! = 12, -1  

"""
print(s[-1])
print(s[0]) # H
print(s[7:12]) # World
print(s[-13:-1]) # Hello, World
print(s[:5]) # Hello starts from 0 index and goes up to 5 but not including 5
print(s[7:]) # World! stsarts from 7 index and goes up to end
print(s[0:13:2])# Hlo ol! # step size of 2
print(s[::-1]) # !dlroW ,olleH # reverse string
# functions on string 
print(len(s)) # length of string 13
print(s.lower()) # hello, world!
print(s.upper()) # HELLO, WORLD!
print(s.replace("World", "there")) # Hello, there!
print(s.split(",")) # ['Hello', ' World!']
print(s.find("World")) # 7 , return starting index of substring
# operations on strings
# concatintion : joining strings togther using + operator
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3) # Hello World
# repetition : repeating strings using * operator
s4 = "hello " * 3
print(s4) # hello hello hello
# loopig through string
for i in range(-1, -len(s), -1):
    print (s[i])
# substring check: using in operator
if "World" in s:
    print("Substring found!")

nmae = "Welcome"
print (nmae[-1])