import manager
from tkinter import *
from tkinter import ttk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master #master widget
        self.grid()



root = Tk() #root window
root.title("Passhole ui v.01")
root.minsize(800,600) #set min size

tree = ttk.Treeview(root)
tree.grid(padx=(20,20))
tree.grid(pady=(50,20))


tree["columns"]=("one","two", "three", "four")
tree.column("one", width=150)
tree.column("two", width=150)
tree.column("three", width=150)
tree.column("four", width=150)

tree.insert("", 0, text="Site", values=("1A","1B"))
tree.insert("", 1, text="Email", values=("2A","2B"))





app = Window(root) #instance class
root.mainloop() #init window
