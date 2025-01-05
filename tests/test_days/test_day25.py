from days.day25 import parse, part1

EXAMPLE_INPUT = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".strip()


def test_parse():
    locks, keys = parse(EXAMPLE_INPUT)
    assert locks[0] == [0, 5, 3, 4, 3]
    assert keys[0] == [5, 0, 2, 1, 3]


def test_part1():
    locks, keys = parse(EXAMPLE_INPUT)
    result = part1(locks, keys)
    assert result == 3
