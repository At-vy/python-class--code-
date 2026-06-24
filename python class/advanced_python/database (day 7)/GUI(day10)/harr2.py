# newspaper GUI 
import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("500x500")
root.title("News Paper")
# for png images 
image1= Image.open(r'C:\Users\vyasa\OneDrive\Desktop\python class\advanced_python\database (day 7)\GUI(day10)\news 1.png')
image1 = ImageTk.PhotoImage(image1)
l1 = tk.Label(root, image=image1)
l1.pack(side = tk.LEFT)
# for jpg images 
image2 = Image.open(r'C:\Users\vyasa\OneDrive\Desktop\python class\advanced_python\database (day 7)\GUI(day10)\news 2.jpg')
image2 = ImageTk.PhotoImage(image2)
l2 = tk.Label(root, image = image2)
l2.pack(side = tk.RIGHT)
root.mainloop()