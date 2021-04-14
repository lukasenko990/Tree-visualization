import tkinter
from tkinter import *
from tkinter import ttk
import time
class Node:
    key, left, right, up, window, obj, key_obj, arrow = None, None, None, None, None, None, None, None
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
    def move_all(self, direction, child):
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
        if direction == "left-up":
            self.window.move(self.obj, -75, -50)
            self.window.move(self.arrow, -75, -50)
            self.window.move(self.key_obj, -75, -50)
            coords = self.window.coords(self.arrow)
            if self.up == None:
                self.window.delete(self.arrow)
                self.arrow = None
            elif coords[2] > coords[0] and self != None and self == self.up.left:
                self.window.delete(self.arrow)
                arrow = self.window.create_line(coords[0]+100, coords[1], coords[2], coords[3], arrow=tkinter.LAST)
                self.arrow=arrow
            if self.right != None:
                self.right.move_all("left-up", True)
            if self.left != None and child == True:
                self.left.move_all("left-up", True)
        if direction == "left-down":
            self.window.move(self.obj, -75, 50)
            self.window.move(self.key_obj, -75, 50)
            print(self.key)
            #time.sleep(3)
            if self.arrow != None:
                self.window.move(self.arrow, -75, 50)
                coords = self.window.coords(self.arrow)
                print(coords)
                if coords[2] > coords[0] and self.up != None and self == self.up.left:
                    self.window.delete(self.arrow)
                    arrow = self.window.create_line(coords[0]+100, coords[1], coords[2], coords[3], arrow=tkinter.LAST)
                    self.arrow = arrow
            else:
                coordinates = self.window.coords(self.obj)
                arrow = self.window.create_line(350, 75,coordinates[2]-25, coordinates[3]-50, arrow=tkinter.LAST)
                self.arrow=arrow
            if self.left != None:
                self.left.move_all("left-down", True)
            if self.right != None and child == True:
                self.right.move_all("left-down", True)
        if direction == "right-up":
            self.window.move(self.obj, 75, -50)
            self.window.move(self.arrow, 75, -50)
            self.window.move(self.key_obj, 75, -50)
            coords = self.window.coords(self.arrow)
            if self.up == None:
                self.window.delete(self.arrow)
                self.arrow = None
            elif coords[2] < coords[0] and self == self.up.right:
                self.window.delete(self.arrow)
                arrow = self.window.create_line(coords[0]-100, coords[1], coords[2], coords[3], arrow=tkinter.LAST)
                self.arrow = arrow
            if self.left != None:
                self.left.move_all("right-up", True)
            if self.right != None and child == True:
                self.right.move_all("right-up", True)
        if direction == "right-down":
            self.window.move(self.obj, 75, 50)
            self.window.move(self.key_obj, 75, 50)
            if self.arrow != None:
                self.window.move(self.arrow, 75, 50)
                coords = self.window.coords(self.arrow)
                if coords[2] < coords[0] and self == self.up.right:
                    self.window.delete(self.arrow)
                    arrow = self.window.create_line(coords[0]-100, coords[1], coords[2], coords[3], arrow=tkinter.LAST)
                    self.arrow = arrow
            else:
                coordinates = self.window.coords(self.obj)
                arrow = self.window.create_line(400, 75, coordinates[2] - 25, coordinates[3] - 50, arrow=tkinter.LAST)
                self.arrow = arrow
            if self.right != None:
                print(self.right.key)
                self.right.move_all("right-down", True)
            if self.left != None and child == True:
                self.left.move_all("right-down", True)
            self.window.update()


