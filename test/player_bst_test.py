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
        self.player8 = Player(8, 'Frank', 67)
        self.player9 = Player(9, 'Gordon', 68)
        self.player10 = Player(10, 'Alex', 12)

        self.list1 = PlayerBST()
        self.list2 = PlayerBST()
        self.list2.insert(self.player1)
        self.list2.insert(self.player2)
        self.list2.insert(self.player3)
        self.list2.insert(self.player4)
        self.list2.insert(self.player5)
        self.list2.insert(self.player6)
        self.list2.insert(self.player7)
        self.list2.insert(self.player8)
        self.list2.insert(self.player9)

    def test_insert_left_branch(self):
        """
        Test to see if player was inserted on the left branch
        """
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)

        expected = Player(2, 'Ben', 33)
        actual = self.list1.root.left_branch.data.name

        self.assertEqual(expected.name, actual, "Player 2 is not on left branch")

    def test_insert_right_branch(self):
        """
        Test to see if player was inserted on the right branch
        """
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)
        self.list1.insert(self.player6)

        expected = Player(6, 'Prince', 66)
        actual = self.list1.root.right_branch.data.name

        self.assertEqual(expected.name, actual, "Player 6 is not on right branch")

    def test_insert_is_SubTree(self):
        """
        Test to see if the player inserted is also a TreeNode object
        """
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)
        self.list1.insert(self.player6)

        expected = True
        actual = isinstance(self.list1.root.right_branch, PlayerBNode)

        self.assertEqual(expected, actual, "Branch is not a sub tree")

    def test_insert_duplicate(self):
        """
        Test to see if node object is updated
        """
        self.list1.insert(self.player1)
        self.list1.insert(self.player2)
        self.list1.insert(self.player6)
        self.list1.insert(self.player7)

        expected = Player(7, 'Prince', 66)
        actual = self.list1.root.right_branch.data.name

        self.assertEqual(expected.name, actual, "Your node player object was not overwritten")

    def test_search_for_player(self):
        """
        Test to see if we can find a specific player object in BST
        """
        actual = self.list2.search(self.player9)
        expected = self.player9

        self.assertEqual(actual, expected, "Not matching")

    def test_search_for_player_root(self):
        """
        Test to see if function will return the root when we search for root player node
        """
        actual = self.list2.search(self.player1)
        expected = self.list2.root.data

        self.assertEqual(actual, expected, "The root of the tree was not return")

    def test_search_player_not_in_tree(self):
        """
        Test to see if a ValueError will occur. i.e when the player cannot be found in the BST
        """
        with self.assertRaises(ValueError):
            self.list2.search(self.player10)
