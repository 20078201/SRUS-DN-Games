class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self._player.uid

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @player.setter
    def player(self, value):
        self._player = value

    @next.setter
    def next(self, value):
        self._next = value

    @previous.setter
    def previous(self, value):
        self._previous = value

    def __str__(self):
        return f"{self._player}"

    def __repr__(self):
        return f"Node (player:{self._player}, next:{self._next}, previous:{self._previous})"

