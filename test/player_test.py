import unittest

from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_name(self):
        """
        Test to see if name variable are the same
        """
        player = Player('1', 'Hello World')
        name = player.name
        self.assertEqual(name, 'Hello World', 'Player name did not equal to Hello World')

    def test_player_uid(self):
        """
        Test to see if uid is equal to player uid variable
        """
        player = Player('1', 'Hello World')
        uid = player.uid
        self.assertEqual(uid, "1", "Player ")


if __name__ == "__main__":
    unittest.main()