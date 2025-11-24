# data handeling in python
# two types of data handeling
# 1. text data handeling ex csv , json , xml files, (human redable).
# 2. binary data handeling ex images , audio , video files
# opeaning and reading text files
file = open("example.txt","r") # r is used for read mode
print(file.read()) # reading the file
# closing the file
# file.close()
# rading only first line 
print(file.readline())
# printing lines according to number specified
with open("example.txt","r") as f:
    line = (f.readlines())
    print(line[1]) # prints the second line 
# writing in a text file
with open("example2.txt","w") as w:
    w.write("this is written using write mode \n")
    w.write("this is second line \n")
# appending in a text file i.e. inserting new data without removing the previous one 
with open("example.txt","a") as a:
    a.write("this is an appended line \n")
# addi multiple lines
lines = ["line 1 \n", "line 2\n","line 3\n"]
with open("example2.txt","a") as a:
    a.writelines(lines)
# checking if file exists or not 
import os
if os.path.exists("example3.txt"):
    print("file exists")
else:
    print("file does'nt exists")
# deleting an existing file
import os
if os.path.exists("example3.txt"):
    os.remove("example3.txt")
    print("file deleted")
