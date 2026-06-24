# GUI using OOP 
from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("777x677")
        self.title("OOP GUI")
    def status(self):
        self.statvar = StringVar()
        self.statvar.set("READY")
        self.sbar = Label(self, textvariable=self.statvar, relief=SUNKEN, anchor=W)
        self.sbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print("Button clicked")
    def create_button(self, inptext):
        Button(self, text=inptext, command= self.click).pack()

if __name__=='__main__':
    window  = GUI()
    window.status()
    window.create_button("Click me")
    window.mainloop()
