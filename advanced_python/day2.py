# Exception handeling in Python
# importance of exception handling:-
# 1. Prevents program from crashing
# 2. Provides meaningful error messages
# 3. Allows for graceful recovery from errors
# 4. Improves code readability and maintainability 

# Basic try-except block
try: 
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("result:" , x+y)
except ValueError:
    print("Invalid input! Please enter numeric values.")

# 0 division error handling
try:
    a = 10
    b = int(input('enter the divisor:'))
    print('result:', a/b)
except ZeroDivisionError:
    print('Error: Division by zero is not allowed ')

# file not found error handling
try:
    file = open('non_existant_file.txt','r')
    print(file.read())
except FileNotFoundError:
    print('Error: The specified file was not found.') 
# handling multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
except Exception as e : # 'exception' keyword is used when we know error is gonna occur but we don't know what the error is 
    print("some error occurred:", e) 
# using finally block
try:
    file2 = open('example.txt','r')
    content = file2.read()
    print(content) 
finally: # this block will always execute whether exception occurs or not it is used to release external resources like file closing database connections, etc.
    file2.close()