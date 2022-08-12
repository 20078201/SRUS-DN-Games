class PlayerList:
    def __init__(self):
        self.head = None
        self.is_empty = True

    def append(self, value):
        # Checks if self.head is empty and append a object at the head
        if not self.head:
            self.head = value
            self.is_empty = False
            return self.is_empty  # should return true
        else:
            # Should return true
            return self.is_empty
