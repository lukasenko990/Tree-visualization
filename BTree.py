import tkinter
from tkinter import *
from tkinter import ttk
import time

class Node:
    key, left, right, window, key_obj, line= None, None, None, None, None, None
    def move(self, x_distance, y_distance, x_velovity, y_velocity):
        coordinates = self.window.coords(self.key_obj)
        while coordinates[0]!=x_distance or coordinates[1]!=y_distance:
            coordinates = self.window.coords(self.key_obj)
            if coordinates[0]==x_distance:
                x_velovity=0
            if coordinates[1]==y_distance:
                y_velocity=0
            if coordinates[0] > x_distance and x_velovity>0:
                x_velovity *= -1
            if coordinates[1] > y_distance and y_velocity>0:
                y_velocity *=-1
            #self.window.move(self.obj, x_velovity, y_velocity)
            self.window.move(self.key_obj, x_velovity, y_velocity)
            self.window.update()
            #time.sleep(0.01)
    def move_all(self, direction):
        if direction == "right":
            self.window.move(self.obj, 25, 0)
            if self.line != None:
                self.window.move(self.line, 25, 0)
            self.window.move(self.key_obj, 25, 0)
            if self.left != None:
                self.left.move_all("right")
            if self.right != None:
                self.right.move_all("right")
        if direction == "left":
            self.window.move(self.obj, 75, -50)
            if self.line != None:
                self.window.move(self.line, 75, -50)
            self.window.move(self.key_obj, 75, -50)
            if self.left != None:
                self.left.move_all("left")
            if self.right != None:
                self.right.move_all("left")

