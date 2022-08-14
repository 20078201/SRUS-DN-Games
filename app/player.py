class Player:
    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.name = name

    def __str__(self):
        return f"Player (id: {self.uid})"
