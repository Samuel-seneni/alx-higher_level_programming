#!/usr/bin/python3
"""Defines modules for text indentation method"""


def text_indentation(text):
    """method of adding two new lines after ., ? and : characters.

    args:
        text (str): the string text.

    Raises:
        Type error if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for x in ".?:":
        # print(x, text.split(c))
        text = (x + "\n\n").join(
            [line.strip(" ") for line in text.split(x)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
