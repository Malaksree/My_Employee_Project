#Employee Management System
from functools import partial
from tkinter import *

from tkinter import messagebox
import pymysql
import framestyle as cs
import dbconnection as cr
#create class 
class Employee:
     def __init__(self, root):
        self.window = root
        self.window.title("Employee Management System")
        #self.window.maxsize(width=940 ,  height=680)
        #self.window.minsize(width=940 ,  height=680)
        self.window.geometry("1199x750")
        self.window.config(bg = "white")
        # Customization
        self.color1 = cs.color1
        self.color2 = cs.color2
        self.color3 = cs.color3
        self.color4 = cs.color4
        self.color5=cs.color5
        self.font1 = cs.font1
        self.font2 = cs.font2
        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color1, border=2,borderwidth=10)
        self.frame_1.place(x=0, y=0, width=230,height = 900)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color2)
        self.frame_2.place(x=230,y=0,width=1500, height=1000)
        self.title=Label(self.frame_2, text="Welcome TO All", font=(self.font2, 35, "bold"), bg=self.color2,fg=self.color3).place(x=350,y=100)
        # Buttons
        self.add = Button(self.frame_1, text='SIGN UP', font=(self.font1, 12), bd=2, command=self.sign,cursor="hand2",
                      bg=self.color5,fg=self.color3).place(x=68,y=40,width=90)
        self.view = Button(self.frame_1, text='LOG IN', font=(self.font1, 12), bd=2, cursor="hand2",command=self.login, bg=self.color5,fg=self.color3).place(x=68,y=120,width=90)
        self.update = Button(self.frame_1, text='UPDATE', font=(self.font1, 12), bd=2,cursor="hand2",command=self.Contact_Update,
                      bg=self.color5,fg=self.color3).place(x=68,y=200,width=90)
        self.delete = Button(self.frame_1, text='DELETE', font=(self.font1, 12), bd=2,cursor="hand2",command=self.Contact_Delete,
                      bg=self.color5,fg=self.color3).place(x=68,y=280,width=90)
        self.clear = Button(self.frame_1, text='CLEAR', font=(self.font1, 12), bd=2,cursor="hand2",command=self.ClearScreen,
                      bg=self.color5,fg=self.color3).place(x=68,y=360,width=90)
        self.exit = Button(self.frame_1, text='EXIT', font=(self.font1, 12), bd=2,cursor="hand2", bg=self.color5,command=self.Exit,
                      fg=self.color3).place(x=68,y=440,width=90)
     def sign(self):
        self.ClearScreen()
        self.name = Label(self.frame_2, text="Employee Details", font=(self.font2, 15, "bold"), bg=self.color2).place(x=350,y=10)
        self.name = Label(self.frame_2, text="Enter Your Name", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=50)
        self.name_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.name_entry.place(x=400,y=50, width=350,height=30)
        self.title = Label(self.frame_2, text="Employee Title", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=100)
        self.title_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.title_entry.place(x=400,y=100, width=350,height=30)
        self.gender_entry=StringVar()
        self.gender = Label(self.frame_2, text="Gender", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=150)
        self.gender1 = Radiobutton(text="Male",bg=self.color2,fg=self.color3,font=(self.font2,15,"bold"),value="Male",variable=self.gender_entry)
        self.gender2 = Radiobutton(text="Female",bg=self.color2,fg=self.color3,font=(self.font2,15,"bold"),value="Female",variable=self.gender_entry)
        self.gender1.place(x=650,y=150)
        self.gender1.select()
        self.gender2.place(x=800,y=150)
        self.gender2.deselect()
        self.dob = Label(self.frame_2, text="Date of Birth", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=200)
        self.dob_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.dob_entry.place(x=400,y=200, width=350,height=30)
        self.doj = Label(self.frame_2, text="Date of Joining", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=250)
        self.doj_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.doj_entry.place(x=400,y=250, width=350,height=30)
        self.mailid = Label(self.frame_2, text="Email Id", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=300)
        self.mailid_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.mailid_entry.place(x=400,y=300, width=350,height=30)
        self.phone = Label(self.frame_2, text="Mobile Number", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=350)
        self.phone_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.phone_entry.place(x=400,y=350, width=350,height=30)
        self.aadhar = Label(self.frame_2, text="Aadhar Number", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=400)
        self.aadhar_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.aadhar_entry.place(x=400,y=400, width=350,height=30)
        self.city = Label(self.frame_2, text="City", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=450)
        self.city_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.city_entry.place(x=400,y=450, width=350,height=30)
        self.pin = Label(self.frame_2, text="Pin", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=500)
        self.pin_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.pin_entry.place(x=400,y=500, width=350,height=30)
        self.address = Label(self.frame_2, text="Address", font=(self.font2, 15, "bold"), bg=self.color2).place(x=100,y=550)
        self.address_entry = Entry(self.frame_2, bg=self.color4, fg=self.color3,font=(self.font2,15))
        self.address_entry.place(x=400,y=550, width=350,height=100)
        self.submit = Button(self.frame_2, text='Submit', font=(self.font1, 12,"bold"), bd=3, command=self.addinform,cursor="hand2",
                      bg=self.color5,fg=self.color3,).place(x=530,y=660,width=100)
       

     def ClearScreen(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()

     
     def addinform(self):
        if (self.name_entry.get() == "" or self.title_entry.get() == "" or self.dob_entry.get() == "" or self.doj_entry.get() == "" or 
        self.mailid_entry.get() == "" or self.phone_entry.get() == "" or self.aadhar_entry.get() == "" or self.city_entry.get() == "" or self.pin_entry.get() == "" 
        or self.address_entry.get() == "" or self.gender_entry.get()==""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from employee where phone=%s", self.phone_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The contact number is already exists, please try again with another number",parent=self.window)
                else:
                    curs.execute("insert into employee(name,title,gender,dob,doj,mailid,phone,aadhar,city,pin,address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.name_entry.get(),
                                            self.title_entry.get(),
                                            self.gender_entry.get(),
                                            self.dob_entry.get(),
                                            self.doj_entry.get(),
                                            self.mailid_entry.get(),
                                            self.phone_entry.get(),
                                            self.aadhar_entry.get(),
                                            self.city_entry.get(),
                                            self.pin_entry.get(),
                                            self.address_entry.get(),
                                                                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
     def reset_fields(self):
        self.name_entry.delete(0, END)
        self.title_entry.delete(0, END)
        self.dob_entry.delete(0, END)
        self.doj_entry.delete(0, END)
        self.mailid_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.aadhar_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.pin_entry.delete(0, END)
        self.address_entry.delete(0, END)
     
     def login(self):
        self.ClearScreen()
        self.username = Label(self.frame_2, text="Login Here", font=(self.font1, 20, "bold"), bg=self.color2).place(x=320,y=100)

        self.username = Label(self.frame_2, text="Enter User Name", font=(self.font2, 18, "bold"), bg=self.color2).place(x=150,y=180)
        self.username_entry = Entry(self.frame_2, font=(self.font1, 12), bg=self.color4, fg=self.color3)
        self.username_entry.place(x=400, y=180, width=250, height=35)
        self.pwd= Label(self.frame_2, text="Enter Password", font=(self.font2, 18, "bold"), bg=self.color2).place(x=150,y=250)
        self.pwd_entry=Entry(self.frame_2, font=(self.font1, 12), bg=self.color4, fg=self.color3)
        self.pwd_entry.place(x=400, y=250, width=250, height=35)
        self.pwd_entry.config(show="*",font=("bold",18))        
        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font1, 13,"bold"), bd=2, command=self.Checklogin, cursor="hand2", 
        bg=self.color5,fg=self.color3).place(x=450,y=330,width=100,height=35)
     def Checklogin(self):
       if (self.username_entry.get() == "" or self.pwd_entry==""):
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
       else:
           try:
               connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
               curs = connection.cursor()
               sql="select * from employee where name=%s and phone=%s"
               un=self.username_entry.get()
               ps=self.pwd_entry.get()
               curs.execute(sql,[(un),(ps)])
               row=curs.fetchone()
               if row == None:
                   messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                                      
               else:
                   self.ShowDetails(row) 
                   connection.close()                   
                   
           except Exception as e:
               messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

     def ShowDetails(self, row):
        self.ClearScreen()
        head=Label(self.frame_2, text="Employee Details", font=(self.font2,22,"bold","underline")).place(x=350,y=10)
        name = Label(self.frame_2, text="Name", font=(self.font2,18,"bold")).place(x=100,y=60)
        name_data = Label(self.frame_2, text=row[0], font=(self.font1, 15)).place(x=300, y=60)
        
        title = Label(self.frame_2, text="Title", font=(self.font2, 18, "bold")).place(x=100,y=100)
        title_data = Label(self.frame_2, text=row[1], font=(self.font1, 15)).place(x=300, y=100)

        gender = Label(self.frame_2, text="Gender", font=(self.font2, 18, "bold")).place(x=100,y=150)
        gender_data = Label(self.frame_2, text=row[2], font=(self.font1, 15)).place(x=300, y=150)

        dob = Label(self.frame_2, text="Date of Birth", font=(self.font2, 18, "bold")).place(x=100,y=200)
        dob_data = Label(self.frame_2, text=row[3], font=(self.font1, 15)).place(x=300, y=200)

        doj = Label(self.frame_2, text="Date of joining", font=(self.font2, 18, "bold")).place(x=100,y=250)
        doj_data = Label(self.frame_2, text=row[4], font=(self.font1, 15)).place(x=300, y=250)

        mailid = Label(self.frame_2, text="Mailid", font=(self.font2, 18, "bold")).place(x=100,y=300)
        mailid_data = Label(self.frame_2, text=row[5], font=(self.font1, 15)).place(x=300, y=300)

        phone= Label(self.frame_2, text="Phone", font=(self.font2, 18, "bold")).place(x=100,y=350)
        phone_data = Label(self.frame_2, text=row[6], font=(self.font1, 15)).place(x=300, y=350)

        aadhar = Label(self.frame_2, text="Aadhar Number", font=(self.font2, 18, "bold"),).place(x=100,y=400)
        aadhar_data = Label(self.frame_2, text=row[7], font=(self.font1, 15)).place(x=300, y=400)

        city = Label(self.frame_2, text="City", font=(self.font2, 18, "bold"), bg=self.color2).place(x=100,y=450)
        city_data = Label(self.frame_2, text=row[8], font=(self.font1, 15)).place(x=300, y=450)

        pin = Label(self.frame_2, text="Pin", font=(self.font2, 18, "bold"), bg=self.color2).place(x=100,y=500)
        pin_data = Label(self.frame_2, text=row[9], font=(self.font1, 15)).place(x=300, y=500)

        address = Label(self.frame_2, text="Address", font=(self.font2, 18, "bold"), bg=self.color2).place(x=100,y=550)
        address_data= Label(self.frame_2, text=row[10], font=(self.font1, 15)).place(x=300, y=550)
    
     def Contact_Update(self):
        self.ClearScreen()

        self.contact = Label(self.frame_2, text="Enter Contact Number", font=(self.font2, 18, "bold"), bg=self.color2).place(x=332,y=170)
        self.contact_entry = Entry(self.frame_2, font=(self.font1, 12), bg=self.color4, fg=self.color3)
        self.contact_entry.place(x=360, y=220, width=200, height=40)
        self.submit = Button(self.frame_2, text='Submit', font=(self.font1, 14), bd=2, command=self.CheckContact_Update, cursor="hand2",
         bg=self.color1,fg=self.color3).place(x=420,y=280,width=100)

     def CheckContact_Update(self):
        if self.contact_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from employee where phone=%s", self.contact_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    self.UpdateEntryDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

     def UpdateDetails(self, row):
        if( self.name_entry.get() == "" or self.title_entry.get() == "" or self.gender_entry.get() == "" or self.dob_entry.get() == "" or 
        self.doj_entry.get() == "" or self.mailid_entry.get() == "" or self.phone_entry.get() == "" or self.aadhar_entry.get() == "" or self.city_entry.get() == "" or
            self.pin_entry.get()== "" or self.address_entry.get()==""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from employee where phone=%s",row[6])
                row=curs.fetchone()

                if row==None:
                    messagebox.showerror("Error!","The contact number doesn't exists",parent=self.window)
                else:
                    curs.execute("update employee set name=%s,title=%s,gender=%s,dob=%s,doj=%s,mailid=%s,phone=%s,aadhar=%s,city=%s,pin=%s,address=%s where phone=%s",
                                        (
                                            self.name_entry.get(),
                                            self.title_entry.get(),
                                            self.gender_entry.get(),
                                            self.dob_entry.get(),
                                            self.doj_entry.get(),
                                            self.mailid_entry.get(),
                                            self.phone_entry.get(),
                                            self.aadhar_entry.get(),
                                            self.city_entry.get(),
                                            self.pin_entry.get(),
                                            self.address_entry.get(),
                                            row[6]
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    

     def UpdateEntryDetails(self, row):
        self.ClearScreen()
        
        self.name = Label(self.frame_2, text="Name", font=(self.font2,18,"bold")).place(x=100,y=60)
        self.name_entry = Entry(self.frame_2, font=(self.font1, 15),bg=self.color4, fg=self.color3)
        self.name_entry.insert(0,row[0])
        self.name_entry.place(x=300, y=60,width=150,height=22)
        
        self.title = Label(self.frame_2, text="Title", font=(self.font2, 18, "bold")).place(x=100,y=100)
        self.title_entry = Entry(self.frame_2, text=row[1], font=(self.font1, 15))
        self.title_entry.insert(0,row[1])
        self.title_entry.place(x=300, y=100,width=150,height=22)
        
        self.gender = Label(self.frame_2, text="Gender", font=(self.font2, 18, "bold")).place(x=100,y=150)
        self.gender_entry=Entry(self.frame_2,text=row[2],font=(self.font1,15))
        self.gender_entry.insert(0,row[2])
        self.gender_entry.place(x=300,y=150)
                 

        self.dob = Label(self.frame_2, text="Date of Birth", font=(self.font2, 18, "bold")).place(x=100,y=200)
        self.dob_entry = Entry(self.frame_2, text=row[3], font=(self.font1, 15))
        self.dob_entry.insert(0,row[3])
        self.dob_entry.place(x=300, y=200)

        self.doj = Label(self.frame_2, text="Date of joining", font=(self.font2, 18, "bold")).place(x=100,y=250)
        self.doj_entry = Entry(self.frame_2, text=row[4], font=(self.font1, 15))
        self.doj_entry.insert(0,row[4])
        self.doj_entry.place(x=300, y=250)

        self.mailid = Label(self.frame_2, text="Mailid", font=(self.font2, 18, "bold")).place(x=100,y=300)
        self.mailid_entry = Entry(self.frame_2, text=row[5], font=(self.font1, 15))
        self.mailid_entry.insert(0,row[5])
        self.mailid_entry.place(x=300, y=300)

        self.phone= Label(self.frame_2, text="Phone", font=(self.font2, 18, "bold")).place(x=100,y=350)
        self.phone_entry = Entry(self.frame_2, text=row[6], font=(self.font1, 15))
        self.phone_entry.insert(0,row[6])
        self.phone_entry.place(x=300, y=350)

        self.aadhar = Label(self.frame_2, text="Aadhar Number", font=(self.font2, 18, "bold"),).place(x=100,y=400)
        self.aadhar_entry = Entry(self.frame_2, text=row[7], font=(self.font1, 15))
        self.aadhar_entry.insert(0,row[7])
        self.aadhar_entry.place(x=300, y=400)

        self.city = Label(self.frame_2, text="City", font=(self.font2, 18, "bold"), bg=self.color2).place(x=100,y=450)
        self.city_entry = Entry(self.frame_2, text=row[8], font=(self.font1, 15))
        self.city_entry.insert(0,row[8])
        self.city_entry.place(x=300, y=450)

        self.pin = Label(self.frame_2, text="Pin", font=(self.font2, 18, "bold"), bg=self.color2).place(x=100,y=500)
        self.pin_entry = Entry(self.frame_2, text=row[9], font=(self.font1, 15))
        self.pin_entry.insert(0,row[9])
        self.pin_entry.place(x=300, y=500)

        self.address = Label(self.frame_2, text="Address", font=(self.font2, 18, "bold"), bg=self.color2).place(x=100,y=550)
        self.address_entry= Entry(self.frame_2, text=row[10], font=(self.font1, 15))
        self.address_entry.insert(0,row[10])
        self.address_entry.place(x=300, y=550)
        
        self.submit = Button(self.frame_2, text='Submit', font=(self.font1, 12), bd=2, command=partial(self.UpdateDetails, row), 
        cursor="hand2", bg=self.color5,fg=self.color3).place(x=300,y=600,width=100)
        self.cancel = Button(self.frame_2, text='Cancel', font=(self.font1, 12), bd=2, command=self.reset_fields, cursor="hand2", 
        bg=self.color5,fg=self.color3).place(x=420,y=600,width=100)

     def Contact_Delete(self):
        self.ClearScreen()

        self.contact = Label(self.frame_2, text="Enter Contact Number", font=(self.font2, 18, "bold"), bg=self.color2).place(x=332,y=170)
        self.contact_entry = Entry(self.frame_2, font=(self.font1, 12), bg=self.color4, fg=self.color3)
        self.contact_entry.place(x=360, y=220, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font1, 10), bd=2, command=self.DeleteData, cursor="hand2", 
        bg=self.color1,fg=self.color3).place(x=420,y=280,width=80)

     def DeleteData(self):
        if self.contact_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from employee where phone=%s", self.contact_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    curs.execute("delete from employee where phone=%s", self.contact_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

     def Exit(self):
        self.window.destroy()

     
     
     
    

     
     
             
# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()

        
