# Sliders 
from tkinter import *
import tkinter.messagebox as msg

# taking the user entered value from silder into a file 
def submit():
        with open("slider.txt", "w") as f:
                f.write(f"User experience rating is {slider.get()}")
root = Tk()
root.title("Sliders")
root.geometry("1000x1000")
label = Label(root, text="Rate your experience").pack()
slider = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=5)
slider.pack()
# initialising the slider with a value
slider.set(5)
btn = Button(root, text = "Submit", command=submit)
btn.pack()
# Using radio buttons 
var = IntVar()
def Order():
    msg.showinfo("Order", f"Your order of {var.get()} is placed")
        
ask = Label(root, text="What will U like to Eat ?").pack()
radio = Radiobutton(root, text="Pizza", variable=var, value=1, command=Order).pack()
radio = Radiobutton(root, text="burger", variable=var, value=2, command=Order).pack()
radio = Radiobutton(root, text="fries", variable=var, value=3, command=Order).pack()
radio = Radiobutton(root, text="ice cream", variable=var, value=4,    command=Order).pack()
root.mainloop()