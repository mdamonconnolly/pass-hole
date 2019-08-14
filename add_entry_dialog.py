import manager
from tkinter import *
from tkinter import ttk

class addDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.resizable(False, False)

        vertical_frame = Frame(top)
        vertical_frame.pack(side=TOP)
        label_frame = Frame(vertical_frame)
        label_frame.pack(side=LEFT, fill=BOTH, expand=FALSE)
        field_frame = Frame(vertical_frame)
        field_frame.pack(side=RIGHT, fill=BOTH, expand=FALSE)
        button_frame=Frame(top)
        button_frame.pack(side=BOTTOM, fill=BOTH)

        # labels
        site_label = Label(label_frame, text="Enter website")
        site_label.pack(pady=10, padx=10)
        email_label = Label(label_frame, text="Enter email")
        email_label.pack(pady=10, padx=10)
        user_label = Label(label_frame, text="Enter username")
        user_label.pack(pady=10, padx=10)
        pass_label = Label(label_frame, text="Enter password")
        pass_label.pack(pady=10, padx=10)

        # entries
        self.site = Entry(field_frame, width=30)
        self.site.pack(pady=10, padx=10)
        self.email = Entry(field_frame, width=30)
        self.email.pack(pady=10, padx=10)
        self.user = Entry(field_frame, width=30)
        self.user.pack(pady=10, padx=10)
        self.password = Entry(field_frame, width=30)
        self.password.pack(pady=10, padx=10)

        #buttons
        self.enterDetails_btn = Button(button_frame, text="Add new entry", width=15, command=self.addEntry).pack(side=LEFT, pady=10, padx=20)    
        self.cancel_btn = Button(button_frame, text="Cancel", width=15, command=self.exit).pack(side=RIGHT, pady=10, padx=20)

    def addEntry(self):
        entered_site = str(self.site.get())
        entered_email = str(self.email.get())
        entered_user = str(self.user.get())
        entered_password = str(self.password.get())
        self.top.destroy()
        
        print(entered_site, entered_email, entered_user, entered_password)

        
    def exit(self):
        self.top.destroy()

#TODO 
# close popup dialog on button click
# store fields 1-4 as strings
# on popup closure, display added variables as a new row in the table



