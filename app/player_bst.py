from collections import deque
from player_bnode import TreeNode


class BinarySearchTree:
    """
    A class for making a binary search tree object
    """

    def __init__(self, tree_data):
        tree_data = deque(tree_data)
        self.root = None
        # A while loop for generating the binary search tree with input data (tree_data)
        while tree_data:
            data = tree_data.popleft()
            self.insert(data)

    def data(self):
        """
        Call data method to return an unsorted list
        :return: unsorted list
        """
        return self.root

    def sorted_data(self):
        """
        Takes the current tree and sort the data
        :return: a sorted list of numbers of type string in ascending order
        """
        sorted_array = []
        if self.root:
            self.root.inorder(self.root, sorted_array)
            return sorted_array

    def insert(self, data):
        """
        A method for inserting new tree nodes in the binary search tree
        :param data: a number of type string
        :return: void
        """
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = TreeNode(data)
