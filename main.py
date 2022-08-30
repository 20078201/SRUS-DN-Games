from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList


def main():
    player1 = Player(1, "Player 1", 100)
    player2 = Player(2, "Player 2", 100)

    print(player1 == player2)


if __name__ == '__main__':
    main()
