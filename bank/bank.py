from tkinter import *
import tkinter.messagebox as tmsg
import time



def mah_transfers():
    if (mah_transfer_to.get()) == "fardin":

        y = open("mahin.txt")
        mah_balance = y.read()
        mah_balance_int = int(mah_balance)
        y.close()

        mah_how_much_transfer_int = int(mah_how_much_transfer.get())

        if mah_how_much_transfer_int <= mah_balance_int:
            v = open("mahin.txt",'w')
            mah_present = mah_balance_int - mah_how_much_transfer_int
            v.write(f'{mah_present}')
            v.close()

            h = open("fardin.txt")
            far_balance = h.read()
            far_balance_int = int(far_balance)
            h.close()

            s = open('fardin.txt','w')
            far_present = far_balance_int + mah_how_much_transfer_int
            s.write(f'{far_present}')
            s.close()

        elif mah_how_much_transfer_int > mah_balance_int:
            tmsg.showerror('Error', 'Insufficient balance!')

    elif (mah_transfer_to.get()) == "shabbir":
        y = open("mahin.txt")
        mah_balance = y.read()
        mah_balance_int = int(mah_balance)
        y.close()

        mah_how_much_transfer_int = int(mah_how_much_transfer.get())

        if mah_how_much_transfer_int <= mah_balance_int:
            v = open("mahin.txt", 'w')
            mah_present = mah_balance_int - mah_how_much_transfer_int
            v.write(f'{mah_present}')
            v.close()

            h = open("shabbir.txt")
            sha_balance = h.read()
            sha_balance_int = int(sha_balance)
            h.close()

            s = open('shabbir.txt', 'w')
            sha_present = sha_balance_int + mah_how_much_transfer_int
            s.write(f'{sha_present}')
            s.close()

            tmsg.showinfo('Done!', f'Your transfer of {mah_how_much_transfer_int} to shabbir was successful.')

        elif mah_how_much_transfer_int > mah_balance_int:
            tmsg.showerror('Error', 'Insufficient balance!')








    else:
        tmsg.showerror('Invalid username!','Invalid username!')




def sha_transfers():
    if(sha_transfer_to.get()) == "fardin":

        j = open("shabbir.txt")
        sha_balance = j.read()

        sha_balance_int = int(sha_balance)
        j.close()
        sha_how_much_transfer_int = int(sha_how_much_transfer.get())

        if sha_how_much_transfer_int <= sha_balance_int:
            x = open("shabbir.txt",'w')
            sha_present = sha_balance_int - sha_how_much_transfer_int
            x.write(f'{sha_present}')
            x.close()

            w = open("fardin.txt")
            far_balancee = w.read()
            far_balance_int = int(far_balancee)
            w.close()

            d = open('fardin.txt','w')
            far_present = sha_how_much_transfer_int + far_balance_int
            d.write(f'{far_present}')
            d.close()

            tmsg.showinfo('Done!',f'Your transfer of {sha_how_much_transfer_int} to fardin was successful!')

        elif sha_how_much_transfer_int > sha_balance_int:
            tmsg.showerror('Error!','Insufficient balance!')

    elif (sha_transfer_to.get()) == "mahin":
        j = open("shabbir.txt")
        sha_balance = j.read()

        sha_balance_int = int(sha_balance)
        j.close()
        sha_how_much_transfer_int = int(sha_how_much_transfer.get())

        if sha_how_much_transfer_int <= sha_balance_int:
            x = open("shabbir.txt", 'w')
            sha_present = sha_balance_int - sha_how_much_transfer_int
            x.write(f'{sha_present}')
            x.close()

            w = open("mahin.txt")
            mah_balancee = w.read()
            mah_balance_int = int(mah_balancee)
            w.close()

            d = open('mahin.txt', 'w')
            mah_present = sha_how_much_transfer_int + mah_balance_int
            d.write(f'{mah_present}')
            d.close()

            tmsg.showinfo('Done!', f'Your transfer of {sha_how_much_transfer_int} to mahin was successful!')

        elif sha_how_much_transfer_int > sha_balance_int:
            tmsg.showerror('Error!','Insufficient balance!')


    else:
        tmsg.showerror('Invalid username!','Invalid username!')



