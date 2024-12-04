from days.day03 import parse, parse2, part1, part2, solve

EXAMPLE_INPUT = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip()

EXAMPLE_INPUT_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data == [(2, 4), (5, 5), (11, 8), (8, 5)]


def test_parse2():
    data = parse2(EXAMPLE_INPUT_2)
    assert data == [(2, 4), (8, 5)]


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 161


def test_part2():
    result = part2(EXAMPLE_INPUT_2)
    assert result == 48


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
