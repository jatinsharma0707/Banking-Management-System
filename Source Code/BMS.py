
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector as a


conn= a.connect(
    host='localhost',
    user= 'root',
    password= '',
    database= 'bank'
)

class BMS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("BMS")
        self.geometry("730x430")
        self.resizable(0,0)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Fnction, CreateAccount, DepWith, BalEnq, CustDetail, CloseAccount):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def show():
            p = password.get() #get password from entry
            if (p != "jatin"):
                    messagebox.showinfo("warning", "Wrong Password! Try Again...")
                    # print("Wrong Password! Try Again...")
            else:
                controller.show_frame("Fnction")

        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616", height= 800)
        F2.pack(side= TOP, fill=BOTH, ipady='70')
        etp = Label(F2, text= "Enter the password",  bg= "#161616", fg= "white",font="calibri 14 bold",width=30 )
        etp.pack(pady= "80 20", anchor= "center")
        password = StringVar() #Password variable
        passentry = Entry(F2, textvariable=password, bg= "#5e5858", fg= "white", show='*', width=50 ).pack(ipady= 4,pady= "10 30")
        submit = Button(F2, text='Login!',command=show, width=20).pack()

class Fnction(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616", height= 800)
        F2.pack(side= TOP, fill=BOTH, ipady='20')
        Button(F2, text='Create New Account',command=lambda: controller.show_frame("CreateAccount"), bg="#3f3a3a",borderwidth=0,font="calibri 16 bold",  width=40).pack(pady="15 0", expand= True,)
        Button(F2, text='Deposit/Withdraw Amount',command=lambda: controller.show_frame("DepWith"), bg="#3f3a3a", borderwidth=0, font="calibri 16 bold",  width=40).pack(pady="15 0", expand= True)
        Button(F2, text='Balance Enquiry',command=lambda: controller.show_frame("BalEnq"), bg="#3f3a3a", borderwidth=0, font="calibri 16 bold",  width=40).pack(pady="15 0", expand= True)
        Button(F2, text='Customer Details',command=lambda: controller.show_frame("CustDetail"), bg="#3f3a3a", borderwidth=0, font="calibri 16 bold",  width=40).pack(pady="15 0", expand= True)
        Button(F2, text='Close Account',command=lambda: controller.show_frame("CloseAccount"), bg="#3f3a3a", borderwidth=0, font="calibri 16 bold",  width=40).pack(pady="15 0", expand= True)
        Button(F2, text='Logout!',command=lambda: controller.show_frame("StartPage"), bg="#3f3a3a", borderwidth=0, font="calibri 16 bold",  width=40).pack(pady=15, expand= True)


class CreateAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
           # signup database connect
        def action():
            if Name.get() == "" or DoB.get() == "" or Phone.get() == "" or Address.get() == "" or OpenBalance.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=root)

            else:
                try:
                    conn = a.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='bank'
                    )
                    data1 = (Name.get(), DoB.get(), Phone.get(), Address.get(), OpenBalance.get(),)
                    data2 = (Name.get(), OpenBalance.get())
                    sql1 = "insert into savaccount(Name, DoB, Phone, Address, OpenBalance) values(%s,%s,%s,%s,%s)"
                    sql2 = "insert into savamount(Name, Balance) values(%s,%s)"
                    c = conn.cursor()
                    c.execute(sql1, data1)
                    c.execute(sql2, data2)
                    conn.commit()
                    c.execute("SELECT AccountNo FROM bank.savaccount ORDER BY AccountNo DESC LIMIT 1")
                    acn = c.fetchone()
                    messagebox.showinfo("Account No.", acn[0], parent=root)
                    clear()


                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)


        def clear():
            Name.delete(0, END)
            DoB.delete(0, END)
            Phone.delete(0, END)
            Address.delete(0, END)
            OpenBalance.delete(0, END)
        

        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616")
        F2.pack(side= TOP, fill=BOTH, ipady='200')

        # text label
        intro = Label(F2, text="Create New Account", font='Verdana 15 bold underline', bg='#161616', fg='#3dc3e5')
        intro.place(x=240, y=20)
        Name = Label(F2, text="Full Name :", font='Verdana 10 bold', bg='#161616', fg='white')
        Name.place(x=120, y=70)
        DoB = Label(F2, text="Date of Birth :", font='Verdana 10 bold', bg='#161616', fg='white')
        DoB.place(x=120, y=120)
        Phone = Label(F2, text="Phone No :", font='Verdana 10 bold', bg='#161616', fg='white')
        Phone.place(x=120, y=170)
        Address = Label(F2, text="Address :", font='Verdana 10 bold', bg='#161616', fg='white')
        Address.place(x=120, y=220)
        OpenBalance = Label(F2, text="Opening Balance :", font='Verdana 10 bold', bg='#161616', fg='white')
        OpenBalance.place(x=120, y=270)

        # Entry Box ------------------------------------------------------------------
        Name = StringVar()
        DoB = StringVar()
        Phone = IntVar
        Address = StringVar()
        OpenBalance = IntVar

        Name = Entry(F2, width=40, textvariable=Name,)
        Name.place(x=300, y=73)
        DoB = Entry(F2, width=40, textvariable=DoB)
        DoB.place(x=300, y=123)
        Phone = Entry(F2, width=40, textvariable=Phone)
        Phone.place(x=300, y=173)
        Address = Entry(F2, width=40, textvariable=Address)
        Address.place(x=300, y=223)
        OpenBalance = Entry(F2, width=40, textvariable=OpenBalance)
        OpenBalance.place(x=300, y=273)

        # button
        btn_create = Button(F2, text="Create", command= action, width=10, font='Verdana 10 bold', bg='grey')
        btn_create.place(x=200, y=323)
        btn_clear = Button(F2, text = "Clear", command= clear ,width=10,font='Verdana 10 bold' , bg='grey')
        btn_clear.place(x=350, y=323)
        Button(F2, text='Back',command=lambda: controller.show_frame("Fnction"), width=10, bg='grey',font='Verdana 10 bold').pack(side=TOP,padx=5, pady=8, anchor=NE, expand=True)
        

        
