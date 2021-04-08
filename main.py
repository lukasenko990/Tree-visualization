import tkinter
from tkinter import *
from tkinter import ttk
import time

class Node:
    key, left, right, up, window, obj, key_obj, arrow= None, None, None, None, None, None, None, None
    def move(self, x_distance, y_distance, x_velovity, y_velocity):
        coordinates = self.window.coords(self.obj)
        #print(coordinates)
        while coordinates[2]!=x_distance or coordinates[3]!=y_distance:
            coordinates = self.window.coords(self.obj)
            #print(coordinates)
            if coordinates[2]==x_distance:
                x_velovity=0
            if coordinates[3]==y_distance:
                y_velocity=0
            self.window.move(self.obj, x_velovity, y_velocity)
            self.window.move(self.key_obj, x_velovity, y_velocity)
            self.window.update()
            #time.sleep(0.01)
    def move_all(self, direction):
        if direction == "right":
            self.window.move(self.obj, -75, -50)
            self.window.move(self.arrow, -75, -50)
            self.window.move(self.key_obj, -75, -50)
            if self.left != None:
                self.left.move_all("right")
            if self.right != None:
                self.right.move_all("right")
        if direction == "left":
            self.window.move(self.obj, 75, -50)
            self.window.move(self.arrow, 75, -50)
            self.window.move(self.key_obj, 75, -50)
            if self.left != None:
                self.left.move_all("left")
            if self.right != None:
                self.right.move_all("left")


class BstTree:
    root = None
    window=None

    def insert_element(self, key):
        new_element = Node()
        new_element.key = key;
        new_element.window=self.window
        new_element.obj=new_element.window.create_oval(50, 50, 100, 100)
        new_element.key_obj=self.window.create_text(75,75, text=str(key))
        if self.root == None:
            new_element.move(400, 100, 1, 1)
            self.root = new_element
        else:
            current = self.root
            while not ((current.key <= key and current.right == None) or (current.key > key and current.left == None)):
                if current.key <= key:
                    coordinates = self.window.coords(current.obj)
                    text=self.window.create_text(coordinates[2] + 50, coordinates[3] - 25, text=str(key) + " >= " + str(current.key))
                    self.window.itemconfig(current.obj, fill='red')
                    self.window.update()
                    #time.sleep(1)
                    self.window.itemconfig(current.obj, fill='white')
                    self.window.delete(text)
                    self.window.update()
                    #time.sleep(1)
                    current = current.right
                else:
                    coordinates = self.window.coords(current.obj)
                    text=self.window.create_text(coordinates[2] - 100, coordinates[3] - 25, text=str(key) + " <= " + str(current.key))
                    self.window.itemconfig(current.obj, fill='red')
                    self.window.update()
                    #time.sleep(1)
                    self.window.itemconfig(current.obj, fill='white')
                    self.window.delete(text)
                    self.window.update()
                    #time.sleep(1)
                    current = current.left
            if current.key <= key:
                coordinates = self.window.coords(current.obj)
                text=self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                self.window.delete(text)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                #time.sleep(1)
                new_element.move(coordinates[2] + 75, coordinates[3] + 50, 1, 1)
                arrow=self.window.create_line(coordinates[2], (coordinates[3]+coordinates[1])/2,coordinates[2] + 50, coordinates[3], arrow=tkinter.LAST)
                new_element.arrow=arrow
                current.right = new_element
                new_element.up = current
            else:
                coordinates = self.window.coords(current.obj)
                text=self.window.create_text(coordinates[2] - 100, coordinates[3] - 25, text=str(key) + " <= " + str(current.key))
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                new_element.move(coordinates[2] - 75, coordinates[3] + 50, 1, 1)
                arrow=self.window.create_line(coordinates[0], (coordinates[3]+coordinates[1])/2, coordinates[2] - 100, coordinates[3], arrow=tkinter.LAST)
                new_element.arrow=arrow
                current.left = new_element
                new_element.up = current

    def find_element(self, key):
        current = self.root
        while current != None and current.key != key:
            if current.key < key:
                coordinates=self.window.coords(current.obj)
                self.window.itemconfig(current.obj, fill='red')
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.update()
                time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                time.sleep(1)
                current = current.right
            else:
                self.window.itemconfig(current.obj, fill='red')
                coordinates = self.window.coords(current.obj)
                text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
                self.window.update()
                time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                time.sleep(1)
                current = current.left
        if current == None:
            text = self.window.create_text(50, 50, text="Node not found")
            self.window.update()
            time.sleep(1)
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
            return None
        else:
            text = self.window.create_text(50, 50, text="Node found")
            self.window.itemconfig(current.obj, fill='red')
            self.window.update()
            time.sleep(1)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
            return current

    def show_min(self):
        if self.root == None:
            text=self.window.create_text(50, 50, text="Tree is empty!")
            self.window.update()
            time.sleep(1)
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
        else:
            current = self.root
            while current.left != None:
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                time.sleep(1)
                current = current.left
            self.window.itemconfig(current.obj, fill='red')
            text = self.window.create_text(100, 50, text="Minimum key in this tree is: " + str(current.key))
            self.window.update()
            time.sleep(5)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
            print(current.key)

    def show_max(self):
        if self.root == None:
            text = self.window.create_text(50, 50, text="Tree is empty!")
            self.window.update()
            time.sleep(1)
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
        else:
            current = self.root
            while current.right != None:
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                time.sleep(1)
                current = current.right
            self.window.itemconfig(current.obj, fill='red')
            text = self.window.create_text(100, 50, text="Maximum key in this tree is: " + str(current.key))
            self.window.update()
            time.sleep(5)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
            print(current.key)
    def delete_node(self, key):
        current=self.find_element(key)
        if current == None:
            return None
        else:
            if current.left == None and current.right == None:
                if current == self.root:
                    self.window.delete(self.root.obj)
                    self.window.delete(self.root.key_obj)
                    self.root = None
                else:
                    self.window.delete(current.obj)
                    self.window.delete(current.key_obj)
                    self.window.delete(current.arrow)
                    if current == current.up.left:
                        current.up.left = None
                    else:
                        current.up.right = None
            elif current.left == None or current.right == None:
                if current.left == None:
                    current.right.move_all("right")
                    self.window.delete(current.right.arrow)
                    current.right.arrow = current.arrow
                    self.window.delete(current.obj)
                    self.window.delete(current.key_obj)
                else:
                    current.left.move_all("left")
                    self.window.delete(current.left.arrow)
                    current.left.arrow = current.arrow
                    self.window.delete(current.obj)
                    self.window.delete(current.key_obj)


