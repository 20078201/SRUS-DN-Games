from collections import deque
from .player_bnode import PlayerBNode
from .player import Player


class PlayerBST:
    """
    A class for making a binary search tree object
    """

    def __init__(self):
        # tree_data = deque(tree_data)
        self.root = None
        # A while loop for generating the binary search tree with input data (tree_data)
        # while tree_data:
        #     data = tree_data.popleft()
        #     self.insert(data)

    def data(self):
        """
        Call data method to return an unsorted list
        :return: unsorted list
        """
        return self.root

    def sorted_data(self):
        """
        Takes the current tree and sort the data
        :return: an array of sorted numbers in ascending order
        """
        sorted_array = []
        if self.root:
            self.root.inorder(self.root, sorted_array)
            return sorted_array

    def split_list(self, arr, mid):
        lower = arr[:mid]
        upper = arr[mid:]

        return lower, upper

    def balance(self, arr: [Player]):
        # if len(arr) <= 0:
        #     return None
        # middle = len(arr) // 2
        # lower, upper = self.split_list(arr, )
        #
        # subtree_root = PlayerBNode(arr.pop(middle))
        # subtree_root.left_branch = self.balance(arr)
        # subtree_root.right_branch = self.balance(arr)
        # return subtree_root
        if len(arr) == 1:
            return PlayerBNode(arr[0])
        elif len(arr) == 0:
            return None
        else:
            mid_index = len(arr) // 2
            middleElement = arr[mid_index]
            #  set the pivot to the first element
            subtree_root = PlayerBNode(middleElement)

            # Need to add and minus 1 to not include the middle index when we split array
            subtree_root.left_branch = self.balance(arr[:mid_index])
            subtree_root.right_branch = self.balance(arr[mid_index + 1:])

            return subtree_root

    def insert(self, data: Player):
        """
        A method for inserting new tree nodes in the binary search tree
        :param data: Player object
        :return: void
        """
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = PlayerBNode(data)

    def search(self, player: Player) -> Player | None:
        if self.root is None:
            return self.root
        elif self.root.data == player:
            return self.root.data

        # Call the function from player_bnode
        return self.root.search(self.root, player)
