import tkinter
from tkinter import *
from tkinter import ttk
import time
class Node:
    key, left, right, up, window, obj, key_obj, arrow, color, db= None, None, None, None, None, None, None, None, None, None
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






class RedBlackTree:
    window = None
    root = None
    number_of_nodes=0
    def rotate_left(self, node):
        #time.sleep(2)
        print("rotating left:" + str(node.key))
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
            print("here"+str(node.up.left.key))
        if node.right != None:
            print("node right:"+ str(node.right.key))
        if node.up.left != None:
            node.up.left.up = node
            self.window.delete(node.up.left.arrow)
            coordinates = self.window.coords(node.up.left.obj)
            arrow = self.window.create_line(coordinates[2]-75, coordinates[3]-75, coordinates[2]-25, coordinates[3]-50, arrow=tkinter.LAST)
            node.up.left.arrow = arrow
        node.up.left=node
        self.root.color='b'
        self.window.itemconfig(self.root.obj, fill = 'grey')
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
            arrow = self.window.create_line(coordinates[2] + 75, coordinates[3] - 75, coordinates[2] - 25,coordinates[3] - 50, arrow=tkinter.LAST)
            self.arrow = arrow
        node.left = node.up.right
        node.up.right = node
        self.root.color='b'
        self.window.itemconfig(self.root.obj, fill='grey')
        node.move_all("right-down", False)
        node.up.move_all("right-up", False)
        self.window.update()

    def check(self, node):
        if node.up != None and node.up.up != None and node.up.color=='r' and node.color == 'r':
                if node.up == node.up.up.left and node.up.up.right != None and node.up.up.right.color == 'r':
                    node.up.color = 'b'
                    self.window.itemconfig(node.up.obj, fill='grey')
                    node.up.up.right.color = 'b'
                    self.window.itemconfig(node.up.up.right.obj, fill='grey')
                    if node.up.up.color == 'b':
                        node.up.up.color = 'r'
                        self.window.itemconfig(node.up.up.obj, fill='red')
                    else:
                        node.up.up.color = 'b'
                        self.window.itemconfig(node.up.up.obj, fill='grey')
                    self.check(node.up.up)
                elif node.up == node.up.up.right and node.up.up.left != None and node.up.up.left.color == 'r':
                    node.up.color = 'b'
                    self.window.itemconfig(node.up.obj, fill='grey')
                    node.up.up.left.color = 'b'
                    self.window.itemconfig(node.up.up.left.obj, fill='grey')
                    if node.up.up.color == 'b':
                        node.up.up.color = 'r'
                        self.window.itemconfig(node.up.up.obj, fill='red')
                    else:
                        node.up.up.color = 'b'
                        self.window.itemconfig(node.up.up.obj, fill='grey')
                    self.check(node.up.up)
                elif node.up == node.up.up.left and node == node.up.right and ( node.up.up.right == None or node.up.up.right.color == 'b') :
                    self.rotate_left(node.up)
                    self.check(node.left)
                elif node.up == node.up.up.right and node == node.up.left and ( node.up.up.left == None or node.up.up.left.color=='b' ):
                    self.rotate_right(node.up)
                    self.check(node.right)
                elif node.up.color == 'r' and node.up == node.up.up.right and node == node.up.right and ( node.up.up.left == None or node.up.up.left.color == 'b' ):
                    node.up.color = 'b'
                    self.window.itemconfig(node.up.obj, fill='grey')
                    if node.up.up.color == 'b':
                        node.up.up.color = 'r'
                        self.window.itemconfig(node.up.up.obj, fill='red')
                    else:
                        node.up.up.color = 'b'
                        self.window.itemconfig(node.up.up.obj, fill='grey')
                    self.rotate_left(node.up.up)
                    self.check(node.up)
                elif node.up.color == 'r' and node.up == node.up.up.left and node == node.up.left and ( node.up.up.right == None or node.up.up.right.color == 'b' ):
                    node.up.color = 'b'
                    self.window.itemconfig(node.up.obj, fill='grey')
                    if node.up.up.color == 'b':
                        node.up.up.color = 'r'
                        self.window.itemconfig(node.up.up.obj, fill='red')
                    else:
                        node.up.up.color = 'b'
                        self.window.itemconfig(node.up.up.obj, fill='grey')
                    self.rotate_right(node.up.up)
                self.check(node.up)
        self.window.update()
    def insert_key(self, key):
        node = Node()
        node.key = key
        node.color = 'r'
        node.window = self.window
        node.obj = node.window.create_oval(50, 50, 100, 100)
        node.key_obj = self.window.create_text(75, 75, text=str(key))
        self.window.itemconfig(node.obj, fill = 'red')
        #pom->element_w_liscie=liczba_elementow;
        if self.root == None:
            node.move(400, 100, 1, 1)
            self.root = node
            self.root.color = 'b'
            self.window.itemconfig(self.root.obj, fill = 'grey')
        else:
            current = self.root
            while not ( ( current.key <= key and current.right == None ) or ( current.key > key and current.left == None ) ):
                if current.key <= key:
                    coordinates = self.window.coords(current.obj)
                    text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                    self.window.itemconfig(current.obj, fill='green')
                    self.window.update()
                    #time.sleep(1)
                    if current.color == 'b':
                        self.window.itemconfig(current.obj, fill='grey')
                    else:
                        self.window.itemconfig(current.obj, fill='red')
                    self.window.delete(text)
                    self.window.update()
                    #time.sleep(1)
                    current = current.right
                else:
                    coordinates = self.window.coords(current.obj)
                    text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
                    self.window.itemconfig(current.obj, fill='green')
                    self.window.update()
                    #time.sleep(1)
                    if current.color == 'b':
                        self.window.itemconfig(current.obj, fill='grey')
                    else:
                        self.window.itemconfig(current.obj, fill='red')
                    self.window.delete(text)
                    self.window.update()
                    #time.sleep(1)
                    current = current.left
            if current.key <= key:
                coordinates = self.window.coords(current.obj)
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.itemconfig(current.obj, fill='green')
                self.window.update()
                #time.sleep(1)
                self.window.delete(text)
                if current.color == 'b':
                    self.window.itemconfig(current.obj, fill='grey')
                else:
                    self.window.itemconfig(current.obj, fill='red')
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
                self.window.itemconfig(current.obj, fill='green')
                self.window.update()
                #time.sleep(1)
                if current.color == 'b':
                    self.window.itemconfig(current.obj, fill='grey')
                else:
                    self.window.itemconfig(current.obj, fill='red')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                node.move(coordinates[2] - 75, coordinates[3] + 50, 1, 1)
                arrow = self.window.create_line(coordinates[0], (coordinates[3] + coordinates[1]) / 2,coordinates[2] - 100, coordinates[3], arrow=tkinter.LAST)
                node.arrow = arrow
                current.left = node
                node.up = current
            self.check(node)
        self.root.color = 'b'
        self.window.itemconfig(self.root.obj, fill='grey')
    def find_element(self, key):
        current = self.root
        while current != None and current.key != key:
            if current.key < key:
                coordinates=self.window.coords(current.obj)
                self.window.itemconfig(current.obj, fill='green')
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.key))
                self.window.update()
                #time.sleep(1)
                if current.color == 'b':
                    self.window.itemconfig(current.obj, fill='grey')
                else:
                    self.window.itemconfig(current.obj, fill='red')
                self.window.delete(text)
                self.window.update()
                #time.sleep(1)
                current = current.right
            else:
                self.window.itemconfig(current.obj, fill='green')
                coordinates = self.window.coords(current.obj)
                text = self.window.create_text(coordinates[2] - 100, coordinates[3] - 25,text=str(key) + " <= " + str(current.key))
                self.window.update()
                #time.sleep(1)
                if current.color == 'b':
                    self.window.itemconfig(current.obj, fill='grey')
                else:
                    self.window.itemconfig(current.obj, fill='red')
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
            self.window.itemconfig(current.obj, fill='green')
            self.window.update()
            #time.sleep(1)
            if current.color == 'b':
                self.window.itemconfig(current.obj, fill='grey')
            else:
                self.window.itemconfig(current.obj, fill='red')
            self.window.delete(text)
            self.window.update()
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
                self.window.itemconfig(current.obj, fill='green')
                self.window.update()
                #time.sleep(1)
                if current.color == 'b':
                    self.window.itemconfig(current.obj, fill='grey')
                else:
                    self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                current = current.left
            self.window.itemconfig(current.obj, fill='green')
            text = self.window.create_text(100, 50, text="Minimum key in this tree is: " + str(current.key))
            self.window.update()
            #time.sleep(5)
            if current.color == 'b':
                self.window.itemconfig(current.obj, fill='grey')
            else:
                self.window.itemconfig(current.obj, fill='red')
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
                self.window.itemconfig(current.obj, fill='green')
                self.window.update()
                #time.sleep(1)
                if current.color == 'b':
                    self.window.itemconfig(current.obj, fill='grey')
                else:
                    self.window.itemconfig(current.obj, fill='red')
                self.window.update()
                #time.sleep(1)
                current = current.right
            self.window.itemconfig(current.obj, fill='green')
            text = self.window.create_text(100, 50, text="Maximum key in this tree is: " + str(current.key))
            self.window.update()
            #time.sleep(5)
            if current.color == 'b':
                self.window.itemconfig(current.obj, fill='grey')
            else:
                self.window.itemconfig(current.obj, fill='red')
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
    def refactor(self, node, deleted):
        node.db = True
        if node == self.root:
            self.root.db = False
        elif node == node.up.left and node.up.right != None and node.up.right.color == 'b' and ((
                     node.up.right.left == None and node.up.right.right == None) or (
                     node.up.right.left != None and node.up.right.left.color == 'b' and
                     node.up.right.right != None and node.up.right.right == 'b') or (
                     node.up.right.right == None and node.up.right.left != None and node.up.right.left.color == 'b'
        ) or (node.up.right.left == None and node.up.right.right != None and node.up.right.right.color == 'b')
        ):
            print("case 1:"+str(node.key))
            node.db = False
            if node.up.color == 'b':
                node.up.db = True
            else:
                node.up.color = 'b'
                self.window.itemconfig(node.up.obj, fill='grey')
            node.up.right.color = 'r'
            self.window.itemconfig(node.up.right.obj, fill='red')
            next = node.up
            if deleted == False:
                node.color = 'r'
                self.delete_node(node.key)
                deleted = True
            if next.db == True:
                self.refactor(next, deleted)

        elif node == node.up.right and node.up.left != None and node.up.left.color == 'b' and ((
                     node.up.left.left == None and node.up.left.right == None) or (
                     node.up.left.left != None and node.up.left.left.color == 'b' and
                     node.up.left.right != None and node.up.left.right == 'b') or (
                     node.up.left.left == None and node.up.left.right != None and node.up.left.right.color == 'b'
        ) or ( node.up.left.right == None and node.up.left.left != None and node.up.left.left.color == 'b')
        ):
            print("case 1:"+str(node.key))
            node.db = False
            if node.up.color == 'b':
                node.up.db = True
            else:
                node.up.color = 'b'
                self.window.itemconfig(node.up.obj, fill='grey')
            node.up.left.color = 'r'
            self.window.itemconfig(node.up.left.obj, fill='red')
            print(node.up.left.key)
            next = node.up
            if deleted == False:
                node.color = 'r'
                self.delete_node(node.key)
                deleted = True
            if next.db == True:
                self.refactor(next, deleted)
        elif node == node.up.left and node.up.right != None and node.up.right.color == 'r':
            print("case 2:" + str(node.key))
            print(node.up.right.key)
            print(node.up.color)
            node.up.color = 'r'
            node.up.right.color = 'b'
            parent = node.up
            self.window.itemconfig(parent.obj, fill = 'red')
            self.window.itemconfig(parent.right.obj, fill = 'grey')
            self.rotate_left(parent)
            self.refactor(node, deleted)
        elif node == node.up.right and node.up.left != None and node.up.left.color == 'r':
            print("case 2:" + str(node.key))
            node.up.color = 'r'
            node.up.left.color = 'b'
            parent = node.up
            self.window.itemconfig(parent.obj, fill = 'red')
            self.window.itemconfig(parent.left.obj, fill = 'grey')
            self.rotate_right(parent)
            self.refactor(node, deleted)
        elif node == node.up.right and node.up.left != None and node.up.left.color == 'b' and ( (
                     node.up.left.left == None and node.up.left.right != None and node.up.left.right.color == 'r') or (
                     node.up.left.left != None and node.up.left.left.color == 'b' and
                     node.up.left.right != None and node.up.left.right.color == 'r')
        ):
            print("case 3:" + str(node.key))
            node.up.left.color = 'r'
            node.up.left.right.color = 'b'
            parent = node.up
            self.window.itemconfig(parent.left.obj, fill = 'red')
            self.window.itemconfig(parent.left.right.obj, fill='grey')
            self.rotate_left(parent.left)
            self.refactor(node, deleted)
        elif node == node.up.left and node.up.right != None and node.up.right.color == 'b' and ( (
                     node.up.right.right == None and node.up.right.left != None and node.up.right.left.color == 'r') or (
                     node.up.right.right != None and node.up.right.right.color == 'b' and
                     node.up.right.left != None and node.up.right.left.color == 'r')
        ):
            print("case 3:" + str(node.key))
            node.up.right.color = 'r'
            node.up.right.left.color = 'b'
            parent = node.up
            self.window.itemconfig(parent.right.obj, fill = 'red')
            self.window.itemconfig(parent.right.left.obj, fill='grey')
            self.rotate_right(parent.right)
            self.refactor(node, deleted)
        elif node == node.up.right and node.up.left != None and node.up.left.color == 'b' and node.up.left.left != None and node.up.left.left.color == 'r':
            print("case 4:" + str(node.key))
            parent = node.up
            c = parent.color
            parent.color = parent.left.color
            parent.left.color = c
            parent.left.left.color = 'b'
            self.window.itemconfig(parent.left.left.obj, fill='grey')
            if parent.color == 'b':
                self.window.itemconfig(parent.obj, fill='grey')
            else:
                self.window.itemconfig(parent.obj, fill='red')
            if parent.left.color == 'b':
                self.window.itemconfig(parent.left.obj, fill='grey')
            else:
                self.window.itemconfig(parent.left.obj, fill='red')

            self.rotate_right(parent)
            node.db = False
            print (node.key)
            if deleted == False:
                node.color = 'r'
                self.delete_node(node.key)
                deleted = True

            #self.refactor(node, deleted)
        elif node == node.up.left and node.up.right != None and node.up.right.color == 'b' and node.up.right.right != None and node.up.right.right.color == 'r':
            print("case 4:" + str(node.key))
            parent = node.up
            c = parent.color
            parent.color = parent.right.color
            parent.right.color = c
            parent.right.right.color = 'b'
            self.window.itemconfig(parent.right.right.obj, fill='grey')
            if parent.color == 'b':
                self.window.itemconfig(parent.obj, fill='grey')
            else:
                self.window.itemconfig(parent.obj, fill='red')
            if parent.right.color == 'b':
                self.window.itemconfig(parent.right.obj, fill='grey')
            else:
                self.window.itemconfig(parent.right.obj, fill='red')
            node.db = False
            self.rotate_left(parent)
            print("pl:"+str(node.key))
            if deleted == False:
                node.color = 'r'
                self.delete_node(node.key)
                deleted = True
                # self.refactor(node, deleted)

    def delete_node(self, key):
        current = self.find_element(key)
        if current == None:
            return None
        else:
            if current.left != None and current.right != None:
                consequent = self.find_consequence(current)
                k = consequent.key
                self.window.itemconfigure(current.key_obj, text=str(k))
                self.window.itemconfigure(consequent.key_obj, text=str(current.key))
                self.delete_node(consequent.key)
                current.key = k
            else:
                if current.color == 'r' or (current.left != None and current.left.color == 'r') or (current.right != None and current.right.color == 'r'):
                    print(current.key)
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
                    elif current.left == None:
                        self.window.itemconfig(current.right.obj, fill = 'grey')
                        current.right.color ='b'
                        current.right.move_all("right", True)
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
                    else:
                        self.window.itemconfig(current.left.obj, fill='grey')
                        current.left.color = 'b'
                        current.left.move_all("left", True)
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
                else:
                    self.refactor(current, False)