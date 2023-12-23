import aoc_cj.aoc2023.day22 as d

EXAMPLE_INPUT = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 5


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 7
