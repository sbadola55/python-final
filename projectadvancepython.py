import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
import time


class tkk:
    def __init__(self):
        # creating variables to ask user if he would like to create a particular database or table
        createDatabase = (input("Would you like to create a new database by dropping the current database or if "
                                "you are running the program first time enter 'y' else enter any letter or number: ")).lower()

        if (createDatabase == "y"):
            # creating databse
            mydb = mysql.connector.connect(host="localhost", user="root",
                                           passwd="")
            mycursor = mydb.cursor()
            mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
            mycursor.execute("CREATE DATABASE mydatabase")
            mydb.close()
            mycursor.close()
        createTable = input("Would u like to create all tables again? input 'y' if yes else enter any letter or number: ").lower()
        if (createTable == "y"):
            mydb2 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor2 = mydb2.cursor()

            mycursor2.execute("DROP TABLE IF EXISTS credentials")
            mycursor2.execute("CREATE TABLE credentials(username varchar(20) PRIMARY KEY,password varChar(20))")
            sql = "INSERT INTO credentials (username, password) VALUES (%s, %s)"
            val = ("admin", "123456")
            mycursor2.execute(sql, val)
            mydb2.commit()

            mycursor2.execute("DROP TABLE IF EXISTS course")
            mycursor2.execute("DROP TABLE IF EXISTS students")

            mycursor2.execute("CREATE TABLE course(cNum varchar(20) PRIMARY KEY, cName varchar(20))")
            mycursor2.execute(
                "CREATE TABLE students(stdName varchar(20), stdNumber int PRIMARY KEY,cNum varchar(20),grade int,extraInfo varchar(30))")

            mycursor2.execute("DROP TABLE IF EXISTS professor")
            mycursor2.execute(
                "CREATE TABLE professor(profName varchar(20),profNum varchar(20) PRIMARY KEY ,cNum varchar(20))")
            mycursor2.close()
            mydb2.close()
        insertData=input("Would you like to make enteries to created table? input 'y' if yes else enter any letter or number: " ).lower()
        if(insertData=="y"):
            time.sleep(3.0)
            self.addDataToCourse()
            self.addDataToProfessor()
            self.addDataToCredentials()
            self.addDataToStudents()

        # creating main window
        self.main_window = Tk()
        self.main_window.geometry("1350x700+0+0")
        self.main_window.title("User Type")
        self.main_window.configure(bg="cyan2")
        # creating frames
        self.first_Frame = tkinter.Frame(self.main_window,bg="cyan2")
        self.second_Frame = tkinter.Frame(self.main_window,bg="cyan2")
        self.third_Frame = tkinter.Frame(self.main_window,bg="cyan2")
        self.fourth_Frame = tkinter.Frame(self.main_window,bg="cyan2")

        # creating labels for first_Frame
        self.label1 = tkinter.Label(self.first_Frame, text="UserType", width=50, pady=20, font=("bold", 20),bg="cyan2")
        # creating radio buttons second_Frame to select a user type on first Window
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.R1 = tkinter.Radiobutton(self.second_Frame, text="Admin User", pady=10, variable=self.radio_var, value=1,font=("bold", 10),bg="cyan2")
        self.R2 = tkinter.Radiobutton(self.second_Frame, text="Professor User", pady=10, variable=self.radio_var,
                                      value=2,font=("bold", 10),bg="cyan2")
        self.R3 = tkinter.Radiobutton(self.second_Frame, text="Student User", pady=10, variable=self.radio_var, value=3,font=("bold", 10),bg="cyan2")

        # creating labels and Entries for fourth_Frame and placing them in grid
        # label and entry for username
        self.label2 = tkinter.Label(self.fourth_Frame, text="Username ", pady=10, width=25, font=("bold", 10),bg="cyan2")
        self.label2.grid(row=0, column=0)
        self.user = tkinter.Entry(self.fourth_Frame, width=25)

        self.user.grid(row=0, column=1)
        # label and entry for password
        self.label4 = tkinter.Label(self.fourth_Frame, text="Password ", pady=15, width=25, font=("bold", 10),bg="cyan2")
        self.label4.grid(row=1, column=0)

        self.passs = tkinter.Entry(self.fourth_Frame, width=25,show="*")

        self.passs.grid(row=1, column=1)

        # Creating Buttons for third_Frame
        self.confirm = tkinter.Button(self.third_Frame, text="Log In ", command=self.reset ,activebackground="grey",bg='white')

        self.exit = tkinter.Button(self.third_Frame, text="Exit", command=self.main_window.destroy,activebackground="grey",bg='white')

        # Packing labels and Radio Buttons
        self.label1.pack()
        self.R1.pack()
        self.R2.pack()
        self.R3.pack()
        # Packing frames
        self.first_Frame.pack()
        self.second_Frame.pack()
        self.fourth_Frame.pack()
        self.third_Frame.pack()

        # packing Buttons
        self.confirm.pack(side="left")

        self.exit.pack(side="left")

        # Putting the main window into mainloop
        tkinter.mainloop()


    def reset(self):

        if (self.user.get() == "" or self.passs.get() == ""):
            self.invalid()




        elif self.radio_var.get() == 1:

            # creating window for Admin User
            mydb8 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor8 = mydb8.cursor()
            mycursor8.execute("select password from credentials where username='admin'")
            data = mycursor8.fetchone()
            pswd = data[0]

            mycursor8.close()

            if (self.user.get() == "admin") and (self.passs.get() == pswd):

                self.window1 = Tk()
                self.window1.geometry("1350x700+0+0")
                self.window1.title("Admin")
                self.window1.configure(bg="cyan2")
                # creating levels for the window
                self.first_Frame = tkinter.Frame(self.window1,bg="cyan2")
                self.second_Frame = tkinter.Frame(self.window1,bg="cyan2")
                self.third_Frame = tkinter.Frame(self.window1,bg="cyan2")

                # cerating labels for first_Frame
                self.label1 = tkinter.Label(self.first_Frame, text="Admin User", width=50, pady=20, font=("bold", 20),bg="cyan2")

                # creating labels for second_Frame and placing them in grid
                self.comboSelectUser = ttk.Combobox(self.second_Frame, font=("times new roman", 16, "bold"),
                                                    state="readonly")
                self.comboSelectUser['values'] = ("Student", "Professor", "Course")
                self.comboSelectUser.grid(row=2, column=1, pady=20, padx=40)

                # creating Buttons for third_Frame
                self.confirm = tkinter.Button(self.third_Frame, text="Confirm", command=self.UserSelect,activebackground="grey",bg='white')

                self.reset = tkinter.Button(self.third_Frame, text="Exit", command=self.window1.destroy,activebackground="grey",bg='white')
                # packing label 1
                self.label1.pack()

                # packing frames
                self.first_Frame.pack()
                self.second_Frame.pack()
                self.third_Frame.pack()

                # packing buttons
                self.confirm.pack(side="left")
                self.reset.pack(side="left")
                # putting window1 into mainloop
                self.window1.mainloop()
            else:
                tkinter.messagebox.showinfo('Response', 'Invalid Admin Credentials')

        elif self.radio_var.get() == 2:

            # creating window for professor user
            self.window2 = Tk()
            self.window2.geometry("1350x700+0+0")
            self.window2.title("Professor")
            self.window2.configure(bg="cyan2")

            # creating Frames
            self.first_Frame = tkinter.Frame(self.window2,bg="cyan2")
            self.second_Frame = tkinter.Frame(self.window2,bg="cyan2")
            self.third_Frame = tkinter.Frame(self.window2,bg="cyan2")

            # creating labels for first_frame annd second_frame and placing them in grid
            self.PU = tkinter.Label(self.first_Frame, text="Professor User", pady=20, width=50, font=("bold", 20),bg="cyan2")
            self.pname = tkinter.Label(self.second_Frame, text="Professor Name ", pady=10, width=25, font=("bold", 10),bg="cyan2")
            self.pname.grid(row=0, column=0)
            self.pentry = tkinter.Entry(self.second_Frame, width=25)
            self.pentry.grid(row=0, column=1)
            self.snum = tkinter.Label(self.second_Frame, text="Student Number ", pady=10, width=25, font=("bold", 10),bg="cyan2")
            self.snum.grid(row=1, column=0)
            self.sentry = tkinter.Entry(self.second_Frame, width=25)
            self.sentry.grid(row=1, column=1)
            self.sname = tkinter.Label(self.second_Frame, text="Student Name ", width=25, pady=10, font=("bold", 10),bg="cyan2")
            self.sname.grid(row=2, column=0)
            self.sentry1 = tkinter.Entry(self.second_Frame, width=25)
            self.sentry1.grid(row=2, column=1)
            self.cnum1 = tkinter.Label(self.second_Frame, text="Course Number ", width=25, pady=10, font=("bold", 10),bg="cyan2")
            self.cnum1.grid(row=3, column=0)
            self.centry1 = tkinter.Entry(self.second_Frame, width=25)
            self.centry1.grid(row=3, column=1)
            self.cname = tkinter.Label(self.second_Frame, text="Course Name", width=25, pady=10, font=("bold", 10),bg="cyan2")
            self.cname.grid(row=4, column=0)
            self.cnentry = tkinter.Entry(self.second_Frame, width=25)
            self.cnentry.grid(row=4, column=1)
            self.cgrade = tkinter.Label(self.second_Frame, text="Course Grade", width=25, pady=15, font=("bold", 10),bg="cyan2")
            self.cgrade.grid(row=5, column=0)
            self.gentry = tkinter.Entry(self.second_Frame, width=25)
            self.gentry.grid(row=5, column=1)
            self.pnum = tkinter.Label(self.second_Frame, text="Professor Number ", pady=10, width=25, font=("bold", 10),bg="cyan2")
            self.pnum.grid(row=6, column=0)
            self.pentrynum = tkinter.Entry(self.second_Frame, width=25)
            self.pentrynum.grid(row=6, column=1)

            # Creating buttons for third frame
            self.confirm = tkinter.Button(self.third_Frame, text="Reset", command=self.empty,activebackground="grey",bg='white')
            self.update = tkinter.Button(self.third_Frame, text="Submit", command=self.enter,activebackground="grey",bg='white')

            self.reset = tkinter.Button(self.third_Frame, text="Exit", command=self.window2.destroy,activebackground="grey",bg='white')

            # packing label
            self.PU.pack()

            # packing frames
            self.first_Frame.pack()
            self.second_Frame.pack()
            self.third_Frame.pack()

            # packing buttons
            self.confirm.pack(side="left")
            self.update.pack(side="left")
            self.reset.pack(side="left")

            # putting window2 inn mainloop
            self.window2.mainloop()

        elif self.radio_var.get() == 3:

            # creating window for Student User
            self.window3 = Tk()
            self.window3.geometry("1350x700+0+0")
            self.window3.title("Student")
            self.window3.configure(bg="cyan2")

            # creating frames
            self.first_Frame = tkinter.Frame(self.window3,bg="cyan2")
            self.second_Frame = tkinter.Frame(self.window3,bg="cyan2")
            self.third_Frame = tkinter.Frame(self.window3,bg="cyan2")
            self.Fourth_Frame = tkinter.Frame(self.window3,bg="cyan2")

            # creating Labels for first_Frame
            self.Stdusr = tkinter.Label(self.first_Frame, text="Student User", pady=20, width=50, font=("bold", 20),bg="cyan2")
            # creating Labels for second_Frame and placing them in grid
            self.number = tkinter.Label(self.second_Frame, text="Enter Your Number ", pady=20, width=25, font=("bold", 10),bg="cyan2")
            self.number.grid(row=0, column=0)
            self.entrysnumber = tkinter.Entry(self.second_Frame, width=25)
            self.entrysnumber.grid(row=0, column=1)

            self.outpu0 = tkinter.Label(self.Fourth_Frame,text="Student Name", width=25,bg="cyan2")
            self.outpu0.grid(column=0, row=4)
            self.outpu1 = tkinter.Label(self.Fourth_Frame,text="Student Number", width=25,bg="cyan2")
            self.outpu1.grid(column=1, row=4)
            self.outpu2 = tkinter.Label(self.Fourth_Frame,text="Course Number", width=25,bg="cyan2")
            self.outpu2.grid(column=2, row=4)
            self.outpu3 = tkinter.Label(self.Fourth_Frame,text="grade", width=25,bg="cyan2")
            self.outpu3.grid(column=3, row=4)
            self.outpu4 = tkinter.Label(self.Fourth_Frame,text="Extra Info", width=25,bg="cyan2")
            self.outpu4.grid(column=4, row=4)

            self.output0 = tkinter.Entry(self.Fourth_Frame, width=25)
            self.output0.grid(column=0, row=5)
            self.output1 = tkinter.Entry(self.Fourth_Frame, width=25)
            self.output1.grid(column=1, row=5)
            self.output2 = tkinter.Entry(self.Fourth_Frame, width=25)
            self.output2.grid(column=2, row=5)
            self.output3 = tkinter.Entry(self.Fourth_Frame, width=25)
            self.output3.grid(column=3, row=5)
            self.output4 = tkinter.Entry(self.Fourth_Frame, width=25)
            self.output4.grid(column=4, row=5)

            # creating buttons for third frame
            self.confirm = tkinter.Button(self.third_Frame, text="Enter", command=self.select,activebackground="grey",bg='white')

            self.reset = tkinter.Button(self.third_Frame, text="Exit", command=self.window3.destroy,activebackground="grey",bg='white')
            # packing labels of first_Frame
            self.Stdusr.pack()

            # packing frames
            self.first_Frame.pack()
            self.second_Frame.pack()

            self.third_Frame.pack()
            self.Fourth_Frame.pack()

            # packing buttons
            self.confirm.pack(side="left")

            self.reset.pack(side="left")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="mydatabase"
            )
            self.window3.mainloop()

    def UserSelect(self):
        self.value = self.comboSelectUser.get()
        if self.value == "Student":
            self.window4 = Tk()
            self.window4.geometry("1350x700+0+0")
            self.window4.title("Student User")
            self.window4.configure(bg="cyan2")
            # creating levels for the admin main window2
            self.first_Frame = tkinter.Frame(self.window4)
            self.second_Frame = tkinter.Frame(self.window4)
            self.third_Frame = tkinter.Frame(self.window4)

            # cerating labels for the admin first_Frame
            self.label1 = tkinter.Label(self.first_Frame, text="Student  Entry", width=50, pady=20,
                                        font=("bold", 20),bg="cyan2")

            # creating labels for the admin second_Frame and placing them in grid
            self.labelStdNum = tkinter.Label(self.second_Frame, text="Student Number", pady=10, width=25,
                                             font=("bold", 10),bg="cyan2")
            self.labelStdNum.grid(row=0, column=0)
            self.entryStdNum = tkinter.Entry(self.second_Frame, width=25)
            self.entryStdNum.grid(row=0, column=1)
            self.labelStdName = tkinter.Label(self.second_Frame, text="Student Name", pady=10, width=25,
                                              font=("bold", 10),bg="cyan2")
            self.labelStdName.grid(row=1, column=0)
            self.entryStdName = tkinter.Entry(self.second_Frame, width=25)
            self.entryStdName.grid(row=1, column=1)
            self.labelCourseNum = tkinter.Label(self.second_Frame, text="Course Number ", pady=10, width=25,
                                                font=("bold", 10),bg="cyan2")
            self.labelCourseNum.grid(row=2, column=0)
            self.entryCourseNum = tkinter.Entry(self.second_Frame, width=25)
            self.entryCourseNum.grid(row=2, column=1)

            self.labelGrade = tkinter.Label(self.second_Frame, text="Grade", width=25, pady=10, font=("bold", 10),bg="cyan2")
            self.labelGrade.grid(row=3, column=0)
            self.entryGrade = tkinter.Entry(self.second_Frame, width=25)
            self.entryGrade.grid(row=3, column=1)
            self.labeluserName = tkinter.Label(self.second_Frame, text="Username", width=25, pady=10,
                                               font=("bold", 10),bg="cyan2")
            self.labeluserName.grid(row=4, column=0)
            self.entryUserName1 = tkinter.Entry(self.second_Frame, width=25)
            self.entryUserName1.grid(row=4, column=1)
            self.labelUserPassword = tkinter.Label(self.second_Frame, text="Password", width=25, pady=10,
                                                   font=("bold", 10),bg="cyan2")
            self.labelUserPassword.grid(row=5, column=0)
            self.entryUserPassword1 = tkinter.Entry(self.second_Frame, width=25)
            self.entryUserPassword1.grid(row=5, column=1)
            self.labelExtraInfo = tkinter.Label(self.second_Frame, text="Optional: Any extra info needed", pady=15,
                                                width=25,
                                                font=("bold", 10),bg="cyan2")
            self.labelExtraInfo.grid(row=6, column=0)
            self.entryExtraInfo = tkinter.Entry(self.second_Frame, width=25)
            self.entryExtraInfo.grid(row=6, column=1)

            # creating Buttons for third_Frame
            self.confirm1 = tkinter.Button(self.third_Frame, text="Confirm", command=self.accept1,activebackground="grey",bg='white')
            self.update1 = tkinter.Button(self.third_Frame, text="Update", command=self.updat1,activebackground="grey",bg='white')
            self.delete1 = tkinter.Button(self.third_Frame, text="Delete", command=self.delet1,activebackground="grey",bg='white')

            self.reset1 = tkinter.Button(self.third_Frame, text="Exit", command=self.window4.destroy,activebackground="grey",bg='white')
            # packing label 1
            self.label1.pack()

            # packing frames
            self.first_Frame.pack()
            self.second_Frame.pack()
            self.third_Frame.pack()

            # packing buttons
            self.confirm1.pack(side="left")
            self.update1.pack(side="left")
            self.delete1.pack(side="left")
            self.reset1.pack(side="left")

            # putting window1 into mainloop
            self.window4.mainloop()

        elif self.value == "Professor":
            self.window5 = Tk()
            self.window5.geometry("1350x700+0+0")
            self.window5.title("Admin")
            self.window5.configure(bg="cyan2")
            # creating levels for the admin main window
            self.first_Frame = tkinter.Frame(self.window5,bg="cyan2")
            self.second_Frame = tkinter.Frame(self.window5,bg="cyan2")
            self.third_Frame = tkinter.Frame(self.window5,bg="cyan2")

            # cerating labels for the admin first_Frame
            self.label1 = tkinter.Label(self.first_Frame, text="Professor Enter", width=50, pady=20, font=("bold", 20),bg="cyan2")

            # creating labels for the admin second_Frame and placing them in grid
            self.labelProfName = tkinter.Label(self.second_Frame, text="Professor Name", pady=10, width=25,
                                               font=("bold", 10),bg="cyan2")
            self.labelProfName.grid(row=0, column=0)
            self.entryProfName = tkinter.Entry(self.second_Frame, width=25)
            self.entryProfName.grid(row=0, column=1)
            self.labelProfNumber = tkinter.Label(self.second_Frame, text="Professor Number", pady=10, width=25,
                                                 font=("bold", 10),bg="cyan2")
            self.labelProfNumber.grid(row=1, column=0)
            self.entryProfNumber = tkinter.Entry(self.second_Frame, width=25)
            self.entryProfNumber.grid(row=1, column=1)
            self.labeluserName = tkinter.Label(self.second_Frame, text="Username", width=25, pady=10,
                                               font=("bold", 10),bg="cyan2")
            self.labeluserName.grid(row=2, column=0)
            self.entryUserName = tkinter.Entry(self.second_Frame, width=25)
            self.entryUserName.grid(row=2, column=1)
            self.labelUserPassword = tkinter.Label(self.second_Frame, text="Password", width=25, pady=10,
                                                   font=("bold", 10),bg="cyan2")
            self.labelUserPassword.grid(row=3, column=0)
            self.entryUserPassword = tkinter.Entry(self.second_Frame, width=25)
            self.entryUserPassword.grid(row=3, column=1)

            # creating Buttons for third_Frame
            self.confirm2 = tkinter.Button(self.third_Frame, text="Confirm", command=self.accept2,activebackground="grey",bg='white')
            self.update2 = tkinter.Button(self.third_Frame, text="Update", command=self.updat2,activebackground="grey",bg='white')
            self.delete2 = tkinter.Button(self.third_Frame, text="Delete", command=self.delet2,activebackground="grey",bg='white')

            self.reset = tkinter.Button(self.third_Frame, text="Exit", command=self.window5.destroy,activebackground="grey",bg='white')
            # packing label 1
            self.label1.pack()

            # packing frames
            self.first_Frame.pack()
            self.second_Frame.pack()
            self.third_Frame.pack()

            # packing buttons
            self.confirm2.pack(side="left")
            self.update2.pack(side="left")
            self.delete2.pack(side="left")
            self.reset.pack(side="left")

            # putting window1 into mainloop
            self.window5.mainloop()

        elif self.value == "Course":
            self.window6 = Tk()
            self.window6.geometry("1350x700+0+0")
            self.window6.title("Admin")
            self.window6.configure(bg="cyan2")
            # creating levels for the admin main window
            self.Cfirst_Frame = tkinter.Frame(self.window6,bg="cyan2")
            self.Csecond_Frame = tkinter.Frame(self.window6,bg="cyan2")
            self.Cthird_Frame = tkinter.Frame(self.window6,bg="cyan2")

            # cerating labels for the admin first_Frame
            self.Clabel1 = tkinter.Label(self.Cfirst_Frame, text="Course Enter ", width=50, pady=20, font=("bold", 20),bg="cyan2")

            # creating labels for the admin second_Frame and placing them in grid
            self.labelCourseNum = tkinter.Label(self.Csecond_Frame, text="Course Number ", pady=10, width=25,
                                                font=("bold", 10),bg="cyan2")
            self.labelCourseNum.grid(row=0, column=0)
            self.entryCourseNum = tkinter.Entry(self.Csecond_Frame, width=25)
            self.entryCourseNum.grid(row=0, column=1)
            self.labelCourseName = tkinter.Label(self.Csecond_Frame, text="Course Name ", pady=10, width=25,
                                                 font=("bold", 10),bg="cyan2")
            self.labelCourseName.grid(row=1, column=0)
            self.entryCourseName = tkinter.Entry(self.Csecond_Frame, width=25)
            self.entryCourseName.grid(row=1, column=1)

            # creating Buttons for third_Frame
            self.confirm3 = tkinter.Button(self.Cthird_Frame, text="Confirm", command=self.accept3,activebackground="grey",bg='white')
            self.update3 = tkinter.Button(self.Cthird_Frame, text="Update", command=self.updat3,activebackground="grey",bg='white')
            self.delete3 = tkinter.Button(self.Cthird_Frame, text="Delete", command=self.delet3,activebackground="grey",bg='white')

            self.reset3 = tkinter.Button(self.Cthird_Frame, text="Exit", command=self.window6.destroy,activebackground="grey",bg='white')
            # packing label 1
            self.Clabel1.pack()

            # packing frames
            self.Cfirst_Frame.pack()
            self.Csecond_Frame.pack()
            self.Cthird_Frame.pack()

            # packing buttons
            self.confirm3.pack(side="left")
            self.update3.pack(side="left")
            self.delete3.pack(side="left")
            self.reset3.pack(side="left")

            # putting window1 into mainloop
            self.window6.mainloop()
    # accept1 is method to insert data into students table for admin
    def accept1(self):
        try:
            mydb4 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor4 = mydb4.cursor()
            sql2 = "INSERT INTO credentials (username, password) VALUES (%s, %s)"
            val2 = (self.entryUserName1.get(), self.entryUserPassword1.get())
            sql1 = "INSERT INTO students (stdNumber, stdName,cNum,grade,extraInfo) VALUES (%s, %s,%s,%s,%s)"
            val1 = (self.entryStdNum.get(), self.entryStdName.get(), self.entryCourseNum.get(), self.entryGrade.get(),
                    self.entryExtraInfo.get())
            if (
                    self.entryStdNum.get() != "" and self.entryStdName.get() != "" and self.entryCourseNum.get() != "" and self.entryGrade.get() != "" and self.entryExtraInfo.get() != "" and self.entryUserName1.get() != "" and self.entryUserPassword1.get() != ""):
                if (int(self.entryGrade.get()) >= 0 and int(self.entryGrade.get()) <= 100):
                    mycursor4.execute(sql1, val1)
                    mycursor4.execute(sql2, val2)
                    mydb4.commit()
                    tkinter.messagebox.showinfo('Response', 'Thanks ,your Information has been saved')
                    self.window4.destroy()
                else:
                    tkinter.messagebox.showinfo('Grade Error', 'Grade must be between 0 and 100')
            else:
                tkinter.messagebox.showinfo('Empty Fields', 'Please Fill all the fields to Insert')
            mydb4.close()
            mycursor4.close()
        except Exception as e:
            tkinter.messagebox.showinfo('Exception: ', e)

    # accept2 is method to insert data into Professor table for admin
    def accept2(self):
        try:
            mydb4 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor4 = mydb4.cursor()
            sql3 = "INSERT INTO professor (profName, profNum) VALUES (%s, %s)"
            val3 = (self.entryProfName.get(), self.entryProfNumber.get())
            sql4 = "INSERT INTO credentials (username, password) VALUES (%s, %s)"
            val4 = (self.entryUserName.get(), self.entryUserPassword.get())
            if (
                    self.entryProfName.get() != "" and self.entryProfNumber.get() != "" and self.entryProfName.get() != "" and self.entryProfNumber.get() != ""):
                mycursor4.execute(sql4, val4)
                mycursor4.execute(sql3, val3)
                mydb4.commit()
                tkinter.messagebox.showinfo('Response', 'Thanks ,your Information has been saved')
                self.window5.destroy()
            else:
                tkinter.messagebox.showinfo('Empty Fields', 'Please Fill all the fields to insert')
            mydb4.close()
            mycursor4.close()
        except Exception as e:
            tkinter.messagebox.showinfo('Exception: ', e)

    # accept3 is method to insert data into Course table for admin
    def accept3(self):
        try:
            mydb4 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor4 = mydb4.cursor()
            sql5 = "INSERT INTO course (cNum, cName) VALUES (%s, %s)"
            val5 = (self.entryCourseNum.get(), self.entryCourseName.get())
            if (self.entryCourseName.get() != "" and self.entryCourseNum.get() != ""):
                mycursor4.execute(sql5, val5)
                mydb4.commit()
                tkinter.messagebox.showinfo('Response', 'Thanks ,your Information has been saved')
                self.window6.destroy()
            else:
                tkinter.messagebox.showinfo('Empty Fields', 'Please Fill all the fields to insert')
            mydb4.close()
            mycursor4.close()
            tkinter.messagebox.showinfo('Response', 'Thanks ,your Information has been saved')
        except Exception as e:
            tkinter.messagebox.showinfo('Exception: ', e)

    # enter methods allows the professor user to insert grade into studnets table
    def enter(self):
        try:
            flag = True
            mydb5 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor5 = mydb5.cursor()

            sql6 = "UPDATE students SET  grade=%s where stdNumber=%s"
            val6 = (int(self.gentry.get()), self.sentry.get())

            num = self.sentry.get()
            query = ("""SELECT * FROM students WHERE stdNumber = '%s'""" % (num))
            mycursor5.execute(query)
            results = mycursor5.fetchall()

            num1 = self.pentrynum.get()
            query1 = ("""SELECT * FROM professor WHERE profNum = '%s'""" % (num1))
            mycursor5.execute(query1)
            mycursor5.fetchall()
            length=mycursor5.rowcount
            if(length==0):
                    flag=False

            if (self.gentry.get() != "" and self.sentry.get() != "" and flag and self.pentry.get()!=""and
                    self.centry1.get()!="" and self.sentry1.get()!=""):
                if (int(self.gentry.get()) >= 0 and int(self.gentry.get()) <= 100):
                    mycursor5.execute(sql6, val6)
                    mydb5.commit()
                    tkinter.messagebox.showinfo('Response', 'Thanks ,your Information has been saved')
            else:
                tkinter.messagebox.showinfo('Error', 'Please fill all fields correctly ')
            mydb5.close()
            mycursor5.close()

        except Exception as e:
            tkinter.messagebox.showinfo('Exception: ', e)

    # delet1 method deletes an entry from students table if student has no grade associated with it.
    def delet1(self):
        try:
            mydb6 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor6 = mydb6.cursor()
            if ((self.entryStdNum.get() != "")):
                data=mycursor6.execute("Select grade from students where stdNumber=%s",self.entryStdNum.get())
                tkinter.messagebox.showinfo('checking', data)

                query = "DELETE FROM students WHERE stdNumber = %s"
                data = (self.entryStdNum.get(),)
                mycursor6.execute(query, data)
                mydb6.commit()
                mydb6.close()
                mycursor6.close()
                self.window4.destroy()
                tkinter.messagebox.showinfo("Deletion","Data deleted!")
            else:
                tkinter.messagebox.showinfo('Response', 'Cannot delete this entry')
        except Exception as e:
                tkinter.messagebox.showinfo('Exception: ', e)

    # delet2 method deletes an entry from professor table
    def delet2(self):
        try:
            mydb6 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor6 = mydb6.cursor()
            if ((self.entryProfNumber.get() != "")):

                query1 = "DELETE FROM professor WHERE profNum = %s"
                data1 = (self.entryProfNumber.get(),)
                mycursor6.execute(query1, data1)
                mydb6.commit()
                mydb6.close()
                mycursor6.close()
                self.window5.destroy()
                tkinter.messagebox.showinfo("Deletion","Data deleted!")
            else:
                tkinter.messagebox.showinfo('Response', 'Cannot delete this entry')
        except Exception as e:
                tkinter.messagebox.showinfo('Exception: ', e)

    # delet3 method  an entry from course table
    def delet3(self):
        try:
            mydb6 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor6 = mydb6.cursor()
            if ((self.entryCourseNum.get() != "")):

                query3 = "DELETE FROM course WHERE cNum = %s"
                data3 = (self.entryCourseNum.get(),)
                mycursor6.execute(query3, data3)
                mydb6.commit()
                mydb6.close()
                mycursor6.close()
                self.window6.destroy()
                tkinter.messagebox.showinfo("Deletion","Data deleted!")
            else:
                tkinter.messagebox.showinfo('Response', 'Cannot delete this entry')
        except Exception as e:
                tkinter.messagebox.showinfo('Exception: ', e)
    # admin updates data of student using updat1
    def updat1(self):
        try:
            mydb7 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            q1 = "UPDATE students SET stdName=%s, cNum=%s, grade=%s, extraInfo=%s where stdNumber=%s"
            val1 = (
                self.entryStdName.get(), self.entryCourseNum.get(),
                int(self.entryGrade.get()), self.entryExtraInfo.get(), self.entryStdNum.get())
            q2 = "Update credentials set  password=%s where username=%s"
            val2 = (self.entryUserPassword1.get(), self.entryUserName1.get())
            mycursor7 = mydb7.cursor()

            if (
                    self.entryStdNum.get() != "" and self.entryStdName.get() != "" and self.entryCourseNum.get() != "" and self.entryGrade.get() != "" and self.entryExtraInfo.get() != ""):
                if (int(self.entryGrade.get()) >= 0 and int(self.entryGrade.get()) <= 100):
                    mycursor7.execute(q1, val1)
                    mycursor7.execute(q2, val2)
                    mydb7.commit()
                    tkinter.messagebox.showinfo('Update', 'Information Updated Successfully!')
                    self.window4.destroy()
                else:
                    tkinter.messagebox.showinfo('Grade Error', 'Grade must be between 0 and 100')
            else:
                tkinter.messagebox.showinfo('Empty Fields', 'Please Fill all the fields to update')
            mydb7.close()
            mycursor7.close()
        except Exception as e:
                tkinter.messagebox.showinfo('Exception: ', e)

    # admin updates data of professor using updat2
    def updat2(self):
        try:
            mydb7 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor7 = mydb7.cursor()
            q1 = "UPDATE professor SET profName=%s where profNum=%s"
            val1 = (self.entryProfName.get(), self.entryProfNumber.get())
            q2 = "Update credentials set  password=%s where username=%s"
            val2 = (self.entryUserPassword.get(), self.entryUserName.get())

            if (
                    self.entryProfName.get() != "" and self.entryProfNumber.get() != ""):
                mycursor7.execute(q1, val1)
                mycursor7.execute(q2, val2)
                mydb7.commit()
                tkinter.messagebox.showinfo('Update', 'Information Updated Successfully!')
                self.window5.destroy()
            else:
                tkinter.messagebox.showinfo('Empty Fields', 'Please Fill all the fields to update')
            mydb7.close()
            mycursor7.close()
        except Exception as e:
                tkinter.messagebox.showinfo('Exception: ', e)

    # admin updates data of course using updat3
    def updat3(self):
        try:
            mydb7 = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor7 = mydb7.cursor()
            q1 = "UPDATE course SET cName=%s where cNum=%s"
            val1 = (self.entryCourseName.get(), self.entryCourseNum.get())

            if (self.entryCourseName.get() != "" and self.entryCourseNum.get() != ""):
                mycursor7.execute(q1, val1)
                mydb7.commit()
                tkinter.messagebox.showinfo('Update', 'Information Updated Successfully!')
                self.window6.destroy()
            else:
                tkinter.messagebox.showinfo('Empty Fields', 'Please Fill all the fields to update')
            mydb7.close()
            mycursor7.close()
        except Exception as e:
                tkinter.messagebox.showinfo('Exception: ', e)

    def invalid(self):
        tkinter.messagebox.showinfo('Response', 'Please input Username/Password')
    # empty resets fields of professor window when reset button is clicked
    def empty(self):
        self.pentry.delete(0, 'end')
        self.sentry.delete(0, 'end')
        self.sentry1.delete(0, 'end')
        self.centry1.delete(0, 'end')
        self.cnentry.delete(0, 'end')
        self.gentry.delete(0, 'end')
        self.pentrynum.delete(0,'end')

    # select method display result of grade search to student in student window
    def select(self):
        self.output0.delete(0,'end')
        self.output1.delete(0, 'end')
        self.output2.delete(0, 'end')
        self.output3.delete(0, 'end')
        self.output4.delete(0, 'end')

        mydb8 = mysql.connector.connect(host="localhost", user="root",
                                        passwd="", database="mydatabase")
        mycursor8 = mydb8.cursor()
        num=self.entrysnumber.get()
        query = ("""SELECT * FROM students WHERE stdNumber = '%s'""" % (num))

        mycursor8.execute(query)

        results = mycursor8.fetchall()
        print(results)
        for data in results:
            self.output0.insert(0, data[0])
            self.output1.insert(0, data[1])
            self.output2.insert(0, data[2])
            self.output3.insert(0, data[3])
            self.output4.insert(0, data[4])
            mycursor8.close()
    # Method to insert data into created table students when program runs first time
    def addDataToStudents(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor=mydb.cursor()
            sql = "INSERT INTO students (stdNumber, stdName,cNum,grade,extraInfo) VALUES (%s, %s,%s,%s,%s)"
            val1 = ("2134", "John Smith", "C219", "0", "1st Sem Student")
            val2 = ("2210","Kate Watson","C220","0","2nd Sem Student")
            val3 = ("1298", "Mark Hendrick", "C218", "0", "3rd Sem Student")
            val4 = ("4567", "Allah Rakha", "C314", "0", "1st Sem Student")
            val5 = ("3344", "Michelle Love", "C129", "0", "1st Sem Student")

            mycursor.execute(sql,val1)
            mycursor.execute(sql, val2)
            mycursor.execute(sql, val3)
            mycursor.execute(sql, val4)
            mycursor.execute(sql, val5)
            mydb.commit()
            mycursor.close()
            mydb.close()
        except Exception as e:
            tkinter.messagebox.showinfo("Exception",e)

    # Method to insert data into created table Credentials when program runs first time
    def addDataToCredentials(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor=mydb.cursor()
            sql = "INSERT INTO credentials (username, password) VALUES (%s, %s)"
            val1 = ("kellyadams","kadam")
            val2 = ("malina24", "123")
            val3 = ("anglina", "293218")
            val4 = ("robert", "432")
            val5 = ("JA", "221")
            val6 = ("kate", "22345")
            val7 = ("John", "3456")
            val8 = ("Mark", "323556")
            val9 = ("Love", "hj432")
            val10 = ("Allah", "k76")
            mycursor.execute(sql,val1)
            mycursor.execute(sql, val2)
            mycursor.execute(sql, val3)
            mycursor.execute(sql, val4)
            mycursor.execute(sql, val5)
            mycursor.execute(sql, val6)
            mycursor.execute(sql, val7)
            mycursor.execute(sql, val8)
            mycursor.execute(sql, val9)
            mycursor.execute(sql, val10)
            mydb.commit()
            mycursor.close()
            mydb.close()
        except Exception as e:
            tkinter.messagebox.showinfo("Exception",e)

    # Method to insert data into created table professor when program runs first time
    def addDataToProfessor(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor=mydb.cursor()
            sql = "INSERT INTO professor (profName, profNum,cNum) VALUES (%s, %s,%s)"
            val1 = ("kelly Adams","P423","C219")
            val2=("Malina Kails","p455","C218")
            val3 = ("Anglina Jhones", "p96", "C129")
            val4=("Robert peterson","p98","C313")
            val5=("James Anderson","p233","C220")
            mycursor.execute(sql,val1)
            mycursor.execute(sql, val2)
            mycursor.execute(sql, val3)
            mycursor.execute(sql, val4)
            mycursor.execute(sql, val5)
            mydb.commit()
            mycursor.close()
            mydb.close()
        except Exception as e:
            tkinter.messagebox.showinfo("Exception",e)

    # Method to insert data into created table course when program runs first time
    def addDataToCourse(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root",
                                            passwd="", database="mydatabase")
            mycursor=mydb.cursor()
            sql = "INSERT INTO course (cNum, cName) VALUES (%s, %s)"
            val1 = ("C219","Computer Software")
            val2 = ("C218", "Civil Engineering")
            val3 = ("C129", "Android Development")
            val4 = ("C313", "Robotics")
            val5 = ("C220", "Computer Networking")

            mycursor.execute(sql,val1)
            mycursor.execute(sql, val2)
            mycursor.execute(sql, val3)
            mycursor.execute(sql, val4)
            mycursor.execute(sql, val5)
            mydb.commit()
            mycursor.close()
            mydb.close()
        except Exception as e:
            tkinter.messagebox.showinfo("Exception",e)

ob = tkk()