# Step 1 - Set up local and remote git repositories (Complete)

# Step 2 Create core class and unit tests (Complete)

# Step 3 Prepare the Double-Linked List implementation (Complete)

# Step 4 Create the Player class (Complete)

# Step 5 Implement the Double-Linked List (Complete)

# Step 6 Add code optimisation (Complete)

# Step 7 Add Functionality to Double-Linked List

# Step 8 Show entire list

from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList


def main():
    list1 = PlayerList()

    list1.append_forward(PlayerNode(Player(1, "Player 1")))
    list1.append_forward(PlayerNode(Player(2, "Player 2")))
    list1.append_forward(PlayerNode(Player(3, "Player 3")))
    list1.append_forward(PlayerNode(Player(4, "Player 4")))

    list1.delete_item(4)

    print(list1.head)
    print(list1.tail)


if __name__ == '__main__':
    main()
