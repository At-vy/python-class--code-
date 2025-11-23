from firstmod import * #here the whole module is imported using *
from secondmod import div#only the individual function div is imported
from secondmod import mul
i = float(input("Enter the first number:"))
j = float(input("Enter the second number:"))
opr = input("enter the operation(+,-,*,/):")
if opr == '+':
    print("the sum is :", add(i,j))
elif opr == '-':
    print("the difference is :", sub(i,j))
elif opr == '*':
    print("the product is:", mul(i,j))
elif opr == '/':
    print("the division is:", div(i,j))

