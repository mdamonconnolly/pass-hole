import manager
import add_entry_dialog
from tkinter import *
from tkinter import ttk
import pyperclip

#Constants
VERSION = '0.8'


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
        self.current_row = self.table.focus()
        print(self.table.item(self.current_row))

        self.dialog_popup = add_entry_dialog.addDialog(self.master, self.manager, main=self)
        
            
    def edit_func(self):
        self.current_row = self.table.focus()
        if  self.table.item(self.current_row)['values'] == '':
            print("Nothing selected..")
        else:
            entries = [self.table.item(self.current_row)['values'][0], 
                    self.table.item(self.current_row)['values'][1],
                    self.table.item(self.current_row)['values'][2],
                    self.table.item(self.current_row)['values'][3]]
            self.dialog_popup = add_entry_dialog.addDialog(self.master, self.manager, main=self, entry=entries)
            print('Edited')
        
    def populate_table(self):
        self.table.delete(*self.table.get_children())
        entry_dict = self.manager.get_all_entries()

        print(entry_dict.items)
        
        for site, entry in entry_dict.items():
            self.table.insert('','end',text="site.com", values=(site, entry[0],entry[1], entry[2] ))

    def del_func(self):
        current_item = self.table.focus()
        try:
            self.manager.delete_entry((self.table.item(current_item)["values"][0]))
            self.populate_table()

        except Exception as e:
            print("Error deleting item. Exception : {0}".format(e))
            return 0
        return 1

    def copy_email(self):
        current_item = self.table.focus()
        pyperclip.copy(self.table.item(current_item)["values"][1])
        print('Copied email of selected row')

    def copy_user(self):
        current_item = self.table.focus()
        pyperclip.copy(self.table.item(current_item)["values"][2])
        print('Copied username of selected row')

    def copy_pass(self):
        current_item = self.table.focus()
        pyperclip.copy(self.table.item(current_item)["values"][3])
        print('Copied password of selected row')


if __name__ == '__main__':

    m = manager.Manager()

    root = Tk() #root window
    root.title("Passhole ui v{0}".format(VERSION))
    root.minsize(850,400)

    topFrame = Frame(root).grid(row=0)
    midFrame = Frame(root).grid(row=1)
    bottomFrame = Frame(root).grid(row=2)

    app = Window(root, m) #instance class
    root.mainloop() #init window
