import pytest

import aoc_cj.aoc2023.day12 as d

EXAMPLE_INPUT = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()


@pytest.mark.parametrize(
    ("example_input", "expected"),
    (
        *zip(
            EXAMPLE_INPUT.splitlines(),
            (1, 4, 1, 1, 4, 10),
        ),
        (EXAMPLE_INPUT, 21),
    ),
)
def test_part_1(example_input: str, expected: int) -> None:
    assert d.part_1(example_input) == expected


@pytest.mark.parametrize(
    ("example_input", "expected"),
    (
        (".# 1", ".#?.#?.#?.#?.# 1,1,1,1,1"),
        (EXAMPLE_INPUT.splitlines()[0], "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"),
    ),
)
def test_parse_row2(example_input: str, expected: str) -> None:
    expected = d.Row.parse(expected)
    actual = d.Row.parse2(example_input)
    assert expected == actual, f"expected {expected}. got {actual}"


@pytest.mark.parametrize(
    ("example_input", "expected"),
    (
        *zip(
            EXAMPLE_INPUT.splitlines(),
            (1, 16384, 1, 16, 2500, 506250),
        ),
        (EXAMPLE_INPUT, 525152),
    ),
)
def test_part_2(example_input: str, expected: int) -> None:
    assert d.part_2(example_input) == expected
