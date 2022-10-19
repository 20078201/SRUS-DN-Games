"""
A player module that contain a player class
"""
from argon2 import PasswordHasher, exceptions


class Player:
    """
    A class for instantiating a player object which excepts id (int) and name (string)
    """

    def __init__(self, uid: int, name: str, score: int):
        """
        :param uid: int (Cant be less than or equal to 0
        :param name: string representing the name of the player
        :param score: int (Between 0 -> 100)
        """
        self.uid = uid
        self.name = name
        self._password = None
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def __eq__(self, other):
        return self._score == other._score

    def __ge__(self, other):
        return self._score >= other._score

    def __gt__(self, other):
        return self._score > other._score

    def __ne__(self, other):
        return self._score != other._score

    def __lt__(self, other):
        return self._score < other._score

    def __le__(self, other):
        return self._score <= other._score

    def __str__(self):
        return f"Player Object (id: {self.uid}, name: {self.name}, score: {self._score}%)"

    def __repr__(self):
        return f"'Player({self.uid}, '{self.name}', {self._score})'"

    def add_password(self, password: str):
        """
        A method for adding password to the player object
        :param password: a string representing the password
        :return: a hash version of the input password
        """
        self._password = PasswordHasher().hash(password)

    def verify_password(self, password_to_be_checked: str) -> bool:
        """
        A method to verify a user entered string to the object password
        :param password_to_be_checked: a string that the method will check with object password
        :return: a boolean value
        """
        try:
            PasswordHasher().verify(self._password, password_to_be_checked)
        except exceptions.VerifyMismatchError:
            return False

    @staticmethod
    def qsort_descending(arr: []) -> []:
        """
        A static method to sort a list of players in descending orders
        :param arr: An array of ints containing players score
        :return: A sorted list players based on the scores
        """
        # base case - when the array is none or contains 1 element

        if len(arr) <= 1:
            return arr
        else:
            #  set the pivot to the first element
            pivot = arr[0]
            pivots = [x for x in arr if x == pivot]
            less = [x for x in arr[1:] if x < pivot]
            greater = [x for x in arr[1:] if x > pivot]

            # if duplicate exist then the pivots list count will be greater than 1
            if len(pivots) >= 1:
                return Player.qsort_descending(greater) + pivots + Player.qsort_descending(less)

            return Player.qsort_descending(greater) + [pivot] + Player.qsort_descending(less)
