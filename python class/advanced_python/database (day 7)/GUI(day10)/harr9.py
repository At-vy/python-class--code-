# status bar 
from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Learning Tkinter")
# function to upadte the status bar
def update():
    statvar.set("updating....")
    sbar.update()
    import time
    time.sleep(5) # this will freeze the window for 5 seconds , Use of .after() is more preferred  
    statvar.set("Updated")
# setting a variable for ststus bar 
statvar = StringVar()
statvar.set("ready")
# status bar cannot be created directly so we use label and border to create it 
sbar = Label(root, textvariable=statvar, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)
# adding a button to change status bar
btn = Button(root, text= "Update", command=update, bg="red", fg="white")
btn.pack(pady=20)

root.mainloop()