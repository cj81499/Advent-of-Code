import re
from collections.abc import Generator
from typing import Callable

import more_itertools as mi

from aoc_cj import util


def parta(txt: str, *, _get_nums: Callable[[str], Generator[int, None, None]] = util.digits) -> int:
    def calibration_value(line: str) -> int:
        nums = _get_nums(line)
        first = mi.first(nums)
        last = mi.last(nums, first)  # default to first in case there's only one number on the line
        return 10 * first + last

    return sum(map(calibration_value, txt.splitlines()))


# use a positive lookahead to allow for overlaps
NUMBER_PATTERN = re.compile(r"(?=(?P<num>\d|one|two|three|four|five|six|seven|eight|nine))")
STR_TO_INT = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def partb(txt: str) -> int:
    def get_nums(line: str) -> Generator[int, None, None]:
        yield from (
            int(s) if s.isdigit() else STR_TO_INT[s] for s in NUMBER_PATTERN.findall(line) if isinstance(s, str)
        )

    return parta(txt, _get_nums=get_nums)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
