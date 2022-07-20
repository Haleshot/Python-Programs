# Class for defining the structure of BST which includes the root values present
# on either side of the main root value and the value
class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def Insert_BST(root, key):
    if root is None:
        return BinarySearchTree(key)
    else:
        if root.val == key or root is None:
            return root
        elif root.val > key:
            root.left = Insert_BST(root.left, key)
        elif root.val < key:
            root.right = Insert_BST(root.right, key)
        return root

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val)
        Inorder(root.right)

def main():
    p = BinarySearchTree(20)
    root = None
    while True:
        print("\nThe Menu is : ")
        print("1. Insert a value in the BST\n2. Display the BST\n3. Exit\n")
        ch = int(input("Enter the choice : "))

        if ch == 1:
            value = int(input("Enter the value to be entered into the BST : "))
            root = Insert_BST(root, value)
        
        elif ch == 2:
            Inorder(root)
        
        elif ch == 3:
            exit(0)

        else:
            print("Invalid Choice!\n")
main()