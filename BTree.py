import tkinter
from tkinter import *
from tkinter import ttk
import time

class Node:
    key, left, right, window, key_obj, line, right_line= None, None, None, None, None, None, None
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
    nodes, max_degree, nodes_num, leaf , window, up, left, right, obj, min_degree= None, None, 0, True, None, None, None, None, None, None
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
        self.window.update()
        root = self
        while root.up != None:
            root = root.up
        coords = self.window.coords(root.obj)
        x_min = coords[0]
        x_max = 800 - coords[2]
        y_min = coords[1]
        if y_min > 100:
            y_min = y_min - (y_min-100)
            y_min *= -1
        else:
            y_min = 0
        diff_x = int(abs(x_min - x_max) / 2)
        if x_min > x_max:
            diff_x *= -1
        root.move(diff_x, y_min, 0.5, 0.5)
        next = root.nodes[0].left
        while next != None:
            left = next
            right = next
            while left.nodes[0].left != None:
                left = left.nodes[0].left
            while right.nodes[right.nodes_num-1].right != None:
                right = right.nodes[right.nodes_num-1].right
            if next != left:
                coords_min = self.window.coords(left.obj)
                coords_max = self.window.coords(right.obj)
                x_min = coords_min[0]
                x_max = coords_max[2]
                coords_self = self.window.coords(next.obj)
                coords_up = self.window.coords(next.up.obj)
                x_min_diff = abs(coords_self[0] - x_min)
                x_max_diff = abs(coords_self[2] - x_max)
                y_diff = coords_self[1]-coords_up[1]
                if(y_diff > 50):
                    y_diff = y_diff-(y_diff-50)
                    y_diff *= -1
                else:
                    y_diff = 0
                self_diff = int(abs(x_min_diff - x_max_diff) / 2)
                if (x_min > coords_self[0]):
                    self_diff += int(x_min - coords_self[0])
                if (x_max < coords_self[2]):
                    self_diff += int(coords_self[2] - x_max)
                if x_min_diff > x_max_diff:
                    self_diff *= -1
                next.move(self_diff, y_diff, 0.5, 0.5)
            else:
                coords = self.window.coords(root.obj)
                min = coords[0]
                max = coords[2]
                coords2 = self.window.coords(next.obj)
                pom = next
                while pom.right != None:
                    pom = pom.right
                coords3 = self.window.coords(pom.obj)
                coords_up = self.window.coords(next.up.obj)
                y_diff = coords2[1] - coords_up[1]
                if (y_diff > 50):
                    y_diff = y_diff - (y_diff - 50)
                    y_diff *= -1
                else:
                    y_diff = 0
                min_diff = abs(min - coords2[0])
                max_diff = abs(coords3[2] - max)
                diff = int(abs(min_diff - max_diff))
                diff = int(diff / 2)
                if min_diff < max_diff:
                    diff *= -1
                cur = next
                while cur != None:
                    cur.move(diff, y_diff, 0.5, 0.5)
                    cur = cur.right
                break
            if next.right != None:
                next = next.right
            else:
                while next.left != None:
                    next = next.left
                next = next.nodes[0].left
    def create_lines(self):
        cur = self
        while cur.up != None:
            cur = cur.up
        while cur != None:
            current = cur
            while current.left != None:
                current = current.left
            while current!= None:
                for i in range(0, current.nodes_num):
                    if current.nodes[i].left != None:
                        source = self.window.coords(current.nodes[i].key_obj)
                        destination = self.window.coords(current.nodes[i].left.obj)
                        current.nodes[i].line = self.window.create_line(source[0]-17, source[1], (destination[0]+destination[2])/2, destination[1])
                    if i == current.nodes_num - 1 and current.nodes[i].right != None:
                        source = self.window.coords(current.nodes[i].key_obj)
                        destination = self.window.coords(current.nodes[i].right.obj)
                        current.nodes[i].right_line = self.window.create_line(source[0]+12.5, source[1], (destination[0] + destination[2]) / 2, destination[1])
                current = current.right
            cur = cur.nodes[0].left
    def delete_lines(self):
        cur = self
        while cur.up != None:
            cur = cur.up
        while cur != None:
            current = cur
            while current.left != None:
                current = current.left
            while current != None:
                for i in range (0, current.nodes_num):
                    if current.nodes[i].line != None:
                        self.window.delete(current.nodes[i].line)
                        current.nodes[i].line = None
                    if current.nodes[i].right_line != None:
                        self.window.delete(current.nodes[i].right_line)
                        current.nodes[i].right_line = None
                current = current.right
            cur = cur.nodes[0].left


    def borrow_from_left_leaf(self):
        current = self.up
        node_up = None
        for i in range (0, current.nodes_num):
            if current.nodes[i].right == self:
                node_up = current.nodes[i]
                break
        new_node = Node()
        new_node.key = node_up.key
        new_node.window = self.window
        new_node_coords = self.window.coords(self.nodes[0].key_obj)
        new_node.key_obj = self.window.create_text(new_node_coords[0]-25, new_node_coords[1], text = str(new_node.key))
        self_obj_coords = self.window.coords(self.obj)
        new_node.right = self.nodes[0].left
        new_node.left = node_up.left.nodes[node_up.left.nodes_num-1].right
        if new_node.left != None:
            new_node.left.up = self
        self.window.coords(self.obj, self_obj_coords[0]-25, self_obj_coords[1], self_obj_coords[2], self_obj_coords[3] )
        coords = self.window.coords(node_up.left.obj)
        self.window.coords(node_up.left.obj, coords[0], coords[1], coords[2] - 25, coords[3])
        self.nodes_num +=1
        self.nodes.append(new_node)
        self.nodes = sorted(self.nodes, key = lambda nodes:nodes.key)
        node_left = node_up.left.nodes[node_up.left.nodes_num-1]
        node_up.key = node_left.key
        node_up_coords = self.window.coords(node_up.key_obj)
        self.window.delete(node_up.key_obj)
        node_up.key_obj = self.window.create_text(node_up_coords[0], node_up_coords[1], text = str(node_up.key))
        self.window.delete(node_up.left.nodes[node_up.left.nodes_num - 1].key_obj)
        self.delete_lines()
        self.align()
        del node_up.left.nodes[node_up.left.nodes_num - 1]
        node_up.left.nodes_num -= 1
        self.create_lines()
    def borrow_from_right_leaf(self):
        current = self.up
        node_up = None
        for i in range (0, current.nodes_num):
            if current.nodes[i].left == self:
                node_up = current.nodes[i]
                break
        new_node = Node()
        new_node.key = node_up.key
        new_node.left = self.nodes[self.nodes_num-1].right
        new_node.right = node_up.right.nodes[0].left
        if new_node.right != None:
            new_node.right.up = self
        new_node.window = self.window
        new_node_coords = self.window.coords(self.nodes[self.nodes_num - 1].key_obj)
        new_node.key_obj = self.window.create_text(new_node_coords[0]+25, new_node_coords[1], text = str(new_node.key))
        self_obj_coords = self.window.coords(self.obj)
        self.window.coords(self.obj, self_obj_coords[0], self_obj_coords[1], self_obj_coords[2]+25, self_obj_coords[3] )
        coords = self.window.coords(node_up.right.obj)
        self.window.coords(node_up.right.obj, coords[0]+25, coords[1], coords[2], coords[3])
        self.nodes_num +=1
        self.nodes.append(new_node)
        node_right = node_up.right.nodes[0]
        node_up.key = node_right.key
        node_up_coords = self.window.coords(node_up.key_obj)
        self.window.delete(node_up.key_obj)
        node_up.key_obj = self.window.create_text(node_up_coords[0], node_up_coords[1], text = str(node_up.key))
        self.window.delete(node_up.right.nodes[0].key_obj)
        self.delete_lines()
        self.align()
        del node_up.right.nodes[0]
        node_up.right.nodes_num -= 1
        self.create_lines()
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
        self.align()

