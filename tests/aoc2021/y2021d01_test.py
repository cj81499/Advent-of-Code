import aoc_cj.aoc2021.day01 as d

EXAMPLE_INPUT = """
199
200
208
210
200
207
240
269
260
263
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 7


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 5
