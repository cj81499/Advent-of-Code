import path_fix
import day_10

EXAMPLE_0 = """.#..#
.....
#####
....#
...##""".splitlines()


EXAMPLE_1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.  #....####""".splitlines()

EXAMPLE_2 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""".splitlines()

EXAMPLE_3 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""".splitlines()

EXAMPLE_4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".splitlines()


def test_day_10_part1_0():
    assert day_10.part1(EXAMPLE_0) == 8


def test_day_10_part1_1():
    assert day_10.part1(EXAMPLE_1) == 33


def test_day_10_part1_2():
    assert day_10.part1(EXAMPLE_2) == 35


def test_day_10_part1_3():
    assert day_10.part1(EXAMPLE_3) == 41


def test_day_10_part1_4():
    assert day_10.part1(EXAMPLE_4) == 210


# def test_day_10_part2_0():
#     assert day_10.part2([]) is None
