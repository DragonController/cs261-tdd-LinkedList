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
            self.left = node
            node.parent = self
        if self.key < node.key:
            self.right = node
            node.parent = self

    def search(self, key):
        if self.key == key:
            return self
        return None

    def delete(self, key):
        if self.key == key:
            return None
        return self
