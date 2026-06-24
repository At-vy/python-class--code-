# Listbox
from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.title("Listbox")
root.geometry("700x800")

# Create a frame to hold the listbox and scrollbar
frame = Frame(root)
frame.pack(anchor=CENTER, fill=BOTH, expand=True)

list = Listbox(frame)
list.insert(1, "Python")
list.insert(2, "Java")
list.insert(3, "C++")
for i in range (4, 100):
    list.insert(END,f"Item {i}")

# Pack the listbox to fill the frame
list.pack(side=LEFT, fill=BOTH, expand=True)

# Adding a scrollbar to the listbox
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the scrollbar and listbox
list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)

root.mainloop()