class SplayTree:
    window = None
    root = None
    def rotate_left(self, node):
        #time.sleep(2)
        if node == self.root:
            self.root=node.right
        elif node == node.up.left:
            node.up.left = node.right
        else:
            node.up.right=node.right
        node.right.up = node.up
        node.up = node.right
        node.right = node.up.left
        if node.up.left != None:
            node.up.left.up = node
            self.window.delete(node.up.left.arrow)
            coordinates = self.window.coords(node.up.left.obj)
            arrow = self.window.create_line(coordinates[2]-75, coordinates[3]-75, coordinates[2]-25, coordinates[3]-50, arrow=tkinter.LAST)
            node.up.left.arrow = arrow
        node.up.left=node
        node.move_all("left-down", False)
        node.up.move_all("left-up", False)
        self.window.update()
        print("rotation completed")

    def rotate_right(self, node):

        if node == self.root:
            self.root = node.left
        elif node == node.up.left:
            node.up.left = node.left
        else:
            node.up.right = node.left
        node.left.up = node.up
        node.up = node.left
        if node.up.right != None:
            node.up.right.up = node
            self.window.delete(node.up.right.arrow)
            coordinates = self.window.coords(node.up.right.obj)
            arrow = self.window.create_line(coordinates[0] + 75, coordinates[1] - 25, coordinates[2] - 25,coordinates[3] - 50, arrow=tkinter.LAST)
            node.up.right.arrow = arrow
        node.left = node.up.right
        node.up.right = node
        node.move_all("right-down", False)
        node.up.move_all("right-up", False)
        self.window.update()
    def splay(self, node):
        while node != self.root:
            if node.up.up != None and node == node.up.left and node.up == node.up.up.left:
                self.rotate_right(node.up.up)
                self.rotate_right(node.up)
            elif node.up.up != None and node == node.up.right and node.up == node.up.up.right:
                self.rotate_left(node.up.up)
                self.rotate_left(node.up)
            elif node.up.up != None and node == node.up.right and node.up == node.up.up.left:
                self.rotate_left(node.up)
                self.rotate_right(node.up)
            elif node.up.up != None and node == node.up.left and node.up == node.up.up.right:
                self.rotate_right(node.up)
                self.rotate_left(node.up)
            elif node.up == self.root and node == node.up.left:
                self.rotate_right(node.up)
            elif node.up == self.root and node == node.up.right:
                self.rotate_left(node.up)
    def insert_key(self, key):
        node = Node()
        node.key = key
        node.window = self.window
        node.obj = node.window.create_oval(50, 50, 100, 100)
        node.key_obj = self.window.create_text(75, 75, text=str(key))
        if self.root == None:
            node.move(400, 100, 1, 1)
            self.root = node
        else:
            current = self.root
            while not ( ( current.key <= key and current.right == None ) or ( current.key > key and current.left == None ) ):
                if current.key <= key:
                    coordinates = self.window.coords(current.obj)
                    text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
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
                    text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
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
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                self.window.delete(text)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                #time.sleep(1)
                node.move(coordinates[2] + 75, coordinates[3] + 50, 1, 1)
                arrow = self.window.create_line(coordinates[2], (coordinates[3] + coordinates[1]) / 2,coordinates[2] + 50, coordinates[3], arrow=tkinter.LAST)
                node.arrow = arrow
                current.right = node
                node.up = current
            else:
                coordinates = self.window.coords(current.obj)
                text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                node.move(coordinates[2] - 75, coordinates[3] + 50, 1, 1)
                arrow = self.window.create_line(coordinates[0], (coordinates[3] + coordinates[1]) / 2,coordinates[2] - 100, coordinates[3], arrow=tkinter.LAST)
                node.arrow = arrow
                current.left = node
                node.up = current
            self.splay(node)
    def find_element(self, key):
        current = self.root
        while current != None and current.key != key:
            if current.key < key:
                coordinates=self.window.coords(current.obj)
                self.window.itemconfig(current.obj, fill='red')
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                current = current.right
            else:
                self.window.itemconfig(current.obj, fill='red')
                coordinates = self.window.coords(current.obj)
                text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                current = current.left
        if current == None:
            text = self.window.create_text(50, 50, text="Node not found")
            self.window.update()
            #time.sleep(1)
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
            return None
        else:
            text = self.window.create_text(50, 50, text="Node found")
            self.window.itemconfig(current.obj, fill='red')
            self.window.update()
            #time.sleep(1)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
            return current
    def splay_find_element(self, key):
        current = self.root
        last = self.root
        while current != None and current.key != key:
            if current.key < key:
                coordinates=self.window.coords(current.obj)
                self.window.itemconfig(current.obj, fill='red')
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                current = current.right
                if current != None:
                    last = last.right
            else:
                self.window.itemconfig(current.obj, fill='red')
                coordinates = self.window.coords(current.obj)
                text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                current = current.left
                if current != None:
                    last = last.left
        if current == None:
            text = self.window.create_text(50, 50, text="Node not found")
            self.window.update()
            #time.sleep(1)
            self.window.delete(text)
            self.window.update()
            self.splay(last)
            #time.sleep(1)
            return None
        else:
            text = self.window.create_text(50, 50, text="Node found")
            self.window.itemconfig(current.obj, fill='red')
            self.window.update()
            #time.sleep(1)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            self.splay(current)
            #time.sleep(1)
            return current

    def show_min(self):
        if self.root == None:
            text=self.window.create_text(50, 50, text="Tree is empty!")
            self.window.update()
            #time.sleep(1)
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
        else:
            current = self.root
            while current.left != None:
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                #time.sleep(1)
                current = current.left
            self.window.itemconfig(current.obj, fill='red')
            text = self.window.create_text(100, 50, text="Minimum key in this tree is: " + str(current.key))
            self.window.update()
            #time.sleep(5)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
            print(current.key)

    def show_max(self):
        if self.root == None:
            text = self.window.create_text(50, 50, text="Tree is empty!")
            self.window.update()
            #time.sleep(1)
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
        else:
            current = self.root
            while current.right != None:
                self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                self.window.itemconfig(current.obj, fill='white')
                self.window.update()
                #time.sleep(1)
                current = current.right
            self.window.itemconfig(current.obj, fill='red')
            text = self.window.create_text(100, 50, text="Maximum key in this tree is: " + str(current.key))
            self.window.update()
            #time.sleep(5)
            self.window.itemconfig(current.obj, fill='white')
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
            print(current.key)
    def find_consequence(self, node):
        if node.left == None:
            return None
        else:
            current=node.left
            while current.right != None:
                current=current.right
            return current

    def delete_node(self, key):
        current = self.find_element(key)
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
                    self.splay(current.up)
            elif current.left == None or current.right == None:
                if current.left == None:
                    current.right.move_all("right", False)
                    self.window.delete(current.right.arrow)
                    current.right.arrow = current.arrow
                    self.window.delete(current.obj)
                    self.window.delete(current.key_obj)
                    if current == self.root:
                        self.root = current.right
                    else:
                        if current.up.left == current:
                            current.up.left = current.right
                            current.right.up = current.up
                        else:
                            current.up.right = current.right
                            current.right.up = current.up
                        self.splay(current.up)
                else:
                    current.left.move_all("left", False)
                    self.window.delete(current.left.arrow)
                    current.left.arrow = current.arrow
                    self.window.delete(current.obj)
                    self.window.delete(current.key_obj)
                    if current == self.root:
                        self.root = current.left
                    else:
                        if current.up.left == current:
                            current.up.left = current.left
                            current.left.up = current.up
                        else:
                            current.up.right = current.left
                            current.left.up = current.up
                        self.splay(current.up)
            else:
                consequent = self.find_consequence(current)
                k = consequent.key
                self.window.itemconfigure(current.key_obj, text=str(k))
                self.window.itemconfigure(consequent.key_obj, text=str(current.key))
                self.delete_node(consequent.key)
                current.key = k
                if current.up != None:
                    self.splay(current.up)