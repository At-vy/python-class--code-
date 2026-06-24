from tkinter import *
root = Tk()
root.title("testing out canvas widget ")
canvas_width = 800
canvas_height = 800
root.geometry(f"{canvas_width}x{canvas_height}")
canvas = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
canvas.create_rectangle(100,100,700,700, fill="blue") # pass coords Top left - Bottom right 
canvas.create_oval(100,100,700,700, fill="green") # pass coords same as rectangle
line1 = canvas.create_line(100,400,700,400, fill="red", width=5)
line2 = canvas.create_line(400,100,400,700, fill="red", width = 5)
canvas.pack()

root.mainloop()