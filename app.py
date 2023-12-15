from tkinter import *
from tkinter import ttk
import BST
import RBT
import Splay
import BTree


def insert():
    if tree_menu.get() == "Binary Search Tree":
        BST.insert_element(int(key_entry.get()))
    elif tree_menu.get() == "Red-Black Tree":
        RBT.insert_key(int(key_entry.get()))
    elif tree_menu.get() == "Splay Tree":
        Splay.insert_key(int(key_entry.get()))
    elif tree_menu.get() == "B-Tree":
        B_tree.insert_element(int(key_entry.get()))


def max():
    if tree_menu.get() == "Binary Search Tree":
        BST.show_max()
    elif tree_menu.get() == "Red-Black Tree":
        RBT.show_max()
    elif tree_menu.get() == "Splay Tree":
        Splay.show_max()
    elif tree_menu.get() == "B-Tree":
        B_tree.show_max()


def min():
    if tree_menu.get() == "Binary Search Tree":
        BST.show_min()
    elif tree_menu.get() == "Red-Black Tree":
        RBT.show_min()
    elif tree_menu.get() == "Splay Tree":
        Splay.show_min()
    elif tree_menu.get() == "B-Tree":
        B_tree.show_min()


def find():
    if tree_menu.get() == "Binary Search Tree":
        BST.find_element(int(key_entry.get()))
    elif tree_menu.get() == "Red-Black Tree":
        RBT.find_element(int(key_entry.get()))
    elif tree_menu.get() == "Splay Tree":
        Splay.splay_find_element(int(key_entry.get()))
    elif tree_menu.get() == "B-Tree":
        B_tree.find_element(int(key_entry.get()))


def delete():
    if tree_menu.get() == "Binary Search Tree":
        BST.delete_node(int(key_entry.get()))
    elif tree_menu.get() == "Red-Black Tree":
        RBT.delete_node(int(key_entry.get()))
    elif tree_menu.get() == "Splay Tree":
        Splay.delete_node(int(key_entry.get()))
    elif tree_menu.get() == "B-Tree":
        B_tree.delete_node(int(key_entry.get()))


def reset():
    window.delete("all")
    BST.root = None
    RBT.root = None
    Splay.root = None
    B_tree.root = None


selectedTree = None
master = Tk()
master.title('Tree operations visualization')
master.maxsize(800, 600)
window = Canvas(master, width=800, height=600)
ui_frame = Frame(master, width=800, height=100, bg='grey')
ui_frame.grid(row=0, column=0, padx=10, pady=5)
Label(ui_frame, text="Tree:", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
tree_menu = ttk.Combobox(ui_frame, values=['Binary Search Tree', 'Red-Black Tree', 'Splay Tree', 'B-Tree'])
tree_menu.grid(row=0, column=1, padx=5, pady=5)
tree_menu.current(0)

# Buttons initialize
Button(ui_frame, text="Insert", command=insert, bg='red').grid(row=0, column=2, padx=5, pady=5)
Button(ui_frame, text="Max", command=max, bg='red').grid(row=1, column=3, padx=5, pady=5)
Button(ui_frame, text="Min", command=min, bg='red').grid(row=1, column=2, padx=5, pady=5)
Button(ui_frame, text="Find", command=find, bg='red').grid(row=2, column=2, padx=5, pady=5)
Button(ui_frame, text="Delete", command=delete, bg='red').grid(row=0, column=3, padx=5, pady=5)
Button(ui_frame, text="Reset", command=reset, bg='red').grid(row=2, column=3, padx=5, pady=5)
key_entry=Entry(ui_frame)
key_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Label(ui_frame, text="Key:", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)

ui_frame.pack()
window.pack()

BST = BST.BstTree()
BST.window = window
RBT = RBT.RedBlackTree()
RBT.window = window
Splay = Splay.SplayTree()
Splay.window = window
B_tree = BTree.BTree()
B_tree.window = window


mainloop()