class NodeTab:
    nodes, max_degree, nodes_num, leaf , window, up, left, right, obj= None, None, 0, True, None, None, None, None, None
    def move(self, x_distance, y_distance, x_velovity, y_velocity):
        key_coordinates = self.window.coords(self.nodes[0].key_obj)
        obj_coordinates = self.window.coords(self.obj)
        xd = x_distance
        yd = y_distance
        xv = x_velovity
        yv = y_velocity
        while x_distance != 0 or y_distance != 0:
            obj_coordinates = self.window.coords(self.obj)
            if x_distance < 0 and x_velovity > 0:
                x_velovity *= -1
            if y_distance < 0 and y_velocity > 0:
                y_velocity *= -1
            if x_distance == 0:
                x_velovity=0
            if y_distance == 0:
                y_velocity=0
            self.window.move(self.obj, x_velovity, y_velocity)
            self.window.update()
            #time.sleep(0.01)
            if x_distance < 0:
                x_distance += (x_velovity*-1)
            else:
                x_distance -= x_velovity
            if y_distance < 0:
                y_distance += (y_velocity*-1)
            else:
                y_distance -= y_velocity
        for i in range(0, self.nodes_num):
            x_distance = xd
            y_distance = yd
            x_velovity = xv
            y_velocity = yv
            while x_distance != 0 or y_distance != 0:
                key_coordinates = self.window.coords(self.nodes[i].key_obj)
                if x_distance < 0 and x_velovity > 0:
                    x_velovity *= -1
                if y_distance < 0 and y_velocity > 0:
                    y_velocity *= -1
                if x_distance == 0:
                    x_velovity = 0
                if y_distance == 0:
                    y_velocity = 0
                self.window.move(self.nodes[i].key_obj, x_velovity, y_velocity)
                self.window.update()
               # time.sleep(0.01)
                if x_distance < 0:
                    x_distance += (x_velovity * -1)
                else:
                    x_distance -= x_velovity
                if y_distance < 0:
                    y_distance += (y_velocity * -1)
                else:
                    y_distance -= y_velocity
    def move_all(self):
        for i in range(0, self.nodes_num):
            if self.nodes[i].left != None:
                self.nodes[i].left.move(0, 50, 0.5, 0.5)
                self.nodes[i].left.move_all()
            if i == self.nodes_num - 1 and self.nodes[i].right != None:
                self.nodes[i].right.move(0, 50, 0.5, 0.5)
                self.nodes[i].right.move_all()
    def align(self):
        if self.up == None:
            coords = self.window.coords(self.obj)
            x_min = coords[0]
            x_max = 800 - coords[2]
            diff = int(abs(x_min - x_max)/2)
            if x_min > x_max:
                diff *=-1
            self.move(diff, 0, 0.5, 0.5)
        elif self.leaf != True:
            min = self
            while min.leaf != True:
                min = min.nodes[0].left
            max = self
            while max.leaf != True:
                max = max.nodes[max.nodes_num - 1].right
            print("Start:")
            print(self.nodes[0].key)
            print(min.nodes[0].key)
            print(max.nodes[0].key)
            coords_min = self.window.coords(min.obj)
            coords_max = self.window.coords(max.obj)
            x_min = coords_min[0]
            x_max = coords_max[2]
            coords_self = self.window.coords(self.obj)
            x_min_diff = abs(coords_self[0]-x_min)
            x_max_diff = abs(coords_self[2]-x_max)
            print(x_min_diff)
            print(x_max_diff)
            self_diff = int(abs(x_min_diff-x_max_diff)/2)
            if(x_min > coords_self[0]):
                self_diff += int(x_min-coords_self[0])
            if (x_max < coords_self[2]):
                self_diff += int(coords_self[2]-x_max)
            if x_min_diff > x_max_diff:
                self_diff *= -1
            print(self_diff)
            self.move(self_diff, 0, 0.5, 0.5)
        else:
            current = self
            while current.up != None:
                current = current.up
            coords = self.window.coords(current.obj)
            min = coords[0]
            max = coords[2]
            coords2 = self.window.coords(self.obj)
            pom = self
            while pom.right != None:
                pom = pom.right
            coords3 = self.window.coords(pom.obj)
            min_diff = abs(min-coords2[0])
            max_diff = abs(coords3[2]-max)
            diff = int(abs(min_diff - max_diff))
            diff = int(diff/2)
            if min_diff < max_diff:
                diff *=-1
            cur = self
            while cur != None:
                cur.move(diff, 0, 0.5, 0.5)
                cur=cur.right

    def insert_node(self, node):
        it =0
        while it < self.nodes_num and self.nodes[it].key <= node.key:
            it += 1
        if it == 0:
            if self.left != None:
                cu = self.left
                while cu != None:
                    cu.move(-25, 0, 0.5, 0.5)
                    cu = cu.left
            coords = self.window.coords(self.obj)
            node.move(coords[0]-12.5, coords[1]+17, 0.5, 0.5)
            self.window.coords(self.obj, coords[0]-25, coords[1], coords[2], coords[3])
            if node.right == None:
                node.right = self.nodes[0].left
            else:
                self.nodes[0].left = node.right
            self.nodes.append(node)
            self.nodes = sorted(self.nodes, key=lambda nodes: nodes.key)
            self.nodes_num +=1
        elif it == self.nodes_num:
            if self.right != None:
                cu = self.right
                while cu!= None:
                    cu.move(25, 0, 0.5, 0.5)
                    cu = cu.right
            coords = self.window.coords(self.obj)
            node.move(coords[2] + 12.5, coords[1] + 17, 0.5, 0.5)
            self.window.coords(self.obj, coords[0], coords[1], coords[2] + 25, coords[3])
            if node.left == None:
                node.left = self.nodes[it-1].right
            else:
                self.nodes[it-1].right = node.left
            self.nodes.append(node)
            self.nodes_num +=1

        else:
            if self.right != None:
                cr = self.right
                while cr!= None:
                    cr.move(12.5, 0, 0.5, 0.5)
                    cr = cr.right
            if self.left != None:
                cl = self.left
                while cl != None:
                    cl.move(-12.5, 0, 0.5, 0.5)
                    cl = cl.left
            coords = self.window.coords(self.obj)
            self.window.coords(self.obj, coords[0]-12.5, coords[1], coords[2] + 12.5, coords[3])
            for i in range (0, it):
                coords2 = self.window.coords(self.nodes[i].key_obj)
                self.nodes[i].move(coords2[0]-12.5, coords2[1], 0.5, 0.5)
            for i in range (it, self.nodes_num):
                coords2 = self.window.coords(self.nodes[i].key_obj)
                self.nodes[i].move(coords2[0]+12.5, coords2[1], 0.5, 0.5)
            coords = self.window.coords(self.nodes[it-1].key_obj)
            node.move(coords[0] + 25, coords[1] , 0.5, 0.5)
            if node.left == None:
                node.left = self.nodes[it-1].right
            else:
                self.nodes[it-1].right = node.left
            if node.right == None:
                node.right = self.nodes[it].left
            else:
                self.nodes[it].left = node.right
            self.nodes.append(node)
            self.nodes = sorted(self.nodes, key=lambda nodes:nodes.key)
            self.nodes_num +=1
        if self.leaf != True and self.up != None:
            pom = self
            while pom.left != None:
                pom=pom.left
            while pom != None:
                pom.align()
                pom = pom.right
        else:
            pom = self
            while pom.left != None:
                pom = pom.left
            pom.align()

