import manager
from tkinter import *
from tkinter import ttk

class addDialog:
    def __init__(self, parent, manager, main, entry=None):

        self.manager = manager
        top = self.top = Toplevel(parent)
        top.resizable(False, False)
        self.parent = main
        self.entry = entry

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
        if self.entry != None:
            self.enterDetails_btn = Button(button_frame, text="Edit Entry", width=15, command=self.editEntry).pack(side=LEFT, pady=10, padx=20)
        else:
            self.enterDetails_btn = Button(button_frame, text="Add new entry", width=15, command=self.addEntry).pack(side=LEFT, pady=10, padx=20)

        self.cancel_btn = Button(button_frame, text="Cancel", width=15, command=self.exit_dialog).pack(side=RIGHT, pady=10, padx=20)

        # prefill fields for edit dialog

        if self.entry != None:
            self.site.insert(0, str(entry[0]))
            self.email.insert(0, str(entry[1]))
            self.user.insert(0, str(entry[2]))
            self.password.insert(0, str(entry[3]))
   


    def addEntry(self):
        self.entered_site = str(self.site.get())
        self.entered_email = str(self.email.get())
        self.entered_user = str(self.user.get())
        self.entered_password = str(self.password.get())

        '''use manager to create entries'''
        try:
            self.manager.add_entry(self.entered_site, self.entered_email, self.entered_user, self.entered_password)
        except Exception as e:
            print('Adding to manager failed. Exception: {0}'.format(e))

        self.top.destroy()
        self.parent.populate_table()
    
    def editEntry(self):
        try:
            self.manager.edit_entry(self.entry[0], self.entry[1], self.entry[2], self.entry[3])
            
            print('successfully edited existing entry')

        except Exception as e:
            print('Editing entry failed ; Exception: {0}'.format(e))

        self.top.destroy()
        
    def exit_dialog(self):
        self.top.destroy()

#TODO 
# if entry is passed in to constructor, fields should be auto-filled with this. See issue #03



