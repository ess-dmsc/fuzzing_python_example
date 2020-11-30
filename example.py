def csv_addition(buf):
    """
    Convert a csv string into ints and then add them.
    """
    chars = buf.split(",")
    result = 0
    for c in chars:
        result += int(c)
    return result


if __name__ == '__main__':
    # Not relevant to fuzzing
    print(csv_addition("1,2,3"))
