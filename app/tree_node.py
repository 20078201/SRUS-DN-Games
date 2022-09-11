class TreeNode:
    """
    A class for making tree nodes for a binary search tree
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # String comparison works on the first letter of the string
    # https://stackoverflow.com/questions/58531100/why-5-is-greater-than-10-python
    def insert(self, data):
        """
        A method for recursively inserting tree node object to the Binary Search Tree
        :param data: a number value that is type string
        :return: void
        """
        if int(data) <= int(self.data):  # check to see if the root Node data value is greater than the value inputted
            if self.left is not None:  # if the left is occupied
                self.left.insert(data)  # if occupied then recursively call insert method
            else:
                self.left = TreeNode(data)  # then assign a node with that data
        elif int(data) > int(self.data):
            if self.right is not None:  # if the right node of root is occupied,
                self.right.insert(data)
            else:
                self.right = TreeNode(data)  # if not then assign a node with that data

    def inorder(self, currentNode, sorted_array):
        """
        A function for creating a sorted array from a binary search tree
        :param currentNode: TreeNode object
        :param sorted_array: Array
        :return: a sorted array of numbers in ascending order
        """
        if currentNode:  # check if currentNode is a TreeNode
            self.inorder(currentNode.left,
                         sorted_array)  # if yes, recursively call the inorder method on the left branch until no
            # node is found
            sorted_array.append(currentNode.data)  # append the tree node data to the array

            self.inorder(currentNode.right, sorted_array)  # recursively call the inorder method on the left branch
            # until no node is found

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

    def __repr__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
