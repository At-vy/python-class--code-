# GUI : it is the graphical user interface through which we can interact with the computer. It is a visual way of interacting with the computer using items such as windows, icons, and menus.
import tkinter as tk
root = tk.Tk() # it is the main window of the application
root.title("My First GUI") # it is the title of the window
root.geometry("400x300") # it is the size of the window
label = tk.Label(root, text = "Hello World!") # it is a label widget that displays text
label.pack() # it is used to display the label in window 
# Adding a button to the GUI
def on_button_click():
    print("Button clicked!")
btn = tk.Button(root, text="Click Me", command=on_button_click) # it is a button widget that can be clicked
btn.pack() # it is used to display the button in window
# taking input from the user
def on_submit():
    ip = entry.get() # .get() is used to get the value from the entry widget
entry = tk.Entry(root)# it is an entry widget that allows the user to enter a single line of text
entry.pack() # it is used to display the entry widget in window
submit_btn = tk.Button(root, text = "Submit", command = on_submit) # it is a button widget that can be clicked to submit the input
submit_btn.pack() # it is used to display the submit button in window
submit_btn.pack() # it is used to display the submit button in window
root.mainloop() # it runs the window untill the user closes it