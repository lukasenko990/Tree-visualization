import tkinter
from tkinter import *
from tkinter import ttk
import time
import BST
import RBT
import Splay
import BTree
#keyentry=StringVar()
def Insert():
    if treemenu.get() == "Binary Search Tree":
        drzewo.insert_element(int(keyentry.get()))
    elif treemenu.get() == "Red-Black Tree":
        drzewo2.insert_key(int(keyentry.get()))
    elif treemenu.get() == "Splay Tree":
        drzewo3.insert_key(int(keyentry.get()))
    elif treemenu.get() == "B-Tree":
        drzewo4.insert_element(int(keyentry.get()))
def Max():
    if treemenu.get() == "Binary Search Tree":
        drzewo.show_max()
    elif treemenu.get() == "Red-Black Tree":
        drzewo2.show_max()
    elif treemenu.get() == "Splay Tree":
        drzewo3.show_max()
    elif treemenu.get() == "B-Tree":
        drzewo4.show_max()
def Min():
    if treemenu.get() == "Binary Search Tree":
        drzewo.show_min()
    elif treemenu.get() == "Red-Black Tree":
        drzewo2.show_min()
    elif treemenu.get() == "Splay Tree":
        drzewo3.show_min()
    elif treemenu.get() == "B-Tree":
        drzewo4.show_min()
def Find():
    if treemenu.get() == "Binary Search Tree":
        drzewo.find_element(int(keyentry.get()))
    elif treemenu.get() == "Red-Black Tree":
        drzewo2.find_element(int(keyentry.get()))
    elif treemenu.get() == "Splay Tree":
        drzewo3.splay_find_element(int(keyentry.get()))
    elif treemenu.get() == "B-Tree":
        drzewo4.find_element(int(keyentry.get()))
def Delete():
    if treemenu.get() == "Binary Search Tree":
        drzewo.delete_node(int(keyentry.get()))
    elif treemenu.get() == "Red-Black Tree":
        drzewo2.delete_node(int(keyentry.get()))
    elif treemenu.get() == "Splay Tree":
        drzewo3.delete_node(int(keyentry.get()))
    elif treemenu.get() == "B-Tree":
        drzewo4.delete_node(int(keyentry.get()))
def Reset():
    window.delete("all")
    drzewo.root = None
    drzewo2.root = None
    drzewo3.root = None
    drzewo4.root = None
nazwa="asdsa"
slectedTree = None
master = Tk()
master.title('Tree operations visualization')
master.maxsize(800,600)
window = Canvas(master, width=800, height=600)
uiframe = Frame(master, width=800, height=100, bg='grey')
uiframe.grid(row=0, column=0, padx=10, pady=5)
Label(uiframe, text="Tree:", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
treemenu = ttk.Combobox(uiframe, values=['Binary Search Tree', 'Red-Black Tree', 'Splay Tree', 'B-Tree'])
treemenu.grid(row=0, column=1, padx=5, pady=5)
treemenu.current(0)
Button(uiframe, text="Insert", command=Insert, bg='red').grid(row=0, column=2, padx=5, pady=5)
Button(uiframe, text="Max", command=Max, bg='red').grid(row=1, column=3, padx=5, pady=5)
Button(uiframe, text="Min", command=Min, bg='red').grid(row=1, column=2, padx=5, pady=5)
Button(uiframe, text="Find", command=Find, bg='red').grid(row=2, column=2, padx=5, pady=5)
Button(uiframe, text="Delete", command=Delete, bg='red').grid(row=0, column=3, padx=5, pady=5)
Button(uiframe, text="Reset", command=Reset, bg='red').grid(row=2, column=3, padx=5, pady=5)
keyentry=Entry(uiframe)
keyentry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Label(uiframe, text="Key:", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)

uiframe.pack()
window.pack()

drzewo = BST.BstTree()
drzewo.window=window
drzewo2 = RBT.RedBlackTree()
drzewo2.window=window
drzewo3 = Splay.SplayTree()
drzewo3.window=window
drzewo4 = BTree.BTree()
drzewo4.window = window


#drzewo2.insert_key(50)
#drzewo2.insert_key(20)
#drzewo2.insert_key(15)
#drzewo2.insert_key(65)
#drzewo2.insert_key(55)
#drzewo2.insert_key(70)
#drzewo2.insert_key(68)
#drzewo2.insert_key(80)
#drzewo2.insert_key(90)
#drzewo2.delete_node(50)
#print("asd:"+str(drzewo2.root.right.right.left.key))
#drzewo2.delete_node(65)

#print(drzewo2.root.right.left.right.key)

#drzewo2.insert_key(40)
#print(drzewo2.root.right.right.left.right.key)
drzewo4.insert_element(1)
drzewo4.insert_element(2)
drzewo4.insert_element(3)
drzewo4.insert_element(4)
drzewo4.insert_element(5)
drzewo4.insert_element(6)
drzewo4.insert_element(7)
drzewo4.insert_element(8)
drzewo4.insert_element(9)
drzewo4.insert_element(11)
drzewo4.insert_element(12)
drzewo4.insert_element(13)
drzewo4.insert_element(14)
drzewo4.insert_element(15)
drzewo4.insert_element(16)
drzewo4.insert_element(17)
drzewo4.insert_element(18)
drzewo4.insert_element(19)
drzewo4.insert_element(21)
drzewo4.insert_element(22)
drzewo4.insert_element(23)
drzewo4.insert_element(24)
drzewo4.insert_element(25)
drzewo4.insert_element(26)
drzewo4.insert_element(27)
drzewo4.insert_element(28)
drzewo4.delete_node(6)
mainloop()