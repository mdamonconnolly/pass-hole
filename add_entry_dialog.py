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

        site_label = Label(label_frame, text="Enter website").pack(side=LEFT, pady=10, padx=60)
        email_label = Label(label_frame, text="Enter email").pack(side=LEFT, pady=10, padx=50)
        user_label = Label(label_frame, text="Enter username").pack(side=RIGHT, pady=10, padx=60)
        pass_label = Label(label_frame, text="Enter password").pack(side=RIGHT, pady=10, padx=50)


        self.site = Entry(field_frame, width=30).pack(side=LEFT, pady=10, padx=5)
        self.email = Entry(field_frame, width=30).pack(side=LEFT, pady=10, padx=5)
        self.user = Entry(field_frame, width=30).pack(side=RIGHT, pady=10, padx=5)
        self.password = Entry(field_frame, width=30).pack(side=RIGHT, pady=10, padx=5)
    

        self.enterDetails_btn = Button(button_frame, text="Add new entry", width=15, command=self.addEntry).pack(side=LEFT, pady=10, padx=40)    
        self.cancel_btn = Button(button_frame, text="Cancel", width=15).pack(side=RIGHT, pady=10, padx=40)

    def addEntry(self):
        #entered_site = self.site.get()
        #print(entered_site)
        pass
    


#TODO 
# close popup dialog on button click
# store fields 1-4 as strings
# on popup closure, display added variables as a new row in the table



