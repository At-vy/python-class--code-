# loops in python 
# here the loop will automatically iterate from 0 to n - 1,(5-1)
for i in range(5):
    print(i)
# her we can specify a custom startimg poin the end poin will always be n - 1, which in this case is n= 10 , n-1 = 9 
for j in range(2,10): # here the loop will iterate from 2 to 9
    print(j)
# we can also specify a custom step value
for k in range(1,20,3): # here the loop will iterate from 1 to 19 with a step value of 3
    print(k)
print("**********while loop***********")
# while loop in python
count = 0
while count < 5:
    print("the count is " + str(count))
    count += 1 # incrementing the count value by 1
print("**********while loop with len function***********")
# while loop with len function in python
fruits = "apple"
length = len(fruits) # len function returns the length of the string
index = 0
while index < length:
    print("the character at index " + str(index) + " is " + fruits[index])
    index += 1
print("**********controlling statements***********")
# controlling statements in a loop in python
# break statement
for a in range(10):
    if a == 5:
        break # when the value of a becomes 5 the loop will terminate 
    print("THE VALUE IS " + str(a))
# continue statement
for b in range(10):
    if b == 5:
        continue # when the value of b becomes 5 the loop will skip the current iteration and move to the next iteration
    print("THE VALUE IS " + str(b))
# pass statement
for c in range(10):
    if c == 5:
        pass # when the value of c becomes 5 the loop will do nothing and move to the next iteration
    print("THE VALUE IS " + str(c))
