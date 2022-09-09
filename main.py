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
            # Loop for the array until empty
            while arr:
                # take the left most item in the deque and set it to value
                value = arr.popleft()

                # Determine which branch to follow by comparing the value to the parent node data (In this case '4')
                if value <= parent_node.data:  # Travel left of parent Node
                    if parent_node.left is None:
                        parent_node.left = TreeNode(value)

                    child_node = parent_node.left
                    if value <= child_node.data:
                        child_node.left = TreeNode(value)
                    elif value > child_node.data:
                        child_node.right = TreeNode(value)

                elif value > parent_node.data:  # Travel right of parent Node
                    if parent_node.right is None:
                        parent_node.right = TreeNode(value)

                    child_node = parent_node.right
                    if value <= child_node.data:
                        child_node.left = TreeNode(value)
                    elif value > child_node.data:
                        child_node.right = TreeNode(value)

            return parent_node

    def sorted_data(self):
        pass


a = BinarySearchTree(['4', '2', '5', '1', '6'])

print(a.data())
