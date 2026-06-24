# creating gui using tkinter functions 
import tkinter as tk
# NOT USING OOP this time 
root = tk.Tk()
root.geometry("500x700")
root.title("Calculator")
scrvar = tk.StringVar()
screen = tk.Entry(root, font = ('arial','15','bold'), bd = 10, textvariable=scrvar, width=42)
screen.grid(row=0, column=0, columnspan=4, pady=20)
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
# button click function 
def button_click(event):
    text = event.widget.cget("text")
    if text == 'C':
        scrvar.set("")
    elif text == '=':
        result = str(eval(scrvar.get()))
        scrvar.set(result)
    else:
        scrvar.set(scrvar.get() + text)
# Creating Buttons (using for loop)
button = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('3',3,0),('2',3,1),('1',3,2),('+',3,3),
            ('.',4,0),('0',4,1),('C',4,2),('=',4,3),
        ]
for(text, row, column) in button:
    btn = tk.Button(button_frame, text=text, width=10, height = 5, command=  button_click)
    btn.grid(row=row, column=column, pady=15, padx = 15, sticky="nsew")



root.mainloop()
