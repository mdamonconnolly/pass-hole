import manager
from tkinter import *
from tkinter import ttk

class addDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.resizable(False, False)

        label_frame = Frame(top)
        label_frame.pack(side=TOP, fill=BOTH, expand=FALSE)

        field_frame = Frame(top)
        field_frame.pack(fill=BOTH)

        button_frame=Frame(top)
        button_frame.pack(side=BOTTOM)


        site_label = Label(label_frame, text="Enter website")
        site_label.pack(side=LEFT, pady=10, padx=60)

        email_label = Label(label_frame, text="Enter email")
        email_label.pack(side=LEFT, pady=10, padx=50)

        user_label = Label(label_frame, text="Enter username")
        user_label.pack(side=LEFT, pady=10, padx=60)

        pass_label = Label(label_frame, text="Enter password")
        pass_label.pack(side=RIGHT, pady=10, padx=50)

        

        self.site = Entry(field_frame, width=30)
        self.site.pack(side=LEFT, pady=10, padx=5)

        self.email = Entry(field_frame, width=30)
        self.email.pack(side=LEFT, pady=10, padx=5)

        self.user = Entry(field_frame, width=30)
        self.user.pack(side=RIGHT, pady=10, padx=5)

        self.password = Entry(field_frame, width=30)
        self.password.pack(side=RIGHT, pady=10, padx=5)
    

        self.enterDetails_btn = Button(button_frame, text="Add new entry", width=15, command=self.addEntry).pack(side=LEFT, pady=10, padx=40)    
        self.cancel_btn = Button(button_frame, text="Cancel", width=15).pack(side=RIGHT, pady=10, padx=40)


    def addEntry(self):
        entered_site = str(self.site.get())
        entered_email = str(self.email.get())
        entered_user = str(self.user.get())
        entered_password = str(self.password.get())

        print(entered_site, entered_email, entered_user, entered_password)


#TODO 
# close popup dialog on button click
# store fields 1-4 as strings
# on popup closure, display added variables as a new row in the table



