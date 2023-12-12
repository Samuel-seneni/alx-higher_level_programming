#!/usr/bin/python3
"""Definition of a claas models."""
import json
import csv
import turtle


class Base:
    """A representation of the base to the object oriented programming."""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        to_json = json.dumps(list_dictionaries)
        return to_json

    @staticmethod
    def from_json_string(json_string):
        """JSON string to object"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save jsonfied object to file."""
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """loads strinf from file"""
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())

                list_instances = []

                for d in list_dicts:
                    list_instances.append(cls.create(**d))
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                new_list_dict = []
                converted_dict = {}
                for d in list_dicts:
                    for key, value in d.items():
                        converted_dict[key] = int(value)

                    new_list_dict.append(converted_dict)

                list_dicts = new_list_dict

                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls.create(**d))

                return list_of_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

if __name__ == "__main__":

    pass
