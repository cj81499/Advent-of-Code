from datetime import date
from typing import Tuple

from src.intcode_interpreter import run_intcode_program
from src.util.helpers import get_puzzle


def part1(nums: Tuple[int]):
    run_intcode_program(nums, [1])


# def part2(nums: Tuple[int]):
#     run_intcode_program(nums, [5])


def main():
    txt, lines = get_puzzle(date(2019, 12, 5), "Sunny with a Chance of Asteroids")  # noqa
    nums = tuple(int(x) for x in txt.split(","))

    print("part1:")
    part1(nums)

    # print("part2:")
    # part2(nums)


if __name__ == "__main__":
    main()
