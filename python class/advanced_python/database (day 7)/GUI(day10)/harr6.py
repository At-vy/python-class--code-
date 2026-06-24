# Menu's and submenu's || Message box
import tkinter as tk
from tkinter import Menu
import tkinter.messagebox as tmsg
root = tk.Tk()
root.geometry("400x400")
root.title("menu and submenu")
def func(): # creating a function for menu
    print ("function called")
def func2():
    value = tmsg.askretrycancel("retry / cancel", "do you want to retry?")
    if value:
        print("Retrying...")
    else:
        print("Cancelled.")
def rate():
    value = tmsg.askquestion("was ur experience good?")
    if value == "yes":
        tmsg.showinfo("feedback", "thanks for ur feedback :)")
    else:
        tmsg.showinfo("feedback", "sorry for ur inconvenience we will try to improve :)")
menubar = Menu(root) # creating a menu 
menubar.add_command(label="Call function", command=func) # adding a command to menu 
menubar.add_command(label="exit", command=quit)
root.config(menu=menubar) # configuring the menu to root(similar to pack or grid)
# adding a drop down menu 
submenu = Menu(menubar, tearoff=0)
submenu.add_command(label="new file", command=func)
submenu.add_command(label="Open file", command=func)
submenu.add_separator() # adding a seperator (border) to the submenu
submenu.add_command(label="Save", command=func)
menubar.add_cascade(label="file", menu=submenu) # adding the submenu to the menubar cascade is used to add the submenu to the menubar

# adding another dorp down menubar for messagebox representation
m2 = Menu(menubar,tearoff=0)
m2.add_command(label = "show info", command= lambda: tmsg.showinfo("this is the info", "this is an info message box"))
m2.add_command(label="rate us", command=rate)
m2.add_command(label="show error", command = lambda:tmsg.showerror("this is an error", "this is an error message box"))
m2.add_command(label="cancel/retry", command=func2)
menubar.add_cascade(label="options", menu=m2)
root.mainloop()