from tkinter import *
import random as rand
root = Tk()
root.geometry("150x110")
root.minsize(150,110)
root.maxsize(150,110)
root.title("OTP Generator")


def getval():
    f1 = Frame(root)
    val = rand.randint(1111,9999)
    Label(root, text = "Your OTP is:", font = "comicsansms 18 bold").grid(row = 0, column = 0)
    t1 = Label(root, text = val, font = "comicsansms 18 bold", fg = "purple").grid(row = 1, column = 0)



b1 = Button(text = "Generate", command = getval).grid(row = 2, column = 0)

root.mainloop()

