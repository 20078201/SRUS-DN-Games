from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList


def main():
    list1 = PlayerList()

    list1.append_forward(PlayerNode(Player(1, "Player 1")))
    list1.append_forward(PlayerNode(Player(2, "Player 2")))
    list1.append_forward(PlayerNode(Player(3, "Player 3")))
    list1.append_forward(PlayerNode(Player(4, "Player 4")))


if __name__ == '__main__':
    main()
