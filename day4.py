# if and elif ststements in python 
marks = 90
if marks>= 90: # semicolon denotes that any indentation below this "if" is related to this if statement 
    print("grade A") # the space given before print is known as indentation in python we don't need to use braces 
else:
    print(" grade not A")
    print("grade might be B")
    if marks >= 80:
        print("the grade is B")
# Temperature check programme 
temp = input("enter the temp in degree C:")
if temp <= 30:
    print("temp is cold ")
elif temp <= 10:
    print("temp is too cold ")
elif temp <=45:
    print("temp is moderate")
