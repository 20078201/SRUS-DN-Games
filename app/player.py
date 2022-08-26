"""
A player module that contain a player class
"""

from argon2 import PasswordHasher


class Player:
    """
    A class for instantiating a player object which excepts id (int) and name (string)
    """

    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.name = name
        self._password = None

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
