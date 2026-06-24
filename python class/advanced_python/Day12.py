# Matplotlib is a plotting library 
# it is used to create Static, animated, and interactive visualizations in Python.
# It is built on NumPy arrays and designed to work with the broader SciPy stack.
import matplotlib.pyplot as plt 
import numpy as np # it is used for numerical computations in Python, providing support for arrays, matrices, and a wide range of mathematical functions.
# creating data 
# .linspace() is a function that helps to create smoothe curves by generating a specified number of evenly spaced values between a given range.
x = np.linspace(0, 10, 100) # it creates an array of 100 evenly spaced values between 0 and 10
y= np.sin(x) # it computes the sine of each value in the array x
name = ["A","B","C","D"]
value = [10,20,15,25]
# creating a window
plt.figure(figsize=(10,6)) # it creates a new figure or window for plotting
# creating a line plot 
plt.subplot(2,2,1) # (rows , column , position )
plt.plot(x,y) # it creates a line plot of y versus x
plt.title("Sine Wave") # it sets the title of the plot to "Sine Wave"
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid() # it adds a grid to the plot for better visibility

# creating a bar plot
plt.subplot(2,2,2) 
plt.bar(name,value) # it makes a bar plot 
plt.title("Bar plot")
plt.xlabel("Name") 
plt.ylabel("Value")
plt.grid()

# creating a scatter plot
plt.subplot(2,2,3)
plt.scatter(x,y) # it creates a scatter plot of y versus x
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()

# creating a pie chart 
plt.subplot(2,2,4)
plt.pie(value)
plt.title("Pie Chart")

# Display all plots in one window
plt.show()


