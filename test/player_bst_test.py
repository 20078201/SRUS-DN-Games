import unittest
from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST
from app.player import Player


class TestPlayerBST(unittest.TestCase):
    def setUp(self) -> None:
        self.player1 = Player(1, 'Harry', 55)
        self.player2 = Player(2, 'Ben', 35)
        self.player3 = Player(3, 'Alice', 75)
        self.player4 = Player(4, 'Gregory', 85)
        self.player5 = Player(5, 'Ethan', 45)
        self.player6 = Player(6, 'Prince', 66)
        self.player7 = Player(7, 'Prince', 55)

        self.list1 = PlayerBST()

    def test_insert_left_branch(self):
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)

        expected = Player(2, 'Ben', 33)
        actual = self.list1.root.left_branch.data.name

        self.assertEqual(expected.name, actual, "Player 2 is not on left branch")

    def test_insert_right_branch(self):
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)
        self.list1.insert(self.player6)

        expected = Player(6, 'Prince', 66)
        actual = self.list1.root.right_branch.data.name

        self.assertEqual(expected.name, actual, "Player 6 is not on right branch")

    def test_insert_is_SubTree(self):
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)
        self.list1.insert(self.player6)

        expected = True
        actual = isinstance(self.list1.root.right_branch, PlayerBNode)

        self.assertEqual(expected, actual, "Branch is not a sub tree")

    def test_insert_duplicate(self):
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)
        self.list1.insert(self.player6)
        self.list1.insert(self.player7)

        expected = Player(7, 'Prince', 66)
        actual = self.list1.root.right_branch.data.name

        self.assertEqual(expected.name, actual, "Your node player object was not overwritten")
