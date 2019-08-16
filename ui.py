import manager
import add_entry_dialog
from tkinter import *
from tkinter import ttk
import pyperclip

#Constants
version = '0.3'

#Grid.rowconfigure(Grid, row=0, weight=1)
#Grid.columnconfigure(Grid, row=0, weight=1)


class Window(Frame):


    def __init__(self, master=None, manager=None):
        self.manager = manager
        Frame.__init__(self, master)

        self.master = master #master widget
        self.initUI()
        self.populate_table()

    def initUI(self):

        # top row buttons 

        add_btn = Button(topFrame, text="Add", command=self.add_func)
        add_btn.grid(row=0, column=0, sticky=NSEW, pady=20, padx=20)
        edit_btn = Button(topFrame, text="Edit", command=self.edit_func)
        edit_btn.grid(row=0, column=1, sticky=NSEW, pady=20, padx=20)
        del_btn = Button(topFrame, text="Delete", command=self.del_func)
        del_btn.grid(row=0, column=2, sticky=NSEW, pady=20, padx=20)

        # tree table [ middle ]
        self.table = ttk.Treeview(midFrame, columns=("site","email","username","password"))

        self.table.column("0", width=200, minwidth=100,)
        self.table.column("1", width=200, minwidth=100)
        self.table.column("2", width=200, minwidth=100)
        self.table.column("3", width=200, minwidth=100)

        self.table['show'] = 'headings'
        self.table.heading('0',text='Site')
        self.table.heading('1',text='Email')
        self.table.heading('2',text='Username')
        self.table.heading('3',text='Password')

        self.table.grid(columnspan=3, pady=20, padx=20)
        
        # bottom row buttons
        copy_email_btn = Button(bottomFrame, text="Copy Email", command=self.copy_email)
        copy_email_btn.grid(row=4, column=0, sticky=NSEW, pady=20, padx=20)
        copy_username_btn = Button(bottomFrame, text="Copy Username", command=self.copy_user)
        copy_username_btn.grid(row=4, column=1, sticky=NSEW, pady=20, padx=20)
        copy_pass_btn = Button(bottomFrame, text="Copy Pass", command=self.copy_pass)
        copy_pass_btn.grid(row=4, column=2, sticky=NSEW, pady=20, padx=20)
        
    def add_func(self):
        add_dialog_popup = add_entry_dialog.addDialog(self.master, self.manager)
        print("added login\n")

    def edit_func(self):
        print("edited login\n")

    def del_func(self):
        print("deleted login\n")

    def copy_email(self):
        print("copy email\n")

    def copy_user(self):
        print("copy username\n")

    def copy_pass(self):
        print("copy password\n")

    def populate_table(self):
        '''TODO: Get entries from manager and loop through them inserting them to table.'''
        self.table.insert('','end',text='site.com', values=('site','email','username','password'))
        self.table.insert('','end',text='Ebay', values=('SecondSite', 'caro@damon.com', 'carochicky', 'caropass'))
        print("table_populated")


if __name__ == '__main__':

    m = manager.Manager()

    root = Tk() #root window
    root.title("Passhole ui v{0}".format(version))
    root.minsize(850,400)

    '''TODO: Are these needed now?'''
    #Grid.rowconfigure(Grid, row=0, weight=1)
    #Grid.columnconfigure(Grid, row=0, weight=1)

    topFrame = Frame(root).grid(row=0)
    midFrame = Frame(root).grid(row=1)
    bottomFrame = Frame(root).grid(row=2)

    app = Window(root, m) #instance class
    root.mainloop() #init window