class DepWith(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def dep_action():
            if AccountNo.get() == "" or amt.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=root)

            else:
                try:
                    data = (AccountNo.get(),)
                    c = conn.cursor()
                    s = "SELECT AccountNo FROM bank.savamount WHERE AccountNo=%s"
                    c.execute(s, data)
                    row = c.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Account No does not exist!", parent=root)
                    else:
                        a = "select Balance from savamount where AccountNo = %s"
                        c.execute(a, data)
                        result = c.fetchone()
                        totalAmt = result[0] + int(amt.get())
                        sql = "update savamount set Balance = %s where AccountNo = %s"
                        dat = (totalAmt, AccountNo.get())
                        c.execute(sql, dat)
                        conn.commit()
                        messagebox.showinfo("Successfully","Deposit Successfull...", parent=root)
                        clear()


                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)

        def with_action():
            if AccountNo.get() == "" or amt.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=root)

            else:
                try:
                    data = (AccountNo.get(),)
                    c = conn.cursor()
                    s = "SELECT AccountNo FROM bank.savamount WHERE AccountNo=%s"
                    c.execute(s, data)
                    row = c.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Account No does not exist!", parent=root)
                    else:
                        a = "select Balance from savamount where AccountNo = %s"
                        c.execute(a, data)
                        result = c.fetchone()
                        totalAmt = result[0] - int(amt.get())
                        sql = "update savamount set Balance = %s where AccountNo = %s"
                        dat = (totalAmt, AccountNo.get())
                        c.execute(sql, dat)
                        conn.commit()
                        messagebox.showinfo("Successfully","Withdraw Successfull...", parent=root)
                        clear()


                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)


        # clear data function
        def clear():
            AccountNo.delete(0, END)
            amt.delete(0, END)

        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616")
        F2.pack(side= TOP, fill=BOTH, ipady='200')

        # text label
        intro = Label(F2, text="Deposit & Withdraw", font='Verdana 15 bold underline', bg='#161616', fg='#3dc3e5')
        intro.place(x=240, y=20)
        AccountNo = Label(F2, text="Account No :", font='Verdana 10 bold', bg='#161616', fg='white')
        AccountNo.place(x=120, y=100)
        amt = Label(F2, text="Amount :", font='Verdana 10 bold', bg='#161616', fg='white')
        amt.place(x=120, y=150)

        # Entry Box ------------------------------------------------------------------
        AccountNo = StringVar()
        amt = IntVar
        AccountNo = Entry(F2, width=40, textvariable=AccountNo)
        AccountNo.place(x=300, y=103)
        amt = Entry(F2, width=40, textvariable=amt)
        amt.place(x=300, y=153)

        # button
        btn_deposit = Button(F2, text="Deposit", width=10, font='Verdana 10 bold', command=dep_action, bg='grey')
        btn_deposit.place(x=170, y=273)
        btn_withdraw = Button(F2, text="Withdraw", width=10, font='Verdana 10 bold', command=with_action, bg='grey')
        btn_withdraw.place(x=300, y=273)
        btn_clear = Button(F2, text = "Clear",width=10,font='Verdana 10 bold' , command = clear, bg='grey')
        btn_clear.place(x=430, y=273)
        Button(F2, text='Back',command=lambda: controller.show_frame("Fnction"), width=10, bg='grey',font='Verdana 10 bold').pack(side=TOP,padx=5, pady=8, anchor=NE, expand=True)
        
