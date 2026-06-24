import tkinter as tk 
root = tk.Tk()
root.title("login page")
root.geometry("400x300")
# creating a label for username
Username_label = tk.Label(root, text = "Username")
Username_label.grid(row=0, column=0) # here .grid() is used to place the label in the window at the specified row and column
pass_labl = tk.Label(root, text = "Password")
pass_labl.grid(row=1, column=0)
# creating entry for labels
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1)
pass_entry = tk.Entry(root , show="*")
pass_entry.grid(row = 1, column=1)
# creating a button for login
login_btn = tk.Button(root, text = "Login")
login_btn.grid(row = 2 , column=1)
# printing user details
def print_details():
    username = user_entry.get()
    password = pass_entry.get()
    print("username:", username)
    print("password:", password)
# binding the print details to login button
login_btn.config(command = print_details) # here .config() is used to configure the button to call the print_details function when clicked
root.mainloop()