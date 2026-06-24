# creating a GUI window that can change its color based on user input
import tkinter as tk
from matplotlib.pylab import size

root = tk.Tk()
root.title("customizable window")
# setting a size
root.geometry("500x500")
# setting a bg 
root.config(bg = "white")
# a function to change the color of the window
def change_color(): 
    color = color_entry.get().strip()
    if not color:
        return
    try:
        root.config(bg = color)
    except tk.TclError:
        print(f"the color {color} is not valid please enter a valid color name or hex code")

# craeting a label for coolor input
color_label = tk.Label(root, text = "Enter a color:")
# making a color entry 
color_entry = tk.Entry(root)
# creating color change btn
change_btn = tk.Button(root, text = "change color", command=change_color)
# packing the widgets 
color_label.pack()
color_entry.pack()
change_btn.pack()
# a function to reset size 
def reset_size():
    size = size_entry.get().strip()
    if not size:
        return
    try:
        width, height = map(int, size.lower().split("x"))
        root.geometry(f"{width}x{height}")
    except tk.TclError:
        print(f"the size {size} is not valid please enter a valid size in the format width x height")

# creating a reset label
size_label = tk.Label(root, text="Enter the size(width x height):")
# making a size entry 
size_entry = tk.Entry(root)
# creating a reset btn
size_btn = tk.Button(root, text = "reset size", command=reset_size)
# packing the widgets
size_label.pack()
size_entry.pack()
size_btn.pack()
root.mainloop()