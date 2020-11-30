from html.parser import HTMLParser
import os


def csv_addition(buf):
    # Convert a csv string into ints and then add them
    chars = buf.split(",")
    result = 0
    for c in chars:
        result += int(c)
    return result


if __name__ == '__main__':
    with open("initial-inputs/input1.txt") as f:
        i = f.read()
    print(csv_addition(i))
