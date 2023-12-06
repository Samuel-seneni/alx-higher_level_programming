#!/usr/bin/python3
"""Definition of a rectangle subclass """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size):
        """ A new square is initialized.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
