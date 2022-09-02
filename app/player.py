"""
A player module that contain a player class
"""

from argon2 import PasswordHasher


class Player:
    """
    A class for instantiating a player object which excepts id (int) and name (string)
    """

    def __init__(self, uid: int, name: str, score: int):
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
        return f"Player (id: {self.uid})"

    def add_password(self, password: str):
        """
        A method for adding password to the player object
        :param password: a string representing the password
        :return: a hash version of the input password
        """
        self._password = PasswordHasher().hash(password)

    def verify_password(self, password_to_be_checked: str):
        """
        A method to verify a user entered string to the object password
        :param password_to_be_checked: a string that the method will check with object password
        :return: a boolean value
        """

        return PasswordHasher().verify(self._password, password_to_be_checked)

    @classmethod
    def qsort(cls, arr):
        """
        A static method to sort a list of players in descending orders
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
                return cls.qsort(greater) + pivots + cls.qsort(less)
            else:
                return cls.qsort(greater) + [pivot] + cls.qsort(less)
