# Name: Jeffery Ho
# Section: 202 - 11

# A TreeNode is a class
# A left is a TreeNode
# A right is a TreeNode
# A Key is a number
# A data is none
# TreeNode takes a key as a number and returns a Node
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None


    # insert is a method
    # number -> None
    # Takes in a key and returns nothing. Inserts a new node with that key in the correct position
    def insert(self, key):
    # inserts a node with key into the correct position if not a duplicate.
        if self == None:
            return TreeNode(key)

        else:
            if key < self.key:
                if self.left == None:
                    self.left = TreeNode(key)
                else:
                    self.left.insert(key)
            else:
                if self.right == None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)

    # find_successor is a method
    # Class -> TreeNode
    # Takes in nothing and returns the successor to the current TreeNode
    def find_successor(self):
    # returns the node that is the inorder successor of the node def
        current = self.right
        while (current.left != None):
            current = current.left

        return current

    # find_min is a method
    # class -> number
    # Takes in nothing and returns the minimum node of the tree
    def find_min(self, min = None):
    # returns min value in the tree
        min = self.key
        if self.left == None:
            return min
        else:
            return self.left.find_min(min)

    # find_max is a method
    # class -> number
    # Takes in nothing and returns the maximum node of the tree
    def find_max(self, max = None):
    # returns max value in the tree
        max = self.key
        if self.right == None:
            return max
        else:
            return self.right.find_max(max)

    # inorder_print_tree is a method
    # class -> None
    # Takes in nothing and prints the tree in Inorder
    def inorder_print_tree(self):
    # print inorder the subtree of self
        if self:
            if self.left != None:
                self.left.inorder_print_tree()
            print(self.key)
            if self.right != None:
                self.right.inorder_print_tree()

    # print_levels is a method
    # class -> None
    # Takes in nothing and prints each key of the node and level of the node in a list
    def print_levels(self, level = 0):
    #inorder traversal prints list of pairs, [key, level of the node] where root is level 0
        if self:
            if self.left != None:
                self.left.print_levels(level + 1)
            print([self.key, level])
            if self.right != None:
                self.right.print_levels(level + 1)


# A BinarySearchTree is a class
# # A left is a TreeNode
# A right is a TreeNode
# A Key is a number
# A data is none
# A root is the node a level 0
class BinarySearchTree:
    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.key = key
        self.data = None
        self.root = None

    # A find is a method
    # Number -> Boolean
    # Takes in a key as a number and returns true if the key is in a node of the tree, else false
    def find (self, key):
    # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        else:
            if self.key == key:
                return True
            if self.key > key:
                if self.left != None:
                    return self.left.find(key)
            if self.key < key:
                if self.right != None:
                    return self.right.find(key)
        return None



    # A insert is a method
    # Number -> None
    # Takes in a key as a number and inserts the new node in the correct position of the tree
    def insert(self, newkey):
        if self.is_empty():
            self.key = newkey
            self.root = self

        else:
            if newkey < self.key:
                if self.left == None:
                    self.left = BinarySearchTree(newkey)
                    self.left.root = self.root
                else:
                    self.left.insert(newkey)
            if newkey > self.key:
                if self.right == None:
                    self.right = BinarySearchTree(newkey)
                    self.right.root = self.root
                else:
                    self.right.insert(newkey)

    # A delete is a method
    # Number -> None
    # Takes in a key and removes the node with that key form the tree
    # Then finds the successor, the minimum of the right subtree of the deleted node
    # And replace the deleted node with the successor
    def delete(self, key):

        def minValueNode(node):
            current = node

            while (current.left != None):
                current = current.left

            return current

        if self.is_empty():
            return self

        if key < self.key:
            self.left = self.left.delete(key)

        elif key > self.key:
            self.right = self.right.delete(key)

        else:
            if self.right == self.left == None:
                self = None
                return None
            if self.left == None and self.right != None:
                temp = self.right
                self = None
                return temp

            elif self.right == None and self.left != None:
                temp = self.left
                self = None
                return temp

            temp = minValueNode(self.right)
            self.key = temp.key
            self.right = self.right.delete(temp.key)

    # A print_tree is a method
    # Class -> None
    # Takes in nothing and prints the tree in Inorder
    def print_tree(self):
    # print inorder the entire tree

        if self:
            if self.left != None:
                self.left.print_tree()
            print(self.key)
            if self.right != None:
                self.right.print_tree()

    # A is_empty is a method
    # Class -> Boolean
    # Takes in nothing and returns True if all the instance variable are None
    def is_empty(self):
    #returns True if tree is empty, else False
        if self.data == self.left == self.right == self.key == self.root == None:
            return True
        else:
            return False
