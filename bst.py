# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# YOUR NAME

class BinarySearchTree:
   
    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None

    def insert(self, node):
        if self.key >= node.key:
            if self.left == None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        if self.key < node.key:
            if self.right == None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def search(self, key):
        if self.key == key:
            return self
        if self.key > key and self.left != None:
            return self.left.search(key)
        if self.key < key and self.right != None:
            return self.right.search(key)
        return None

    def delete(self, key):
        if self.key == key:
            if self.right != None:
                if self.left != None:
                    self.right.insert(self.left)
                return self.right
            if self.left != None:
                return self.left
            return None
        if self.left != None and self.left.key == key:
            self.left = None
            return self
        if self.right != None and self.right.key == key:
            self.right = None
            return self
        return self

    def is_leaf(self):
        return self.left == None and self.left == None
