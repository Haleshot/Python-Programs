# C++ program to demonstrate insertion
# in a BST recursively.

from lib2to3.pytree import Node
from logging.config import valid_ident
from turtle import left, right

# Class for defining the structure of BST which includes the root values present
# on either side of the main root value and the value
class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def Insert_BST(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            print("Duplicates not allowed!\n")
        elif root.val > key:
            root.left = Insert_BST(root.left, key)
        elif root.val < key:
            root.right = Insert_BST(root.right, key)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val)
        Inorder(root.right)

def main():
    
