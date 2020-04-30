from tkinter import *
from tkinter import messagebox
import random
import os

def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

def randgen():
    pas=''
    for i in range(16):
        pas+=chr(random.randint(33,122))
    
    addToClipBoard(pas)
    return pas


def clicked():
    password = randgen()
    lbl.configure(text=password)
    messagebox.showinfo("Info.","Password Copied to Clipboard!")  

window = Tk()
window.title("16Dgt Random Pass Gen - Lite")
window.geometry('350x50')

lbl = Label(window, text="NaN",fg="green")
lbl.pack()

btn = Button(window, text='Generate!', width=25, command=clicked)
btn.pack()

window.mainloop()