class BTree:
    root = None
    window=None
    def move_key_up(self, NT):
        middle = int(NT.max_degree/2)
        if NT.max_degree % 2 == 0:
            middle -=1
        left = NodeTab()
        right = NodeTab()
        left.min_degree = NT.min_degree
        right.min_degree = NT.min_degree
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
            left_number = NT.max_degree-middle
            right_number = middle+1
            NT.nodes_num = 1
            NT.leaf = False
            NT.nodes.append(pom)
            left.up = NT
            right.up = NT
            coords = self.window.coords(NT.obj)
            left.obj = self.window.create_rectangle(coords[0], coords[1], coords[2]-(25*left_number), coords[3])
            right.obj = self.window.create_rectangle(coords[0]+(25*right_number), coords[1], coords[2], coords[3])
            self.window.coords(NT.obj, coords[0]+(25*middle), coords[1], coords[2]-(25*(NT.max_degree-middle-1)), coords[3] )
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
            else:
                left.move(7.5, 0, 0.5, 0.5)
                right.move(-7.5, 0, 0.5, 0.5)
        else:
            left.up = NT.up
            right.up = NT.up
            left_number = NT.max_degree - middle
            right_number = middle + 1
            coords = self.window.coords(NT.obj)
            left.obj = self.window.create_rectangle(coords[0], coords[1], coords[2]-(25*left_number), coords[3])
            right.obj = self.window.create_rectangle(coords[0]+(25*right_number), coords[1], coords[2], coords[3])
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
            self.window.delete(NT.obj)
            left.up.insert_node(pom)
            if left.up.nodes_num == left.up.max_degree:
                self.move_key_up(left.up)
            left.align()
    def borrow_from_parent_leaf(self, NT):
        if NT.up.nodes_num <= NT.min_degree and NT.up.up != None:
            pom = NT.up
            if pom.left != None and pom.left.up == pom.up and pom.left.nodes_num > pom.min_degree:
                pom.borrow_from_left_leaf()
            elif pom.right != None and pom.right.up == pom.up and pom.right.nodes_num > pom.min_degree:
                pom.borrow_from_right_leaf()
            else:
                self.borrow_from_parent_leaf(pom)
        if NT.left != None and NT.left.up == NT.up:
            current = NT.up
            current_coords = self.window.coords(current.obj)
            node_up = None
            for i in range(0, current.nodes_num):
                if current.nodes[i].right == NT:
                    node_up = current.nodes[i]
                    if i == 0:
                        self.window.coords(current.obj, current_coords[0] + 25, current_coords[1], current_coords[2],
                                           current_coords[3])
                        pom = current
                        while pom != None:
                            pom.move(-25, 0, 0.5, 0.5)
                            pom = pom.right
                    elif i == current.nodes_num - 1:
                        current.nodes[i - 1].right = NT
                        self.window.coords(current.obj, current_coords[0], current_coords[1], current_coords[2] - 25,
                                           current_coords[3])
                        pom = current.right
                        while pom != None:
                            pom.move(-25, 0, 0.5, 0.5)
                            pom = pom.right
                    else:
                        current.nodes[i - 1].right = NT
                        self.window.coords(current.obj, current_coords[0], current_coords[1], current_coords[2] - 25,
                                           current_coords[3])
                        pom = current.right
                        while pom != None:
                            pom.move(-25, 0, 0.5, 0.5)
                            pom = pom.right
                        for j in range(i + 1, current.nodes_num):
                            co = self.window.coords(current.nodes[j].key_obj)
                            current.nodes[j].move(co[0] - 25, co[1], 0.5, 0.5)
                    current.delete_lines()
                    current.align()
                    del current.nodes[i]
                    current.nodes_num -= 1
                    break
            if current == self.root and current.nodes_num == 0:
                self.window.delete(current.obj)
                NT.up = None
                self.root = NT
                if NT.nodes[0].left==None:
                    self.root.leaf = True
            self_coords = self.window.coords(NT.obj)
            left_coords = self.window.coords(NT.left.obj)
            self.window.delete(NT.left.obj)
            self.window.coords(NT.obj, self_coords[0] - (25 * (NT.left.nodes_num + 1)), self_coords[1],
                               self_coords[2], self_coords[3])
            self_up_coords = self.window.coords(NT.nodes[0].key_obj)
            node_up.move(self_up_coords[0] - 25, self_up_coords[1], 0.5, 0.5)
            diff = 50
            i = node_up.left.nodes_num-1
            while i >= 0:
                node_up.left.nodes[i].move(self_up_coords[0] - diff, self_up_coords[1], 0.5, 0.5)
                if node_up.left.nodes[i].left != None:
                    node_up.left.nodes[i].left.up = NT
                if node_up.left.nodes[i].right != None:
                    node_up.left.nodes[i].right.up = NT
                NT.nodes.append(node_up.left.nodes[i])
                NT.nodes_num += 1
                diff += 25
                i -=1
            node_up.left = node_up.left.nodes[node_up.left.nodes_num-1].right
            node_up.right = NT.nodes[0].left
            NT.nodes.append(node_up)
            NT.nodes_num += 1
            NT.nodes = sorted(NT.nodes, key=lambda nodes: nodes.key)
            NT.left = NT.left.left
            if NT.left != None:
                NT.left.right = NT
            po = NT.left
            while po != None:
                po.move(-12.5, 0, 0.5, 0.5)
                po = po.left
            NT.align()
            self.window.update()
            NT.create_lines()
        elif NT.right != None and NT.right.up == NT.up:
            current = NT.up
            current_coords = self.window.coords(current.obj)
            node_up = None
            for i in range(0, current.nodes_num):
                if current.nodes[i].left == NT:
                    node_up = current.nodes[i]
                    if i == 0:
                        if i+1 < current.nodes_num:
                            current.nodes[i + 1].left = NT
                        self.window.coords(current.obj, current_coords[0] + 25, current_coords[1],
                                           current_coords[2], current_coords[3])
                        pom = current
                        while pom != None:
                            pom.move(-25, 0, 0.5, 0.5)
                            pom = pom.right
                    elif i == current.nodes_num - 1:
                        self.window.coords(current.obj, current_coords[0], current_coords[1],
                                           current_coords[2] - 25, current_coords[3])
                        pom = current.right
                        while pom != None:
                            pom.move(-25, 0, 0.5, 0.5)
                            pom = pom.right
                    else:
                        current.nodes[i + 1].left = NT
                        self.window.coords(current.obj, current_coords[0], current_coords[1],
                                           current_coords[2] - 25, current_coords[3])
                        pom = current.right
                        while pom != None:
                            pom.move(-25, 0, 0.5, 0.5)
                            pom = pom.right
                        for j in range(i + 1, current.nodes_num):
                            co = self.window.coords(current.nodes[j].key_obj)
                            current.nodes[j].move(co[0] - 25, co[1], 0.5, 0.5)
                    current.delete_lines()
                    current.align()
                    del current.nodes[i]
                    current.nodes_num -= 1
                    break
            if current == self.root and current.nodes_num == 0:
                self.window.delete(current.obj)
                NT.up = None
                self.root = NT
                if NT.nodes[0].left==None:
                    self.root.leaf = True
            self_coords = self.window.coords(NT.obj)
            right_coords = self.window.coords(NT.right.obj)
            self.window.delete(NT.right.obj)
            self.window.coords(NT.obj, self_coords[0], self_coords[1],
                               self_coords[2] + (25 * (NT.right.nodes_num + 1)), self_coords[3])
            self_up_coords = self.window.coords(NT.nodes[NT.nodes_num - 1].key_obj)
            node_up.move(self_up_coords[0] + 25, self_up_coords[1], 0.5, 0.5)
            diff = 50
            node_up.left = NT.nodes[NT.nodes_num - 1].right
            for i in range(0, node_up.right.nodes_num):
                node_up.right.nodes[i].move(self_up_coords[0] + diff, self_up_coords[1], 0.5, 0.5)
                if node_up.right.nodes[i].left != None:
                    node_up.right.nodes[i].left.up = NT
                if node_up.right.nodes[i].right!= None:
                    node_up.right.nodes[i].right.up = NT
                NT.nodes.append(node_up.right.nodes[i])
                NT.nodes_num += 1
                diff += 25
            node_up.right = node_up.right.nodes[0].left
            NT.nodes.append(node_up)
            NT.nodes_num += 1
            NT.nodes = sorted(NT.nodes, key=lambda nodes: nodes.key)
            NT.right = NT.right.right
            if NT.right != None:
                NT.right.left = NT
            po = NT.right
            while po != None:
                po.move(12.5, 0, 0.5, 0.5)
                po = po.right
            self.window.update()
            #time.sleep(4)
            NT.align()
            self.window.update()
            NT.create_lines()
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
            self.root.min_degree = self.root.max_degree/2
            if self.root.max_degree % 2 == 0:
                self.root.min_degree -=1
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
                current.delete_lines()
                self.move_key_up(current)
                current.create_lines()
            else:
                current.delete_lines()
                current.create_lines()
    def find_element(self, key):
        current = self.root
        found = None
        while current != None and found == None:
            for i in range(0, current.nodes_num):
                self.window.itemconfig(current.nodes[i].key_obj, fill='red')
                self.window.update()
                #time.sleep(1)
                if current.nodes[i].key == key:
                    found = current.nodes[i]
                    break
                self.window.itemconfig(current.nodes[i].key_obj, fill='black')
                self.window.update()
                #time.sleep(1)
                if current.nodes[i].key > key:
                    current = current.nodes[i].left
                    break
                elif current.nodes[i].key < key and i == current.nodes_num -1:
                    current = current.nodes[i].right
                    break
        if found == None:
            text = self.window.create_text(50, 50, text="Node not found")
            self.window.update()
            #time.sleep(1)
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
            return None
        else:
            text = self.window.create_text(50, 50, text="Node found")
            self.window.itemconfig(found.key_obj, fill='red')
            self.window.update()
            #time.sleep(1)
            self.window.itemconfig(found.key_obj, fill='black')
            self.window.delete(text)
            self.window.update()
            #time.sleep(1)
            return current


    def find_successor(self, node):
        if node.right == None:
            return None
        else:
            current=node.right
            while current.nodes[0].left != None:
                current=current.nodes[0].left
            return current
    def find_predecessor(self, node):
        if node.left == None:
            return None
        else:
            current=node.left
            while current.nodes[current.nodes_num-1].right != None:
                current=current.nodes[current.nodes_num-1].right
            return current

    def delete_node(self, key):
        current = self.find_element(key)
        if current != None:
            it =0
            while current.nodes[it].key != key:
                it +=1
            node = current.nodes[it]
            if current.leaf == True:
                coords = self.window.coords(current.obj)
                if current.nodes_num > current.min_degree:
                    self.window.coords(current.obj, coords[0], coords[1], coords[2]-25, coords[3])
                    for i in range(it + 1, current.nodes_num):
                        co = self.window.coords(current.nodes[i].key_obj)
                        current.nodes[i].move(co[0]-25, co[1], 0.5, 0.5)
                    cur = current.right
                    while cur != None:
                        cur.move(-25, 0, 0.5, 0.5)
                        cur = cur.right
                    self.window.delete(current.nodes[it].key_obj)
                    del current.nodes[it]
                    current.nodes_num -=1
                elif current.left != None and current.left.up == current.up and current.left.nodes_num > current.min_degree:
                    current.borrow_from_left_leaf()
                    self.delete_node(key)
                elif current.right != None and current.right.up == current.up and current.right.nodes_num > current.min_degree:
                    current.borrow_from_right_leaf()
                    self.delete_node(key)
                elif current==self.root and current.nodes_num==1:
                    self.window.delete(current.nodes[0].key_obj)
                    self.window.delete(current.obj)
                    del current.nodes[0]
                    self.root=None
                else:
                    self.borrow_from_parent_leaf(current)
                    #if current.up.nodes_num == 0 and current.up == self.root:
                     #   self.window.delete(current.up.obj)
                      #  current.up = None
                       # self.root = current
                    self.delete_node(key)
                if self.root!=None:
                    current.delete_lines()
                    current.align()
                    current.create_lines()
            else:
                predecessor = self.find_predecessor(current.nodes[it])
                successor = self.find_successor(current.nodes[it])
                if predecessor != None and predecessor.nodes_num > predecessor.min_degree:
                    k = predecessor.nodes[predecessor.nodes_num-1].key
                    self.delete_node(predecessor.nodes[predecessor.nodes_num-1].key)
                    current.nodes[it].key = k
                    coords = self.window.coords(current.nodes[it].key_obj)
                    self.window.delete(current.nodes[it].key_obj)
                    current.nodes[it].key_obj = self.window.create_text(coords[0], coords[1], text=str(k))
                elif successor != None and successor.nodes_num > successor.min_degree:
                    k = successor.nodes[0].key
                    self.delete_node(successor.nodes[0].key)
                    current.nodes[it].key = k
                    coords = self.window.coords(current.nodes[it].key_obj)
                    self.window.delete(current.nodes[it].key_obj)
                    current.nodes[it].key_obj = self.window.create_text(coords[0], coords[1], text=str(k))
                else:
                    self.borrow_from_parent_leaf(successor)
                    self.delete_node(key)


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
            while current.nodes[0].left != None:
                self.window.itemconfig(current.nodes[0].key_obj, fill='red')
                self.window.update()
                time.sleep(1)
                self.window.itemconfig(current.nodes[0].key_obj, fill='black')
                self.window.update()
                time.sleep(1)
                current = current.nodes[0].left
            self.window.itemconfig(current.nodes[0].key_obj, fill='red')
            text = self.window.create_text(100, 50, text="Minimum key in this tree is: " + str(current.nodes[0].key))
            self.window.update()
            time.sleep(5)
            self.window.itemconfig(current.nodes[0].key_obj, fill='black')
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
            while current.nodes[current.nodes_num-1].right != None:
                self.window.itemconfig(current.nodes[current.nodes_num-1].key_obj, fill='red')
                self.window.update()
                time.sleep(1)
                self.window.itemconfig(current.nodes[current.nodes_num-1].key_obj, fill='black')
                self.window.update()
                time.sleep(1)
                current = current.nodes[current.nodes_num-1].right
            self.window.itemconfig(current.nodes[current.nodes_num-1].key_obj, fill='red')
            text = self.window.create_text(100, 50, text="Maximum key in this tree is: " + str(current.nodes[current.nodes_num-1].key))
            self.window.update()
            time.sleep(5)
            self.window.itemconfig(current.nodes[current.nodes_num-1].key_obj, fill='black')
            self.window.delete(text)
            self.window.update()
            time.sleep(1)






