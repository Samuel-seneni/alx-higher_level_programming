#!/usr/bin/python3
"""module for rectangle class"""
from models.rectangle import Rectangle


class Rectangle(Base):
    """A Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            self.validate_integer("width", value, False)
            self.__width = value

        @property
        def height(self):
            """height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            self.validate_integer("width", value, False)
            self.__height = value

        @property
        def x(self):
            """x of the rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            self.validate_integer("x", value)
            self.__x = value

        @property
        def y(self):
            """y of the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            self.validate_integer("y", value)
            self.__y = value

        def validate_integer(slef, name, value, eq=True):
            """validation of the value"""
            if type(value) != int:
                raise TypeError("() must be an integer".format(name))
            if eq and value < 0:
                raise ValueError("() must be >= 0".format(name))

        def area(self):
            """computes the area of the rectangle"""
            return self.width * self.height

        def display(self):
            """prints string representation of the Rectangle"""
            if self.width == 0 or  self.height == 0:
                print("")
                return

        [print("") for y in range(self.y)]
        for p in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for width in range(self.width)]
            print("")

        def update(self, *args, **kwargs):
            """update the class rectangle.

            args:
                *args (ints): New attribute values.
                    1st argument should be the id attribute
                    2nd argument should be the width attribute
                    3rd argument should be the height attribute
                    4th argument should be the x attribute
                    5th argument should be the y attribute
                **kwargs (dict): New key values attributes.
            """
        if args and len(args) != 0:
            h = 0
            for arg in args:
                if h == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif h == 1:
                    self.width = arg
                elif h == 2:
                    self.height = arg
                elif h == 3:
                    self.x = arg
                elif h == 4:
                    self.y = arg
                h += 1

        elif kwargs and len(kwargs) != 0:
            for d, v in kwargs.items():
                if d == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif d == "width":
                    self.width = v
                elif d == "height":
                    self.height = v
                elif d == "x":
                    self.x = v
                elif d == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
