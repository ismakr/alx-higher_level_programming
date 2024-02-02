#!/usr/bin/python3
""" module: text_inden"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ":.?":
            print(text[i])
            print("")
            i += 1
            if text[i] == ' ':
                i += 1
        print(text[i], end="")
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
