import unittest

from app.player_list import PlayerList


class TestPlayer(unittest.TestCase):
    def test_is_empty(self):
        """
        Test whether head of the list is empty
        """
        list1 = PlayerList()

        self.assertFalse(list1.is_empty)

    def test_is_not_empty(self):
        list1 = PlayerList()
        list1.append(12)


if __name__ == '__main__':
    unittest.main()
