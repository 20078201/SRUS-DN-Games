from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

        self.is_empty = True

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self._tail = value

    def append_forward(self, node: PlayerNode):
        # Checks if self._head is empty and append an object at the head
        if not self._head:
            self._head = node
            self._tail = node  # set the tail to the value as well as the list only contains one item

            self.is_empty = False
            return

        # set the previous node to be appended
        previous_node = self._tail
        previous_node.next = node

        # assign the tail to new node
        self.tail = node
        self.tail.previous = previous_node

    def append_new_head(self, node: PlayerNode):
        # Checks if self._head is empty and append an object at the head
        if not self._tail:
            self._head = node
            self._tail = node  # set the tail to the value as well as the list only contains one item

            self.is_empty = False
            return

        # set the previous node to be appended
        previous_node = self._head
        previous_node.previous = node

        # assign the tail to new node
        self.head = node
        self.head.next = previous_node

    def delete_head(self):
        # set the new head of the double link list
        self._head = self.head.next
        # set the new head previous node to None
        self._head.previous = None

    def delete_tail(self):
        # set the new tail
        self._tail = self.tail.previous
        # set the tail next node property to None
        self._tail.next = None

    def delete_item(self, idx):
        # set PlayerNode to node variable
        node = self.head

        # linear search the list until player node is found
        while node.next:
            if idx == node.key:
                break
            node = node.next

        if idx != node.key:
            print("Index out of range")
            return
        # if node is head then call delete head function
        elif not node.previous:
            self.delete_head()
        # if node is tail then call delete tail function
        elif not node.next:
            self.delete_tail()
        else:
            # left node of idx node
            node.previous.next = node.next

            # right node from idx node
            node.next.previous = node.previous

    def display(self, forward: bool = True):
        """
        Display the contents of the double link list
        :param forward: can be either set to forward or backward
        :return: list of objects in given direction
        """

        if forward:
            node = self.head
            while node.next:
                print(node)
                node = node.next
            print(node)
        elif not forward:
            node = self.tail
            while node.previous:
                print(node)
                node = node.previous
            print(node)

    def get_list_of_score(self):
        """
        A method for return a dictionary containing key: Player name and value: Score
        :return: a dictionary of player and their scores
        """
        # nodes = []
        # node = self.head
        # while node.next:
        #     nodes.append(node.player.score)
        #     node = node.next
        # else:
        #     nodes.append(node.player.score)
        # return nodes

        nodes = {}
        node = self.head
        while node.next:
            nodes[node.player.name] = node.player.score
            node = node.next
        else:
            nodes[node.player.name] = node.player.score
        return nodes

    def __iter__(self):
        """
        Dunder method for making PlayerList iterable
        """
        current = self.head
        while current is not None:
            yield current.player
            current = current.next

    def __len__(self) -> int:
        """
        Allow the list to return total number of element
        :return: The total number of element in the list. (int)
        """
        return len([player for player in self])

    def __getitem__(self, index: int) -> Player:
        """
        Get a specific item in the list by using the index number
        :param index: A number representing the location of the element in the list. (Starting from 0)
        :return: A player object
        """
        return [player for player in self][index]
