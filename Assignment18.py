#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
#import tkinter
#from tkinter import *
#d={'raju':9876543210,'unknown':9785643210,'mani':7865241202,'abc':9631294546,'def':9708994683,'hij':123,'jkl':456}
#root=Tk()
#s=Scrollbar(root)
#s.pack(side=RIGHT,fill=Y)
#l=Listbox(root,yscrollcommand=s.set)
#for key in d.values():
#    l.insert(END,'this is the list no'+str(key))
#l.pack(side=LEFT,fill=BOTH)
#s.config(command=l.yview())
#root.mainloop()
#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.
import tkinter
from tkinter import *
d={'raju':9876543210,'unknown':9785643210,'mani':7865241202,'abc':9631294546,'def':9708994683,'hij':123,'jkl':456}

def insert():
    k = e1.get()
    v = e2.get()
    d[k]=v
    l.insert(END,k)
    print(d)
root=Tk()

e1 = Entry(root)
e1.pack()
e2 = Entry(root)
e2.pack()
b=Button(root,text="insert",command=insert)
b.pack()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
    l.insert(END,'this is the list no'+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
root.mainloop()
