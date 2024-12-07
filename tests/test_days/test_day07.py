from days.day07 import parse, part1, part2, solve

EXAMPLE_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data == {
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20],
    }


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 3749


def test_part2():
    data = parse(EXAMPLE_INPUT)
    result = part2(data)
    assert result == 11387


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
