import random
from tkinter import *


def mans():
    # Letters making for password
    letters_set = 'abcdefghijklmnopqrstuvwxyz'
    letters_rand1 = random.randint(0, 25)

    # Punctuation making for password
    punctuation_set = '!@#$%^&*}[]~`;".,<>|'
    punctuation_rand1 = random.randint(0, 19)

    # Digits making for passsword
    digit_set = '01234567898'
    digit_rand1 = random.randint(0, 9)

    # Password
    password = letters_rand1 + punctuation_rand1 + digit_rand1

    # Main password
    main_pasword = letters_set[random.randint(0, 25)] + letters_set[random.randint(0, 25)] + punctuation_set[
        random.randint(0, 19)] + digit_set[random.randint(0, 9)] + letters_set[letters_rand1] + punctuation_set[
                       random.randint(0, 19)] + digit_set[random.randint(0, 9)] + punctuation_set[punctuation_rand1] + \
                   digit_set[digit_rand1] + letters_set[letters_rand1]

    f1 = Frame(root, bg = "grey", borderwidth = 6, padx = 20)
    f1.grid(row = 1, column = 0)
    Label(root, text = 'Your Strong password is:', font='comicsansms 18 bold').grid(row=0, column=0)
    t1 = Label(f1, text=main_pasword, font='comicsansms 18 bold', fg = "blue").grid(row = 1, column = 0)
    Label(root, text = 'Fact: It will take 100 million years for hackers to crack your password!', font = 'comicsansms 10 bold').grid(row = 4, column = 0)
    Label(root, text = "Don't forget to write it down!", font='comicsansms 18 bold', fg = "red").grid(row = 3, column = 0)


#Creating tkinter window
root = Tk()
root.geometry('470x180')
#root.minsize(470,130)
#root.maxsize(470,130)
root.title("Strong password generator")
root.iconbitmap("C:/Users/admin/Desktop/Files/images/Icons/pass.ico")



Button(root, text = 'Generate', command = mans).grid(row = 2, column = 0)



root.mainloop()



