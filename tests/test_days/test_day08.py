from days.day08 import parse, part1, part2, solve

EXAMPLE_INPUT = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".strip()


def test_parse():
    grid = parse(EXAMPLE_INPUT)
    positions = grid.antenna_positions
    assert positions == {
        "0": [(1, 8), (2, 5), (3, 7), (4, 4)],
        "A": [(5, 6), (8, 8), (9, 9)],
    }


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 14


def test_part2():
    data = parse(EXAMPLE_INPUT)
    result = part2(data)
    assert result == 34


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
