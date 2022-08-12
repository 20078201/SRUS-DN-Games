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

    def append(self, value):
        # Checks if self._head is empty and append an object at the head
        if not self._head:
            self._head = value
            self._tail = value  # set the tail to the value as well as the list only contains one item
            self.is_empty = False
            return self.is_empty  # should return true
        else:
            # Should return false
            return self.is_empty
