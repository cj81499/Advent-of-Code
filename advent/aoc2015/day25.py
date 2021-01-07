import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

FIRST_CODE = 20151125


def next_code(code):
    return (code * 252533) % 33554393


def code_at(col, row):
    code = FIRST_CODE
    x, y = 1, 1

    while not(x == col and y == row):
        code = next_code(code)
        if y == 1:
            x, y = 1, x + 1
        else:
            x, y = x + 1, y - 1
    return code


PARSE_REGEX = re.compile(r".* row (\d+), column (\d+).")


def parta(txt):
    row, col = map(int, PARSE_REGEX.match(txt).groups())
    return code_at(col, row)


def main(txt):
    print(f"parta: {parta(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)