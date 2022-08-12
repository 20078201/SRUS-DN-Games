import unittest

from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_is_empty(self):
        """
        Test whether head of the list is empty
        """
        list1 = PlayerList()

        self.assertTrue(list1.is_empty)

    def test_is_not_empty(self):
        """
        Test whether an object is appended to the item which will return true
        """
        list1 = PlayerList()
        list1.append(12)
        self.assertFalse(list1.is_empty, "Item was not appended to the list")

    def test_head(self):
        """
        Test whether the tail is equal to the inserted element when the list size is 1
        """
        list1 = PlayerList()
        item = 12
        appended = list1.append(item)
        self.assertEqual(list1._tail, item, "Your item does not match!")

    def test_tail(self):
        """
        Test if the item is inserted to the tail
        """
        node1 = PlayerNode(Player("1", "Player 1"))
        node2 = PlayerNode(Player("1", "Player 1"))

        list1 = PlayerList()
        list1.append(node1)
        list1.append(node2)

        self.assertEqual(list1.tail, node2, "Your tail node does not equal")


if __name__ == '__main__':
    unittest.main()
