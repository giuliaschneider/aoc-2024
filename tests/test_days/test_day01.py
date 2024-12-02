from days.day01 import parse, part1, part2, solve

EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data == [[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 11


def test_part2():
    data = parse(EXAMPLE_INPUT)
    result = part2(data)
    assert result == 31


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
