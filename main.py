from app.player_bst import PlayerBST
from app.player import Player
from app.player_bnode import PlayerBNode

player1 = Player(1, 'Harry', 55)
player2 = Player(2, 'Ben', 35)
player3 = Player(3, 'Alice', 75)
player4 = Player(4, 'Gregory', 85)
player5 = Player(5, 'Ethan', 45)
player6 = Player(6, 'Prince', 66)
player7 = Player(7, 'Prince', 55)

list1 = PlayerBST()
list1.insert(player1)
list1.insert(player2)
list1.insert(player3)
list1.insert(player4)
list1.insert(player5)
list1.insert(player5)
list1.insert(player6)
list1.insert(player7)

print(isinstance(list1.root, PlayerBNode))