class BalEnq(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def benq():
            if AccountNo.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=root)

            else:
                try:
                    data = (AccountNo.get(),)
                    c = conn.cursor()
                    s = "SELECT AccountNo FROM bank.savamount WHERE AccountNo=%s"
                    c.execute(s, data)
                    row = c.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Account No does not exist!", parent=root)
                    else:
                        a = "select Balance from savamount where AccountNo = %s"
                        c.execute(a, data)
                        result = c.fetchone()
                        res=str(result[0])
                        msg = Message(self, text="Balance of Account no. " + AccountNo.get() + "  is : "+ res, font='Calibri 16 bold',
                                    bg='#161616', fg='yellow', width=1000)
                        msg.place(x=140, y=260)
                        clear()


                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)


        # clear data function
        def clear():
            AccountNo.delete(0, END)

        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616")
        F2.pack(side= TOP, fill=BOTH, ipady='200')

        # text label
        intro = Label(F2, text="Balance Enquiry", font='Verdana 15 bold underline', bg='#161616', fg='#3dc3e5')
        intro.place(x=260, y=20)
        AccountNo = Label(F2, text="Account No :", font='Verdana 10 bold', bg='#161616', fg='white')
        AccountNo.place(x=120, y=100)

        # Entry Box 
        AccountNo = StringVar()
        AccountNo = Entry(F2, width=40, textvariable=AccountNo)
        AccountNo.place(x=300, y=103)

        # button
        btn_submit = Button(F2, text="Submit", width=10, font='Verdana 10 bold', command=benq, bg='grey')
        btn_submit.place(x=170, y=293)
        btn_clear = Button(F2, text = "Clear",width=10,font='Verdana 10 bold' ,  bg='grey')
        btn_clear.place(x=430, y=293)
        Button(F2, text='Back', command=lambda: controller.show_frame("Fnction") , width=10, bg='grey',font='Verdana 10 bold').pack(side=TOP,padx=5, pady=8, anchor=NE, expand=True)


