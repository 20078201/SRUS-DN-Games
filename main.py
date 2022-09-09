from collections import deque


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.occupied = False

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

    def __repr__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data: list):
        self.list1 = deque(tuple(tree_data))

    def data(self):
        arr = self.list1
        if len(arr) == 1:
            parent_node = TreeNode(arr.popleft())
            return parent_node
        else:
            parent_node = TreeNode(arr.popleft())
            while arr:
                if not parent_node.occupied:
                    value = arr.popleft()
                    if value <= parent_node.data:
                        parent_node.left = TreeNode(value)
                    elif value > parent_node.data:
                        parent_node.right = TreeNode(value)
                if parent_node.left and parent_node.right:
                    parent_node.occupied = True
            return parent_node

    def sorted_data(self):
        pass


a = BinarySearchTree(['4', '2', '5'])

print(a.data())

