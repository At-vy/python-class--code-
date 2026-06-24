import tkinter as tk
import time # to get time 
root = tk.Tk()
root.title("time display")
root.geometry("500x500")
canvas = tk.Canvas(root, width=500, height=500 , bg="blue")
label = tk.Label(root, bg="red", fg="black", font=("Arial", 24))
label.pack(padx=20, pady=200, anchor="center")
def update_time():
    current_time = time.strftime("%H:%M:%S") # 24 hrs format
    label.config(text=current_time) # configuring the label to show time 
    root.after(1000, update_time) # schedule the function runs after 1000 ms(1 sec)
update_time() # calling the function to start the time loop 

# canvas.pack()
root.mainloop()