class CustDetail(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def show():
            if AccountNo.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=root)

            else:
                try:
                    data = (AccountNo.get(),)
                    c = conn.cursor()
                    s = "SELECT AccountNo FROM bank.savaccount WHERE AccountNo=%s"
                    c.execute(s, data)
                    row = c.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Account No does not exist!", parent=root)
                    else:
                        sql = "select * from savaccount where AccountNo = %s"
                        c.execute(sql, data)
                        i = 1
                        for customer in c:
                            for j in range(len(customer)):
                                e = Entry(F3 , width=16, text=customer[j], borderwidth=2,relief='ridge')
                                e.grid(row=i, column=j,sticky=EW)
                                e.delete(0, END)
                                e.insert(END, customer[j])
                            i = i + 1
                        clear()


                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)

        def showall():
            try:
                c = conn.cursor()
                c.execute("select * from savaccount")
                i = 1
                for customer in c:
                    for j in range(len(customer)):
                        e = Entry(F3 , width=16, text=customer[j], borderwidth=2,relief='ridge')
                        e.grid(row=i, column=j,sticky=EW)
                        e.delete(0, END)
                        e.insert(END, customer[j])
                    i = i + 1
                clear()


            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)

        # clear data function
        def clear():
            AccountNo.delete(0, END)

        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616")
        F2.pack(side= TOP, fill=BOTH, ipady='200')

        # text label
        intro = Label(F2, text="Customer Details", font='Verdana 15 bold underline', bg='#161616', fg='#3dc3e5')
        intro.place(x=260, y=20)
        AccountNo = Label(F2, text="Account No :", font='Verdana 10 bold', bg='#161616', fg='white')
        AccountNo.place(x=10, y=71)

        # Entry Box 
        AccountNo = StringVar()
        AccountNo = Entry(F2, width=30, textvariable=AccountNo)
        AccountNo.place(x=120, y=74)

        # button
        btn_show = Button(F2, text="Show", width=10, font='Verdana 10 bold', command=show, bg='grey')
        btn_show.place(x=380, y=70)
        btn_showall = Button(F2, text="Show All", width=10, font='Verdana 10 bold', command=showall, bg='grey')
        btn_showall.place(x=500, y=70)
        Button(F2, text='Back', command=lambda: controller.show_frame("Fnction"), width=10, bg='grey',font='Verdana 10 bold').pack(side=TOP,padx=5, pady=8, anchor=NE, expand=True)

        # table frame
        F3 = Frame(F2, borderwidth= 10, bg="black", relief=GROOVE)
        F3.place(y= 120)
        e=Label(F3,width=16,text='Account No.',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0, sticky=EW)
        e=Label(F3,width=16,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1, sticky=EW)
        e=Label(F3,width=16,text='DOB',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2, sticky=EW)
        e=Label(F3,width=16,text='Phone',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3, sticky=EW)
        e=Label(F3,width=16,text='Address',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=4, sticky=EW)
        e=Label(F3,width=16,text='Opening Balance',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=5, sticky=EW)
        
class CloseAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def clsAcc():
            if AccountNo.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=root)

            else:
                try:
                    data = (AccountNo.get(),)
                    c = conn.cursor()
                    s = "SELECT AccountNo FROM bank.savaccount WHERE AccountNo=%s"
                    c.execute(s, data)
                    row = c.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Account No does not exist!", parent=root)
                    else:
                        sql1 = "delete from savaccount where AccountNo = %s"
                        sql2 = "delete from savamount where AccountNo = %s"
                        c.execute(sql1, data)
                        c.execute(sql2, data)
                        conn.commit()
                        messagebox.showinfo("Success!", "Account Close Successfully.", parent=root)
                        clear()


                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)


        # clear data function
        def clear():
            AccountNo.delete(0, END)

        F1 = Frame(self, borderwidth= 10, bg="black", relief=GROOVE)
        F1.pack(side= TOP, fill="x")
        bms = Label(F1, text= "Banking Management System",  bg= "black", fg= "white",font="calibri 26 bold" )
        bms.pack()
        F2 = Frame(self, bg="#161616")
        F2.pack(side= TOP, fill=BOTH, ipady='200')

        # text label
        intro = Label(F2, text="Closing Account", font='Verdana 15 bold underline', bg='#161616', fg='#3dc3e5')
        intro.place(x=260, y=20)
        AccountNo = Label(F2, text="Account No :", font='Verdana 10 bold', bg='#161616', fg='white')
        AccountNo.place(x=120, y=120)

        # Entry Box 
        AccountNo = StringVar()
        AccountNo = Entry(F2, width=40, textvariable=AccountNo)
        AccountNo.place(x=300, y=123)

        # button
        btn_submit = Button(F2, text="Submit", width=10, font='Verdana 10 bold', command=clsAcc, bg='grey')
        btn_submit.place(x=170, y=253)
        btn_clear = Button(F2, text = "Clear",width=10,font='Verdana 10 bold' ,  bg='grey')
        btn_clear.place(x=430, y=253)
        Button(F2, text='Back',command=lambda: controller.show_frame("Fnction") , width=10, bg='grey',font='Verdana 10 bold').pack(side=TOP,padx=5, pady=8, anchor=NE, expand=True)
        

if __name__ == "__main__":
    root = BMS()
    root.mainloop()