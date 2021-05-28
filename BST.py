import tkinter
from tkinter import *
from tkinter import ttk
import time

class Node:
    key, left, right, up, window, obj, key_obj, arrow= None, None, None, None, None, None, None, None
    def move(self, x_distance, y_distance, x_velovity, y_velocity):
        coordinates = self.window.coords(self.obj)
        while coordinates[2]!=x_distance or coordinates[3]!=y_distance:
            coordinates = self.window.coords(self.obj)
            if coordinates[2]==x_distance:
                x_velovity=0
            if coordinates[3]==y_distance:
                y_velocity=0
            self.window.move(self.obj, x_velovity, y_velocity)
            self.window.move(self.key_obj, x_velovity, y_velocity)
            self.window.update()
            time.sleep(0.01)
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
                    time.sleep(1)
                    self.window.itemconfig(current.obj, fill='white')
                    self.window.delete(text)
                    self.window.update()
                    time.sleep(1)
                    current = current.right
                else:
                    coordinates = self.window.coords(current.obj)
                    text=self.window.create_text(coordinates[2] - 100, coordinates[3] - 25, text=str(key) + " <= " + str(current.key))
                    self.window.itemconfig(current.obj, fill='red')
                    self.window.update()
                    time.sleep(1)
                    self.window.itemconfig(current.obj, fill='white')
                    self.window.delete(text)
                    self.window.update()
                    time.sleep(1)
                    current = current.left
            if current.key <= key:
                coordinates = self.window.coords(current.obj)
                text=self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                time.sleep(1)
                self.window.delete(text)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                time.sleep(1)
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
                time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                time.sleep(1)
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

    def find_consequence(self, node):
        if node.right == None:
            return None
        else:
            current=node.right
            while current.left != None:
                current=current.left
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
            time.sleep(3)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            time.sleep(1)

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
            time.sleep(3)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            time.sleep(1)
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
                    if current == self.root:
                        self.root=current.right
                    else:
                        if current.up.left == current:
                            current.up.left=current.right
                            current.right.up=current.up
                        else:
                            current.up.right=current.right
                            current.right.up=current.up
                else:
                    current.left.move_all("left")
                    self.window.delete(current.left.arrow)
                    current.left.arrow = current.arrow
                    self.window.delete(current.obj)
                    self.window.delete(current.key_obj)
                    if current == self.root:
                        self.root = current.left
                    else:
                        if current.up.left == current:
                            current.up.left=current.left
                            current.left.up=current.up
                        else:
                            current.up.right=current.left
                            current.left.up=current.up
            else:
                consequent=self.find_consequence(current)
                k=consequent.key
                self.window.itemconfigure(current.key_obj, text=str(k))
                self.window.itemconfigure(consequent.key_obj, text=str(current.key))
                self.delete_node(consequent.key)
                current.key=k