def far_transfers():
    if (e3.get()) == "shabbir":
        fardin_how_much_transfer_int = int(e4.get())
        far_balance_int = int(far_balance)

        #sha_balance_int = int(sha_bal)
        if fardin_how_much_transfer_int <= far_balance_int:
            g = open("fardin.txt","w")
            far_present = far_balance_int - fardin_how_much_transfer_int
            g.write(f'{far_present}')
            g.close()

            global sha_bal
            q = open("shabbir.txt")
            sha_bal = q.read()
            q.close()

            sha_bal_int = int(sha_bal)

            tmsg.showinfo("Transfer successful",f'Your transfer of {fardin_how_much_transfer_int} to Shabbir was successful')


            sha_present = sha_bal_int + fardin_how_much_transfer_int
            c = open("shabbir.txt", "w")
            c.write(f'{sha_present}')
            c.close()

        elif fardin_how_much_transfer_int > far_balance_int:
            tmsg.showerror('Error!','No sufficient balance in account!')

    elif (e3.get()) == "mahin":
        fardin_how_much_transfer_int = int(e4.get())
        far_balance_int = int(far_balance)

        if fardin_how_much_transfer_int <= far_balance_int:
            g = open("fardin.txt", "w")
            far_present = far_balance_int - fardin_how_much_transfer_int
            g.write(f'{far_present}')
            g.close()

            r = open("mahin.txt")
            mah_balance = r.read()
            mah_balance_int = int(mah_balance)
            r.close()

            mah_present = mah_balance_int + fardin_how_much_transfer_int
            c = open("mahin.txt", "w")
            c.write(f'{mah_present}')
            c.close()

            tmsg.showinfo("Transfer successful",
                          f'Your transfer of {fardin_how_much_transfer_int} to mahin was successful')

        elif fardin_how_much_transfer_int > far_balance_int:
            tmsg.showerror('Error!', 'No sufficient balance in account!')




    else:
        tmsg.showerror('Error!','Invalid Username!')




