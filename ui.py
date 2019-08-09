import manager
from tkinter import *
from tkinter import ttk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master #master widget
        self.grid()
        


    self.master = master #master widget
    self.grid()

    
add_btn = Button(master, text="Add login", command=callback)

root = Tk() #root window
root.title("Passhole ui v.01")
root.minsize(800,600) #set min size

tree = ttk.Treeview(root, columns=("site","email","username","pasword"))
tree['show'] = 'headings'
tree.grid(padx=(20,20))
tree.grid(pady=(50,20))


app = Window(root) #instance class
root.mainloop() #init window
