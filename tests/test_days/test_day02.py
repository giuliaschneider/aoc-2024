from days.day02 import parse, part1, part2, solve

EXAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    expected = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert data == expected


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 2


def test_part2():
    data = parse(EXAMPLE_INPUT)
    result = part2(data)
    assert result == 4


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
