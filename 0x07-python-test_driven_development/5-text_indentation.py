#!/usr/bin/python3
""" module: text_inden"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        return
    i = 0
    while i < len(text):
        if ord(text[i]) == 46 or ord(text[i]) == 63 or ord(text[i]) == 58:
            print(text[i])
            print("")
            i += 2
        print(text[i], end="")
        i += 1
    print('\n')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
