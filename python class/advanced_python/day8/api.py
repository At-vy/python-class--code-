# API for fetching weather 
import requests
# step 1:take input from user
city = input("Enter the city name: ")
# step 2: make API call to fetch weather data
url = f"https://wttr.in/{city}?format=j1" # wttr.in is a free weather API that provides weather information in JSON format. The {city} is a placeholder for the city name entered by the user, and the ?format=j1 parameter specifies that we want the response in JSON format.
# step3: send request 
response = requests.get(url) # requests.get() is used to send a GET request to the specified URL and returns a response object.
# step 4: convert JSON -> python object 
data = response.json() 
# step 5 : extract data 
temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
humidity = data["current_condition"][0]["humidity"]
# step 6: print the weather information 
print("\n Weather Report ")
print("city:",city)
print("temperature:",temp,"°C")
print("weather:",weather)                       
print("humidity:",humidity,"%")