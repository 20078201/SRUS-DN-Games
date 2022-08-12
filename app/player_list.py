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

    def append(self, node: PlayerNode):
        # Checks if self._head is empty and append an object at the head
        if not self._head:
            self._head = node
            self._tail = node  # set the tail to the value as well as the list only contains one item

            self.is_empty = False
            return

        # set the previous node to be appended
        current = self.tail
        current.next = node

        # assign the tail to new node
        self.tail = node
        self.tail.previous = current



