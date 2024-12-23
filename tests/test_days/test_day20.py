from days.day20 import parse, part1, part2, Grid

EXAMPLE_INPUT = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".strip()


def test_parse():
    obstacles, start, end, width, height = parse(EXAMPLE_INPUT)
    assert width == 15
    assert height == 15


def test_part1():
    obstacles, start, end, width, height = parse(EXAMPLE_INPUT)
    grid = Grid(height, width, obstacles)
    _, path = grid.astar_search(start, end)
    result = part1(path, 2)
    assert result == 44


def test_part2():
    obstacles, start, end, width, height = parse(EXAMPLE_INPUT)
    grid = Grid(height, width, obstacles)
    _, path = grid.astar_search(start, end)
    result = part2(path, 50)
    expected = 32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3
    assert result == expected
