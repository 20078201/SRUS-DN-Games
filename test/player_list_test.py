import unittest

from app.player_list import PlayerList


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
        appended = list1.append(12)
        self.assertFalse(appended, "Item was not appended to the list")

    def test_head(self):
        """
        Test whether the tail is equal to the inserted element when the list size is 1
        """
        list1 = PlayerList()
        item = 12
        appended = list1.append(item)
        self.assertEqual(list1._tail, item, "Your item does not match!")


if __name__ == '__main__':
    unittest.main()
