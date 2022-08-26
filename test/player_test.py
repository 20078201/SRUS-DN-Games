import unittest

import argon2.exceptions

from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_name(self):
        """
        Test to see if name variable are the same
        """
        player = Player(1, 'Hello World')
        name = player.name
        self.assertEqual(name, 'Hello World', 'Player name did not equal to Hello World')

    def test_player_uid(self):
        """
        Test to see if uid is equal to player uid variable
        """
        player = Player(1, 'Hello World')
        uid = player.uid
        self.assertEqual(uid, 1, f"Player {player.uid}")

    def test_player_password_match(self):
        """
        Test password is created by checking the verification
        """
        player = Player(1, "Player 1")
        password = "Password1"
        player.add_password(password)
        isVerified = player.verify_password("Password1")

        self.assertEqual(isVerified, True)

    def test_player_password_does_not_verified(self):
        """
        Test password is matching by checking the verification method
        """
        with self.assertRaises(argon2.exceptions.VerifyMismatchError):
            player = Player(1, "Player 1")
            password = "Password1"
            player.add_password(password)
            player.verify_password("Password2")


if __name__ == "__main__":
    unittest.main()
