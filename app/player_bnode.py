from .player import Player


class PlayerBNode:
    """
    A class for making tree nodes for a binary search tree
    """

    def __init__(self, data: Player, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    # String comparison works on the first letter of the string
    # https://stackoverflow.com/questions/58531100/why-5-is-greater-than-10-python
    def insert(self, data: Player):
        """
        A method for recursively inserting tree node object to the Binary Search Tree
        :param data: a number value that is type string
        :return: void
        """
        # Check if key are the same
        if data == self._data:
            # print(f"{data.name} is the same as {self._data}")
            self.data = data
        # check to see if the root Node data value is greater than the value inputted
        elif data <= self._data:
            if self._left is not None:  # if the left is occupied
                self._left.insert(data)  # if occupied then recursively call insert method
            else:
                self._left = PlayerBNode(data)  # then assign a node with that data
        elif data > self._data:
            if self._right is not None:  # if the right node of root is occupied,
                self._right.insert(data)
            else:
                self._right = PlayerBNode(data)  # if not then assign a node with that data

    def inorder(self, currentNode, sorted_array):
        """
        A function for creating a sorted array from a binary search tree
        :param currentNode: TreeNode object
        :param sorted_array: Array
        :return: a sorted array of numbers in ascending order
        """
        if currentNode:  # check if currentNode is a TreeNode
            self.inorder(currentNode._left,
                         sorted_array)  # if yes, recursively call the inorder method on the left branch until no
            # node is found
            sorted_array.append(currentNode.data)  # append the tree node data to the array

            self.inorder(currentNode._right,
                         sorted_array)  # recursively call the inorder method on the left branch
            # until no node is found

    def search(self, currentNode, player: Player):
        if currentNode is None:
            raise ValueError

        if currentNode.data == player:
            return currentNode.data

        if currentNode.data < player:
            return self.search(currentNode._right, player)

        return self.search(currentNode._left, player)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def left_branch(self):
        return self._left

    @left_branch.setter
    def left_branch(self, value):
        self._left = value

    @property
    def right_branch(self):
        return self._right

    @right_branch.setter
    def right_branch(self, value):
        self._right = value

    def __str__(self):
        return f'TreeNode(data={self._data}, left={self._left}, right={self._right})'

    def __repr__(self):
        return f'TreeNode(data={self._data}, left={self._left}, right={self._right})'
