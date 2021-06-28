from tkinter import *
import time
import random
root = Tk()
root.geometry("259x150")
root.minsize(259,150)
root.maxsize(259,150)
root.title("Lie detector")


t1 = Label(text = "HitTheButton", font = "comicsansms 30 bold", fg = "yellow").grid(row = 0, column = 0)
def getvals():
    num = random.randint(1,2)
    #t2 = Label(text = "ANALIZING.....", font = "comicsansms 34 bold", fg = "blue").grid(row = 3, column = 0)

    time.sleep(1)
    f1 = Frame(borderwidth = 6, bg = "grey").grid(row = 3, column = 0)

    if(num == 1):
        t3 = Label(f1, text = "TRUTH!!", font = "comicsansms 30 bold", fg = "green").grid(row = 3, column = 0)

    elif(num == 2):
        t4 = Label(f1, text = "LIE!!!", font = "comicsansms 45 bold", fg = "red").grid(row = 3, column = 0)











b1 = Button(text = "Check", command = getvals)
b1.grid(row = 2, column = 0)



mainloop()
