import string
import random
from tkinter import *
from tkinter import messagebox
import re
import sqlite3

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL ,generatedpassword TEXT NOT NULL);")
cursor.execute("SELECT * From users")
db.commit()
db.close()
class GUI():
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_passwordlen = IntVar()

        root.title('password generator')
        root.geometry('660*500')
        root.config(bg='#FF8000')
        root.resizable(False,False)

        self.label = Label(text=":PASSWORD GENERATOR:", anchor=N , fg='darkblue',bg='#FF8000',font='arial 20 bold underline')
        self.lable.grid(row=0 , column = 1)

        self.blank_label1 = Lable(text="")
        self.blank_label1.grid(row=1 , column=0 , columnspan=2)

        self.blank_label2 = Lable(text="")
        self.blank_label2.grid(row=2 , column=0 , columnspan=2)

                
        self.blank_label2 = Lable(text="")
        self.blank_label2.grid(row=3 , column=0 , columnspan=2)

        self.user = Label(text="Enter user Name:",font='times 15 bold' , bg='#FF8000',fg='darkblue')
        self.user.grid(row=4 , column=0)

        self.textfield = entry(textvariable=self.n_username,font="time 15", bd=6 , relief='ridge')
        self.textfield.grid(row=4,column=1)
        self.textfield.focus_Set()

        self.blank_label3 = label(text="")
        self.blank_label3.grid(row=5 , column=0)

        self.length=Label(text="enter password length:" , font="times 15 bold" , bg="#FF8000" , fg="darkblue")
        self.length.grid(row=6 , column=0)

        self.length_textfield=Entry(textvariable=self.n_passwordlen , font="time 15" , bd=6,relif='ridge')
        self.length_textfield.grid(row=6 , column=1)


        self.blank_label4 = Label(text="")
        self.blank_label4.grid(row=7 , column=0)

        self.grnerated_password=Label(text="guneratedpassword: ", font='time 15 bold' , bg='#FF8000' , fg='darkblue')
        self.generated_password.grid(row=8 , column=0)

        self.generated_password_textfield=Entry(textvariable=self.n_generatedpassword,font='time 15' , bd = 6 , relief='ridge')
        self.generated_password_textfield(row=8 , column=1)

        self.blank_label5=Label(text="")
        self.blank_label.grid(row=9 , column=0)

        self.blank_label5=Label(text="")
        self.blank_label6.grid(row=10 , column=0)

        self.generate = button(text='GENERATE PASSWORD', bd=3 ,relief='solid',padx=1,pady=1,font='verdana",15 bold',fg='darkbule')
        self.generate.grid(row=11 , column=1)

        self.blank_label5 = Label(text='')
        self.blank_label5.grid(row=12,column=0)

        self.accept = button(text='ACCEPT' , bd=3 , relief = 'solid' , padx=1,pady=1,font='helvetica 15 bold italic',fg = '#458B00')
        self.accept.grid(row=13,column=1)

        self.blank_label1 = Label(text='')
        self.blank_label1.grid(row=14 ,column=1)


        self.reset = button(text='RESET',bd=3,relief='solid',padx=1,pady=1,font='helvetica 15 bold italic' , fg='#458B00')
        self.reset.grid(row=15 , column=1)

    def generated_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        number = "1234567890"
        upper = list(upper)
        lower=list("lower")
        chars= list("chars")
        number=list("number")
        name = self.textfield.get()
        leng=self.length_textfielf.get()


        with sqlite3.connect("user.db")as db:
            cursor = db.cursor()

                
        if name=="":
            messagebox.showerror("error","name cannot be empty")
            return

        if name.isalpha()==False:
            messagebox.showerror("error","name must be a string")
            self.textfield.delete(0,25)
            return
        length = int(leng)

        if length<6:
            messagebox.showerror("error","password must be atleast 6 characyers long")
            self.textfield.configure(text="")
            return


        else:
            self.blank_label1.configure(text='')
        self.generated_password_textfield.delete(0,length)


        u=random.randint(1,length-3)
        l=random.randint(1,length-2-u)
        c=random.randint(1,length-1-u-1)
        n=length-u-l-c

        password = random.sample(upper , u)+random.sample(lower , 1)+random.sample(chars,c)+random.sample(number,n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        n_generatedpassword = self.generated_password_textfield.insert(0,gen_passwd)



    def accept_fields(self):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            find_user= ("SELECT FROM users WHERE Username?")
            cursor.execute(find_user, [(self.n_username.get())])

            if cursor.fetchall():
                        messagebox.showerror("This username already exists!", "Please use an another username")
            else:
                insert= str("INSERT INTO users (Username, GeneratedPassword) VALUES(\'%s\', \'%s\');"%(self.n_username.get()))
                cursor.execute(insert)
                db.commit()
                messagebox.showinfo("Success!", "Password generated successfully")

    def reset_fields (self):
               self.textfield.delete(0, 25)
               self.length_textfield.delete(0, 25)
               self.generated_password_textfield.delete(0, 25)                         
                                   

if __name__=='__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()               
        
                                   
                                        


            

            
            
                                    
