from app.player_bst import PlayerBST
from app.player import Player

player1 = Player(1, 'Harry', 55)
player2 = Player(2, 'Ben', 35)
player3 = Player(3, 'Alice', 75)
player4 = Player(4, 'Gregory', 85)
player5 = Player(5, 'Ethan', 45)
player6 = Player(6, 'Prince', 66)
player7 = Player(7, 'George', 56)
player8 = Player(8, 'Frank', 67)
player9 = Player(9, 'Gordon', 68)
player10 = Player(10, 'Gordon', 78)

list1 = PlayerBST()
list1.insert(player1)
list1.insert(player2)
list1.insert(player3)
list1.insert(player4)
list1.insert(player5)
list1.insert(player6)
list1.insert(player7)
list1.insert(player8)
list1.insert(player9)


# Hey Raf please uncomment the lines below and run the main.py to return balance tree
# arr = list1.sorted_data()
#
# balance = list1.balance(arr)

