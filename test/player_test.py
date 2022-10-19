import unittest

from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_name(self):
        """
        Test to see if name variable are the same
        """
        player = Player(1, 'Hello World', 75)
        name = player.name
        self.assertEqual(name, 'Hello World', 'Player name did not equal to Hello World')

    def test_player_uid(self):
        """
        Test to see if uid is equal to player uid variable
        """
        player = Player(1, 'Hello World', 100)
        uid = player.uid
        self.assertEqual(uid, 1, f"Player {player.uid}")

    def test_player_password_match(self):
        """
        Test password is created by checking the verification
        """
        player = Player(1, "Player 1", 55)
        password = "Password1"
        player.add_password(password)
        isVerified = player.verify_password("Password1")

        self.assertEqual(isVerified, True)

    def test_player_password_does_not_verified(self):
        """
        Test password is matching by checking the verification method
        """
        player = Player(1, "Player 1", 55)
        password = "Password1"
        player.add_password(password)
        self.assertFalse(player.verify_password("Password2"))

    def test_players_have_same_score(self):
        """
        Test if the same score
        """
        player1 = Player(1, "Player 1", 98)
        player2 = Player(2, "Player 2", 98)

        self.assertEqual(player1 == player2, True)

    def test_players_have_not_same_score(self):
        """
        Test if the score do not equal
        """
        player1 = Player(1, "Player 1", 98)
        player2 = Player(2, "Player 2", 88)

        self.assertEqual(player1 != player2, True)

    def test_players_have_greater_score(self):
        """
        Test if player 1 score is greater
        """
        player1 = Player(1, "Player 1", 98)
        player2 = Player(2, "Player 2", 98)
        player3 = Player(3, "Player 3", 97)

        self.assertEqual(player1 > player2, False)
        self.assertEqual(player1 > player3, True)

    def test_players_have_greater_equal_score(self):
        """
        Test if player1 score is greater or equal to player 2 and player 3
        """
        player1 = Player(1, "Player 1", 98)
        player2 = Player(2, "Player 2", 98)
        player3 = Player(3, "Player 3", 97)

        self.assertEqual(player1 >= player2, True)
        self.assertEqual(player1 >= player3, True)

    def test_players_have_less_score(self):
        """
        Test if the player score is less than player 3.
        For player 2 return false
        """
        player1 = Player(1, "Player 1", 60)
        player2 = Player(2, "Player 2", 75)
        player3 = Player(3, "Player 3", 55)

        self.assertEqual(player1 < player2, True)
        self.assertEqual(player1 < player3, False)

    def test_players_have_less_equal_score(self):
        """
        Test if the same score
        """
        player1 = Player(1, "Player 1", 50)
        player2 = Player(2, "Player 2", 75)
        player3 = Player(3, "Player 3", 60)

        self.assertEqual(player1 <= player2, True)
        self.assertEqual(player1 <= player3, True)

    def test_player_scores_are_descending_order(self):
        """
        Test to see if the order returned is descending
        """
        player1 = Player(1, "Player 1", 50)
        player2 = Player(2, "Player 2", 75)
        player3 = Player(3, "Player 3", 60)
        player4 = Player(4, "Player 4", 85)
        player5 = Player(5, "Player 5", 35)

        players_score = [player1.score, player2.score, player3.score, player4.score, player5.score]
        player_sorted = Player.qsort_descending(players_score)
        expected_list = [85, 75, 60, 50, 35]

        self.assertListEqual(player_sorted, expected_list,
                             f"Your sorted list did not match. \n Check your numbers in your array")


if __name__ == "__main__":
    unittest.main()
