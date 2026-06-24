# starrting with Tkinter
from tkinter import *
from PIL import Image, ImageTk
root = Tk() # main window 

# TEXT EDITOR GUI
# root.title("Text Editor")
# root.geometry("400x400")
# F1 = Frame(root,bg = "grey",relief= SUNKEN, borderwidth= 5)
# F1.pack(side = TOP , fill="x")
# f2 = Frame(root, bg = "grey", relief= SUNKEN, borderwidth= 5)
# f2.pack(side = LEFT, fill="y")
# L1 = Label(F1, text="Text Editor", font="sans 15 bold", bg="grey")
# L1.pack(pady= 10)
# L2 = Label(f2, text="file", font = "arial 10 bold", bg="grey")
# L2.pack(pady= 100, padx= 10)

# News paper GUI
root.title("News Paper")
# for jpg images 
image1 = Image.open("news1.jpg")
image1 = ImageTk.PhotoImage(image1)
l1 = Label(root,image= image1)
l1.pack()
root.mainloop() # TO RUN THE APPLICATION