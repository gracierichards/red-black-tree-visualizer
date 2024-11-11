from enum import Enum
import sys
import networkx as nx
import matplotlib.pyplot as plt

class Color(Enum):
    BLACK = 0
    RED = 1

class Nil:
    def __init__(self):
        self.value = None
        self.color = Color.BLACK

    def isNil(self):
        return True
    
    def sort(self):
        return []
    
    def search(self):
        return None

class Node:
    def __init__(self, value, p, left=Nil(), right=Nil(), color=Color.BLACK):
        self.value = value
        self.p = p
        self.left = left
        self.right = right
        self.color = color

    def isNil(self):
        return False

    """Returns the newly created child node"""
    def addLeftChild(self, value, color=Color.BLACK):
        newNode = Node(value=value, p=self, color=color)
        self.left = newNode
        return newNode

    """Returns the newly created child node"""
    def addRightChild(self, value, color=Color.BLACK):
        newNode = Node(value=value, p=self, color=color)
        self.right = newNode
        return newNode

    """Returns an array with all elements of the subtree rooted at this node in sorted order."""
    def sort(self):
        if not self.left.isNil():
            left_side = self.left.sort()
        else:
            left_side = []
        if not self.right.isNil():
            right_side = self.right.sort()
        else:
            right_side = []
        return left_side + [self.value] + right_side
    
    """Returns the node with the given value, if it exists. Else returns None"""
    def search(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.left.isNil():
                print("Node not found.")
                return None
            return self.left.search(value)
        else:
            if self.right.isNil():
                print("Node not found.")
                return None
            return self.right.search(value)
        
    """Returns the node with minimum value in the subtree rooted at this node"""
    def min(self):
        if not self.left.isNil():
            return self.left.min()
        else:
            return self
        
    """Returns the node with maximum value in the subtree rooted at this node"""
    def max(self):
        if not self.right.isNil():
            return self.right.max()
        else:
            return self
        
    """Returns the successor of this node in the overall tree. Returns none if there is no successor."""
    def successor(self):
        if not self.right.isNil():
            return self.right.min()
        x = self
        y = self.p
        while not y.isNil() and x == y.right:
            x = y
            y = y.p
        return y
    
    """Returns the predecessor of this node in the overall tree. Returns none if there is no predecessor."""
    def predecessor(self):
        if not self.left.isNil():
            return self.left.max()
        x = self
        y = self.p
        while not y.isNil() and x == y.left:
            x = y
            y = y.p
        return y
    
    def height(self, total):
        if self.left.isNil():
            left_height = 0
        else:
            left_height = self.left.height(total + 1)
        if self.right.isNil():
            right_height = 0
        else:
            right_height = self.right.height(total + 1)
        return max(total, left_height, right_height)

# Everything in the left subtree of a node is <= the value of the node. Everything in the right subtree of the node is > the value of the node.
class RBTree:
    def __init__(self):
        self.sentinel = Nil()
        self.root = self.sentinel

    """Returns an array with all elements of the tree in sorted order."""
    def sort(self):
        return self.root.sort()
    
    """Returns the node with the given value, if it exists. Else returns None"""
    def search(self, value):
        return self.root.search(value)
    
    """Replaces the subtree rooted at node u with the subtree rooted at node v"""
    def transplant(self, u, v):
        if u.p.isNil():
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    """Finds a node with the given value and deletes it from the tree"""
    def delete_value(self, value):
        node = self.search(value)
        if node:
            self.delete(node)
    
    """Deletes node z from the tree, then performs the fixes to maintain the red black properties"""
    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left.isNil():
            x = z.right
            self.transplant(z, z.right)
        elif z.right.isNil():
            x = z.left
            self.transplant(z, z.left)
        else:
            y = z.right.min()
            y_original_color = y.color
            x = y.right
            if y != z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            else:
                x.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self.rotate_left(x.p)
                    w = x.p.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.rotate_right(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.rotate_left(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self.rotate_right(x.p)
                    w = x.p.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.rotate_left(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.rotate_right(x.p)
                    x = self.root
        x.color = Color.BLACK
    
    """Performs the ROTATE-LEFT operation at node x"""
    def rotate_left(self, x):
        y = x.right
        if y.isNil():
            print("Cannot rotate at this location.")
            sys.exit()
        if x.p.isNil():
            self.root = y
        else:
            if x == x.p.left:
                x.p.left = y
            else:
                x.p.right = y
        y.p = x.p
        if not y.left.isNil():
            y.left.p = x
        x.right = y.left

        x.p = y
        y.left = x

    """Performs the ROTATE-RIGHT operation at node x"""
    def rotate_right(self, x):
        y = x.left
        if y.isNil():
            print("Cannot rotate at this location.")
            sys.exit()
        if x.p.isNil():
            self.root = y
        else:
            if x == x.p.left:
                x.p.left = y
            else:
                x.p.right = y
        y.p = x.p
        if not y.right.isNil():
            y.right.p = x
        x.left = y.right

        x.p = y
        y.right = x

    """Inserts the given value into the tree, then performs the fixes to maintain the red black properties"""
    def insert(self, value):
        # Basic BST procedure
        z = Node(value, p=None, color=Color.RED)
        x = self.root
        y = self.sentinel
        while not x.isNil():
            y = x
            if value <= x.value:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y.isNil():
            self.root = z
        elif value <= y.value:
            y.left = z
        else:
            y.right = z

        # Fixes
        while z.p.color == Color.RED:
            if z.p == z.p.p.left:
                uncle = z.p.p.right
                if uncle.color == Color.RED:
                    z.p.color = Color.BLACK
                    uncle.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.rotate_left(z)
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.rotate_right(z.p.p)
            else:
                uncle = z.p.p.left
                if uncle.color == Color.RED:
                    z.p.color = Color.BLACK
                    uncle.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rotate_right(z)
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.rotate_left(z.p.p)
        self.root.color = Color.BLACK

    """Returns the height (length of the longest branch of the tree)"""
    def height(self):
        return self.root.height(0)

"""Returns the matplotlib figure"""
def visualize(root):
    fig = plt.figure()
    
    G = nx.Graph()
    node_colors = []
    i = 0
    labels = {}

    def add_nodes(node):
        nonlocal i
        if not node.isNil():
            if node.color == Color.BLACK:
                color = "black"
            else:
                color = "red"
            cur_node_id = i
            G.add_node(cur_node_id, color=color)
            labels[cur_node_id] = node.value
            i += 1
            node_colors.append(color)
            if not node.left.isNil():
                G.add_edge(cur_node_id, i)
                add_nodes(node.left)
            if not node.right.isNil():
                G.add_edge(cur_node_id, i)
                add_nodes(node.right)
    
    add_nodes(root)
    pos = nx.nx_pydot.pydot_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, labels = labels, node_color = node_colors, font_color="white")
    return fig