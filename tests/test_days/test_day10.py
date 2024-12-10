from days.day10 import parse, part1, part2, solve, Position

EXAMPLE_INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".strip()


def test_parse():
    grid, trailheads = parse(EXAMPLE_INPUT)
    assert grid.data[:2] == [
        ["8", "9", "0", "1", "0", "1", "2", "3"],
        ["7", "8", "1", "2", "1", "8", "7", "4"],
    ]
    assert trailheads[:2] == [
        Position(0, 2),
        Position(0, 4),
    ]


def test_part1():
    grid, trailheads = parse(EXAMPLE_INPUT)
    result = part1(grid, trailheads)
    assert result == 36


def test_part2():
    grid, trailheads = parse(EXAMPLE_INPUT)
    result = part2(grid, trailheads)
    assert result == 81


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
