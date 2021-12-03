import aoc_cj.aoc2021.day03 as d

EXAMPLE_INPUT = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 198


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 230
