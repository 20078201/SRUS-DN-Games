from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList


def main():
    player1 = Player(1, "Player 1")

    password = "Password2"
    player1.add_password(password)
    print(player1.verify_password("Password1"))


if __name__ == '__main__':
    main()
