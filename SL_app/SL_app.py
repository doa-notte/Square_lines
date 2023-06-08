from tkinter import *
import os
os.system('clear')

root = Tk()
root.title('Test')
root.geometry("200x200")

myLabel = Label(root, text="Hello World")
myLabel.pack()

root.mainloop()