class BTree:
    root = None
    window=None
    def move_key_up(self, NT):
        middle = int(NT.max_degree/2)
        left = NodeTab()
        right = NodeTab()
        left.nodes = []
        right.nodes = []
        left.max_degree = NT.max_degree
        right.max_degree = NT.max_degree
        left.nodes_num = middle
        right.nodes_num = NT.max_degree - left.nodes_num-1
        for i in range(0,middle):
            left.nodes.append(NT.nodes[i])
        for i in range(middle+1, NT.max_degree):
            right.nodes.append(NT.nodes[i])
        left.right = right
        right.left = left
        left.window = self.window
        right.window = self.window
        pom = NT.nodes[middle]
        pom.left = left
        pom.right = right
        NT.nodes.clear()
        NT.window.update()
        if NT == self.root:
            NT.nodes_num = 1
            NT.leaf = False
            NT.nodes.append(pom)
            left.up = NT
            right.up = NT
            coords = self.window.coords(NT.obj)
            left.obj = self.window.create_rectangle(coords[0], coords[1], coords[2]-50, coords[3])
            right.obj = self.window.create_rectangle(coords[0]+50, coords[1], coords[2], coords[3])
            self.window.coords(NT.obj, coords[0]+25, coords[1], coords[2]-25, coords[3] )
            left.move(0, 50, 0.5, 0.5)
            right.move(0, 50, 0.5, 0.5)
            for i in range(0, left.nodes_num):
                if left.nodes[i].left != None or left.nodes[i].right != None:
                    left.leaf = False
            if left.leaf == False:
                right.leaf = False
                left.move_all()
                right.move_all()
                for i in range(0, left.nodes_num):
                    left.nodes[i].left.up = left
                    if i == left.nodes_num - 1 and left.nodes[i].right != None:
                        left.nodes[i].right.up = left
                for i in range(0, right.nodes_num):
                    right.nodes[i].left.up = right
                    if i == right.nodes_num - 1 and right.nodes[i].right != None:
                        right.nodes[i].right.up = right
                left.align()
                right.align()
            else:
                left.move(7.5, 0, 0.5, 0.5)
                right.move(-7.5, 0, 0.5, 0.5)
        else:
            left.up = NT.up
            right.up = NT.up
            coords = self.window.coords(NT.obj)
            left.obj = self.window.create_rectangle(coords[0], coords[1], coords[2]-50, coords[3])
            right.obj = self.window.create_rectangle(coords[0]+50, coords[1], coords[2], coords[3])
            if NT.left != None and NT.right != None:
                left.left = NT.left
                NT.left.right = left
                right.right = NT.right
                NT.right.left = right
                curr = right
                while curr!=None:
                    curr.move(-12.5, 0, 0.5, 0.5)
                    curr=curr.right
            elif NT.left != None:
                left.left = NT.left
                NT.left.right = left
                right.move(-12.5, 0, 0.5, 0.5)
            elif NT.right != None:
                right.right = NT.right
                NT.right.left = right
                left.move(12.5, 0 ,0.5, 0.5)
            for i in range(0, left.nodes_num):
                if left.nodes[i].left != None or left.nodes[i].right != None:
                    left.leaf = False
            if left.leaf == False:
                right.leaf = False
                for i in range(0, left.nodes_num):
                    left.nodes[i].left.up = left
                    if i == left.nodes_num-1 and left.nodes[i].right != None:
                        left.nodes[i].right.up = left
                for i in range(0, right.nodes_num):
                    right.nodes[i].left.up = right
                    if i == right.nodes_num-1 and right.nodes[i].right != None:
                        right.nodes[i].right.up = right
                current = left
                while current.left != None:
                    current = current.left
                while current != None:
                    current.align()
                    current = current.right
            else:
                current = left
                while current.left != None:
                    current = current.left
                current.align()
            self.window.delete(NT.obj)
            left.up.insert_node(pom)
            if left.up.nodes_num == left.up.max_degree:
                self.move_key_up(left.up)
            #left.up.nodes = sorted(left.up.nodes, key = lambda nodes:nodes.key)

    def insert_element(self, key):
        new_element = Node()
        new_element.key = key;
        new_element.window=self.window
        new_element.key_obj=self.window.create_text(60,60, text=str(key))
        if self.root == None:
            self.root = NodeTab()
            self.root.nodes = []
            self.root.nodes.append(new_element)
            self.root.nodes_num+=1
            self.root.max_degree = 3
            self.root.window=self.window
            self.root.obj=self.window.create_rectangle(382.5, 82.5, 412.5, 112.5)
            new_element.move(400, 100, 0.5, 0.5)
        else:
            current = self.root
            it = 0
            while current.leaf == False:
                if current.nodes[it].key <= key:
                    self.window.itemconfig(current.nodes[it].key_obj, fill='red')
                    self.window.update()
                    #leep(1)
                    self.window.itemconfig(current.nodes[it].key_obj, fill='black')
                    self.window.update()
                    #time.sleep(1)
                    if it+1 < current.nodes_num and current.nodes[it+1].key <= key:
                        it +=1
                    elif it+1 < current.nodes_num and current.nodes[it+1].key > key:
                        current = current.nodes[it].right
                        it = 0
                    elif it == current.nodes_num-1:
                        current = current.nodes[it].right
                        it = 0
                    elif it == current.max_degree - 1:
                        current = current.nodes[it].right
                        it = 0
                else:
                    self.window.itemconfig(current.nodes[it].key_obj, fill='red')
                    self.window.update()
                    #time.sleep(1)
                    self.window.itemconfig(current.nodes[it].key_obj, fill='black')
                    self.window.update()
                    #time.sleep(1)
                    current = current.nodes[it].left
            current.insert_node(new_element)
            if current.max_degree == current.nodes_num:
                self.move_key_up(current)
                    #if current.nodes_num == current.max_degree:




    def find_element(self, key):
        current = self.root
        while current != None and current.key != key:
            if current.key < key:
                coordinates=self.window.coords(current.obj)
                self.window.itemconfig(current.obj, fill='red')
                text = self.window.create_text(coordinates[2] + 50, coordinates[3] - 25,text=str(key) + " >= " + str(current.nodes[it].key))
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
            time.sleep(5)
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
            time.sleep(5)
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






