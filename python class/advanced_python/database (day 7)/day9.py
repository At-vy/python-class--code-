# regex functions
import re
# match() - checks for a match only at the beginning of the string
# search() - checks for a match anywhere in the string
# findall() - finds all the matches and returns them as a list
# replace() - replaces the matches with a specified string
# sub() - replaces the matches with a specified string and returns the new string
# example string
text = "The rain in Spain stays mainly in the plain."
# match() example
match  = re.match(r"rain", text)
if match:
    print("Match found:", match.group())
else:    print("No match found")
username = input("Enter a username: ")
pattern = r"^[A-Za-z]" # r = raw string, ^ = start of the string, [A-Za-z] = any letter (uppercase or lowercase)
if re.match(pattern, username):
    print("valid username")
else:
    print("invalid username")
# search() example
if re.search(r"rain",text):
    print("Match found")
else:    
    print("No match found")
# findall() example
matches = re.findall(r"ain", text)
print("All matches:", matches)
# replace() example
new_text = re.sub(r"ain", "XXX", text)
print("Replaced text:", new_text)