#keyentry=StringVar()
def Insert():
    #print(treemenu.get())
    drzewo.insert_element(int(keyentry.get()))
def Max():
    drzewo.show_max()
def Min():
    drzewo.show_min()
def Find():
    drzewo.find_element(int(keyentry.get()))
def Delete():
    drzewo.delete_node(int(keyentry.get()))
nazwa="asdsa"
slectedTree = None
master = Tk()
master.title('Tree operations visualization')
master.maxsize(800,600)
window = Canvas(master, width=800, height=600)
uiframe = Frame(master, width=800, height=100, bg='grey')
uiframe.grid(row=0, column=0, padx=10, pady=5)
Label(uiframe, text="Tree:", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
treemenu = ttk.Combobox(uiframe, values=['Binary Search Tree', 'Binary Tree'])
treemenu.grid(row=0, column=1, padx=5, pady=5)
treemenu.current(0)
drzewo = BstTree()
drzewo.window=window
Button(uiframe, text="Insert", command=Insert, bg='red').grid(row=0, column=2, padx=5, pady=5)
Button(uiframe, text="Max", command=Max, bg='red').grid(row=1, column=3, padx=5, pady=5)
Button(uiframe, text="Min", command=Min, bg='red').grid(row=1, column=2, padx=5, pady=5)
Button(uiframe, text="Find", command=Find, bg='red').grid(row=2, column=2, padx=5, pady=5)
Button(uiframe, text="Delete", command=Delete, bg='red').grid(row=0, column=3, padx=5, pady=5)
keyentry=Entry(uiframe)
keyentry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Label(uiframe, text="Key:", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)

uiframe.pack()
window.pack()
"""drzewo.show_min()
drzewo.insert_element(9)
drzewo.insert_element(0)
drzewo.insert_element(11)
drzewo.insert_element(18)
drzewo.insert_element(25)
drzewo.insert_element(3)
drzewo.insert_element(1)
drzewo.show_min()
drzewo.show_max()
"""
mainloop()