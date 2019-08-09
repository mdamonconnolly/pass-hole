import manager
from tkinter import *
from tkinter import ttk


topFrame = Frame(root).grid(row=0)
midFrame = Frame(root).grid(row=1)
bottomFrame = Frame(root).grid(row=2)

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master #master widget
        self.initUI()


    def initUI(self):

        # top row buttons 

        add_btn = Button(topFrame, text="Add")
        add_btn.grid(row=0, column=0, pady=(20))
        edit_btn = Button(topFrame, text="Edit")
        edit_btn.grid(row=0, column=1, pady=(20))
        del_btn = Button(topFrame, text="Delete")
        del_btn.grid(row=0, column=2, pady=(20))

        # tree table [ middle ]

        table = ttk.Treeview(midFrame, columns=("site","email","username","password"))
        table['show'] = 'headings'
        table.grid(columnspan=3)
        
        # bottom row buttons
        copy_email_btn = Button(bottomFrame, text="Copy Email")
        copy_email_btn.grid(row=4, column=0, pady=(20))
        copy_username_btn = Button(bottomFrame, text="Copy Username")
        copy_username_btn.grid(row=4, column=1, padx=(120), pady=(20))
        copy_pass_btn = Button(bottomFrame, text="Copy Pass")
        copy_pass_btn.grid(row=4, column=2, pady=(20))


app = Window(root) #instance class
root.mainloop() #init window
