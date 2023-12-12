#!/usr/bin/python3
"""module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor to be initialized
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width  = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height  = value

    @property
    def x(self):
        """get the value x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value x of the rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x  = value

    @property
    def y(self):
        """get the value y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value y of the rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y  = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        area = self.width * self.height

        return area

    def display(self):
        """
        print the size of the rectangle using # character
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return the print() and str() representation of the Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assignment of attributes based on their position
        """
        if args:
            for h, arg in enumerate(args):
                if h == 0:
                    self.id = arg
                elif h == 1:
                    self.width = arg
                elif h == 2:
                    self.height = arg
                elif h == 3:
                    self.x = arg
                elif h == 4:
                    self.y = arg
                else:
                    break

        elif len(kwargs) > 0:
            for p, value in kwargs.items():
                if p == "id":
                    self.id = value
                elif p == "width":
                    self.width = value
                elif p == "height":
                    self.height = value
                elif p == "x":
                    self.x = value
                elif p == "y":
                    self.y = value
                # removed the break statement, incase if the passed args are greater
                # than 5, and one of the attributes is at the end

    def to_dictionary(self):
        """
        A dictionary representation of rectangle
        """
        rec_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

        return rec_dict


if __name__ == "__main__":
    pass
