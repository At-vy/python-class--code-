# JSON = it is an open standard format that uses human-readable text to transmit data objects consisting of attribute-value pairs and array data types (or any other serializable value). It is a common data format used for asynchronous browser/server communication, including as a replacement for XML in some AJAX-style systems. 
# basic JSON 
import json
student = [ # creating data in dictionary format
    {"name": "athatva", "marks": 90},
    {"name": "divya", "marks": 80},
    {"name": "amit", "marks": 85}
]
# saving data in JSON format
with open("student.json", "w") as f: # jason.dump is used to write data in JSON format to a file, it takes two arguments: the data to be written and the file object. The indent parameter is optional and is used to specify the number of spaces to use for indentation in the output JSON file, making it more readable.
    json.dump(student, f,indent=4)   # dumping data in JSON format making file clean and readable with indent
# read data from JSON file
print("data saved successfully in JSON format")
with open("student.json", "r") as f:
    data = json.load(f) # loading data from JSON file
    print(data)
print("data loaded successfully from JSON file")
# converting JSON string to Python object
# json_string = '{"name": "athatva", "age": 20, "city": "New York"}'
# python_object = json.loads(json_string) # converting JSON string to Python object
# print(python_object)
# # converting Python object to JSON string
# python_object = {"name": "athatva", "age": 20, "city": "New York"}
# json_string = json.dumps(python_object) # converting Python object to JSON string
# print(json_string)
