import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

#adjust window
root = tk.Tk()
root.geometry("500x500")

#loading the images
img = ImageTk.PhotoImage(Image.open("Images\download.jpg"))
img1 = ImageTk.PhotoImage(Image.open("Images\im.jpg"))
img2 = ImageTk.PhotoImage(Image.open("Images\img.jpg"))
img3 = ImageTk.PhotoImage(Image.open("Images\mb.jpg"))

l = Label()
l.pack()

#using recursion to slide to next image
x = 1

#function to change to next image
def move():
    global x
    if x == 5:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img1)
    elif x == 3:
        l.config(image=img2)
    elif x == 4:
        l.config(image=img3)
    x = x+1
    root.after(2000, move)

# calling the function

move()

root.mainloop()
