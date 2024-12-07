from days.day06 import Position, parse, part1, part2, solve

EXAMPLE_INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


def test_parse():
    grid, starting_position = parse(EXAMPLE_INPUT)
    assert grid.data[:2] == [
        [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ]
    assert starting_position == Position(6, 4)


def test_part1():
    grid, starting_position = parse(EXAMPLE_INPUT)
    result = part1(grid, starting_position)
    assert result == 41


def test_part2():
    grid, starting_position = parse(EXAMPLE_INPUT)
    result = part2(grid, starting_position)
    assert result == 6


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
