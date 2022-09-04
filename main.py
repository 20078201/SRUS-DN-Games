from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList
from app.plot import find_max_square_dimension

import random


def main():
    player1 = Player(1, "Player 1", 98)
    player2 = Player(2, "Player 2", 45)
    player3 = Player(3, "Player 3", 25)
    player4 = Player(4, "Player 4", 50)
    player5 = Player(5, "Player 5", 100)
    player6 = Player(6, "Player 6", 25)

    mylist = PlayerList()
    mylist.append_forward_from_tail(PlayerNode(player1))
    mylist.append_forward_from_tail(PlayerNode(player2))
    mylist.append_forward_from_tail(PlayerNode(player3))
    mylist.append_forward_from_tail(PlayerNode(player4))
    mylist.append_forward_from_tail(PlayerNode(player5))
    mylist.append_forward_from_tail(PlayerNode(player6))

    for x in mylist:
        print(x)


if __name__ == '__main__':
    main()
