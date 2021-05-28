from tkinter import *
from tkinter import ttk
import BST
import RBT
import Splay
import BTree
def Insert():
    if treemenu.get() == "Binary Search Tree":
        BST.insert_element(int(keyentry.get()))
    elif treemenu.get() == "Red-Black Tree":
        RBT.insert_key(int(keyentry.get()))
    elif treemenu.get() == "Splay Tree":
        Splay.insert_key(int(keyentry.get()))
    elif treemenu.get() == "B-Tree":
        B_tree.insert_element(int(keyentry.get()))
def Max():
    if treemenu.get() == "Binary Search Tree":
        BST.show_max()
    elif treemenu.get() == "Red-Black Tree":
        RBT.show_max()
    elif treemenu.get() == "Splay Tree":
        Splay.show_max()
    elif treemenu.get() == "B-Tree":
        B_tree.show_max()
def Min():
    if treemenu.get() == "Binary Search Tree":
        BST.show_min()
    elif treemenu.get() == "Red-Black Tree":
        RBT.show_min()
    elif treemenu.get() == "Splay Tree":
        Splay.show_min()
    elif treemenu.get() == "B-Tree":
        B_tree.show_min()
def Find():
    if treemenu.get() == "Binary Search Tree":
        BST.find_element(int(keyentry.get()))
    elif treemenu.get() == "Red-Black Tree":
        RBT.find_element(int(keyentry.get()))
    elif treemenu.get() == "Splay Tree":
        Splay.splay_find_element(int(keyentry.get()))
    elif treemenu.get() == "B-Tree":
        B_tree.find_element(int(keyentry.get()))
def Delete():
    if treemenu.get() == "Binary Search Tree":
        BST.delete_node(int(keyentry.get()))
    elif treemenu.get() == "Red-Black Tree":
        RBT.delete_node(int(keyentry.get()))
    elif treemenu.get() == "Splay Tree":
        Splay.delete_node(int(keyentry.get()))
    elif treemenu.get() == "B-Tree":
        B_tree.delete_node(int(keyentry.get()))
def Reset():
    window.delete("all")
    BST.root = None
    RBT.root = None
    Splay.root = None
    B_tree.root = None
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

BST = BST.BstTree()
BST.window=window
RBT = RBT.RedBlackTree()
RBT.window=window
Splay = Splay.SplayTree()
Splay.window=window
B_tree = BTree.BTree()
B_tree.window = window


mainloop()