def myfunc():
    if (name.get() == "fardin") & (password.get() == "Fardin@612**"):
        #far_transfer_to = StringVar()



        root2 = Tk()
        root2.geometry("430x433")
        root2.title("Welcome Fardin")
        Label(root2, text = "Welcome Fardin", font = "comicsansms 20 bold").grid(row = 0, column = 0)


        global far_balance


        f = open("fardin.txt")
        #global far_ball
        far_balance = f.read()
        #far_ball = int(far_bal)

        Label(root2, text = f'Balance: {far_balance}', font = 'comicsansms 18').grid(row = 1, column = 0)
        Label(root2, text = 'Transfer to:', font = 'comicsansms 16').grid(row = 2, column = 0)
        Label(root2, text = 'How much to transfer:', font = 'comicsansms 16').grid(row = 3, column = 0)

        #global far_transfer_to


        far_how_much_transfer = StringVar()
        global e3
        e3 = Entry(root2)
        e3.grid(row = 2, column = 1)

        global e4
        e4 = Entry(root2)
        e4.grid(row = 3, column = 1)

        Button(root2, text = "Transfer", command = far_transfers).grid(row = 4, column = 1)

        root2.mainloop()

    elif (name.get() == 'shabbir') & (password.get() == 'bank'):
        root3 = Tk()
        root3.geometry("430x333")
        root3.title("Welcome Shabbir")
        Label(root3, text="Welcome Shabbir", font="comicsansms 20 bold").grid(row=0, column=0)

        u = open("shabbir.txt")
        shabb_bal = u.read()
        u.close()
        Label(root3, text = f"Balance: {shabb_bal}", font = "comicsansms 18 bold").grid(row = 1, column = 0)

        Label(root3,text = "Transfer to :", font = "comicsansms 16").grid(row = 2, column = 0)
        Label(root3, text = "Amount to transfer :", font = "comicsansms 16").grid(row = 3, column = 0)

        global sha_transfer_to
        sha_transfer_to = Entry(root3)
        sha_transfer_to.grid(row = 2, column = 1)

        global sha_how_much_transfer
        sha_how_much_transfer = Entry(root3)
        sha_how_much_transfer.grid(row=3, column=1)

        Button(root3, text = 'Transfer', command = sha_transfers).grid(row = 4, column = 1)

        #Button(root3, text = 'Log out', command = root3.quit).grid(row = 7, column = 0)

        #sha_tranfer_to = StringVar()
        #Label(root3, text='Transfer to:', font='comicsansms 16').grid(row=2, column=0)
        #e6 =Entry(root2, textvariable= sha_tranfer_to)
        #e6.grid(row = 2, column = 1)

    elif ((name.get()) == "mahin") & ((password.get()) == 'bankline'):
        root5 = Tk()

        root5.geometry("430x333")
        root5.title("Welcome Mahin")
        Label(root5, text="Welcome Mahin", font="comicsansms 20 bold").grid(row=0, column=0)

        o = open("mahin.txt")
        mah_balance = o.read()

        Label(root5, text = f'Balance :{mah_balance}', font = "comicsansms 16 bold").grid(row = 1, column = 0)
        o.close()

        Label(root5, text = 'Transfer to:', font = 'comicsansms 14 bold').grid(row = 2, column = 0)
        Label(root5, text = 'How much to transfer :', font = 'comicsansms 14 bold').grid(row = 3, column = 0)

        global mah_transfer_to
        mah_transfer_to = Entry(root5)
        mah_transfer_to.grid(row = 2, column = 1)

        global mah_how_much_transfer
        mah_how_much_transfer = Entry(root5)
        mah_how_much_transfer.grid(row = 3, column = 1)

        Button(root5, text = 'Transfer', command = mah_transfers).grid(row = 4, column = 1)


        root5.mainloop()





    else:
        Label(text = "Incorrect username or password!", fg = 'red', font = 'comicsansms 15 bold').grid(row = 4, column = 1)

def splash_screen():
    global splash
    splash = Tk()
    splash.geometry('650x320+350+170')
    splash.overrideredirect(True)
    bankimage = PhotoImage(file = 'C:/Users/admin/PycharmProjects/GUI_7/bankimage1.png')
    Label(splash, image = bankimage).place(x = -96, y = -96)
    Label(splash, text = 'Access\nBank', font = 'Elephant  28', fg = 'black').place(x = 500, y = 100)
    splash.update()
    time.sleep(2)
    splash.update()
    Label(text = 'Loading...', font = 'Helvetica 15', fg = 'grey').place(x = 520, y = 200)
    #splash.eval('tk::PlaceWindow . center')
    #  


    splash.after(5000, main)
    splash.mainloop()




def main():
    splash.destroy()
    
    root = Tk()
    root.geometry("430x333+350+170")
    root.title("Bank")
    #root.iconbitmap("bank image.ico")
    global far_transfer_to
    #far_transfer_to = "StringVar()"

    Label(root, text = "Bank login", font = "comicsansms 20 bold").grid(row = 0, column = 0)
    Label(root, text = "Username:", font = 'comicsansms 15').grid(row = 1, column = 0)
    Label(root, text = "Password:", font = 'comicsansms 15').grid(row = 2, column = 0)

    #Entries Vriables
    global name
    global password
    name = StringVar()
    password = StringVar()

    #Entries
    e1 = Entry(root, textvariable = name)
    e1.grid(row = 1, column = 1)

    e2 = Entry(root, textvariable = password, show = '*')
    e2.grid(row = 2, column = 1)


    #Buttons
    b1 = Button(root, text = "Submit", command = myfunc)
    b1.grid(row = 3, column = 1)


    root.mainloop()

if __name__ == "__main__":
    splash_screen()
    
    
    


