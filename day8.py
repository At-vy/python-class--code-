# list, tuples and dictionaries in python 
# lists : ordered, mutable collection of items
mylist = [1, 2, 3, 4, 5, "hello"] # list can contain mixed data types
print(mylist)
# operations on list
mylist.append(6) # add item to end of list
print(mylist) # [1, 2, 3, 4, 5, 'hello', 6]
mylist.remove(1) # remove item from list
print(mylist) # [2, 3, 4, 5, 'hello', 6]
print(mylist[3]) # access item at index 3 = 5
mylist[0] = 10 # modify item at index 0
print(mylist) # [10, 3, 4, 5, 'hello', 6]
print(len(mylist)) # length of list = 6
mylist2 = [7,8,"world"]
mylist.extend(mylist2) # extend list by another list
print(mylist)  
mylist.pop() # remove and return last item
print(mylist) 
# tuples : ordered, immutable collection of items
mytuple = (1, 2, 3, 4, 5, "hello")
print(mytuple)
# operations on tuple
# tuples have same operations as list except for modification operations like append, remove, etc.
# dictionaries : unordered, mutable collection of key-value pairs
mydicn = {"name": "atharva", "age": 18, "city": "indore"}
print(mydicn)
# operations on dictionary
print(mydicn["name"]) # access value by key = Alice
