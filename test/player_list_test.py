import unittest

from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

node1 = PlayerNode(Player(1, "Player 1"))
node2 = PlayerNode(Player(2, "Player 2"))
node3 = PlayerNode(Player(3, "Player 3"))
node4 = PlayerNode(Player(4, "Player 4"))
node5 = PlayerNode(Player(5, "Player 5"))


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
        list1.append_forward(PlayerNode(node1))
        self.assertFalse(list1.is_empty, "Item was not appended to the list")

    def test_head(self):
        """
        Test whether the tail is equal to the inserted element when the list size is 1
        """
        list1 = PlayerList()
        list1.append_forward(node1)
        self.assertEqual(list1._tail, node1, "Your item does not match!")

    def test_tail(self):
        """
        Test if the item is inserted to the tail
        """
        list1 = PlayerList()
        list1.append_forward(node1)
        list1.append_forward(node2)

        self.assertEqual(list1.tail, node2, "Your tail node does not equal")

    def test_head_delete(self):
        """
        Test whether head is deleted
        """
        list1 = PlayerList()
        list1.append_forward(node1)
        list1.append_forward(node2)

        list1.delete_head()

        self.assertNotEqual(node1, list1.head, "Your head item has not been deleted")

    def test_tail_delete(self):
        """
        Test if tail is deleted
        """
        list1 = PlayerList()
        list1.append_forward(node1)
        list1.append_forward(node2)
        list1.append_forward(node3)
        list1.append_forward(node4)
        list1.append_forward(node5)

        list1.delete_tail()

        self.assertNotEqual(node2, list1.tail, "Your tail item has not been deleted")

    def test_delete_item_by_idx(self):
        """
        Test if item is deleted by idx
        """
        list1 = PlayerList()
        list1.append_forward(node1)
        list1.append_forward(node2)
        list1.append_forward(node3)
        list1.append_forward(node4)
        list1.append_forward(node5)

        list1.delete_item(3)

        self.assertEqual(node2.next, node4, "Your node has not been deleted in the list!")
        self.assertEqual(node4.previous, node2, "Your has not been deleted")


if __name__ == '__main__':
    unittest.main()
