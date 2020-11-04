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
            if self.parent != None:
                if self.parent.left == self:
                    self.parent.left = None
                if self.parent.right == self:
                    self.parent.right = None
            if self.has_right_child():
                if self.has_left_child():
                    self.right.insert(self.left)
                self.right.parent = None
                if self.parent != None:
                    self.parent.insert(self.right)
                return self.right
            if self.has_left_child():
                self.left.parent = None
                if self.parent != None:
                    self.parent.insert(self.left)
                return self.left
            return None
        if self.key > key and self.has_left_child():
            self.left.delete(key)
        if self.key < key and self.has_right_child():
            self.right.delete(key)
        return self

    def is_leaf(self):
        return self.left == None and self.right == None

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def minimum(self):
        if self.has_left_child():
            return self.left.minimum()
        return self
