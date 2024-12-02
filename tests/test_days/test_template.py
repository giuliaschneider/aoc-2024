from days.template import parse, part1, part2, solve

EXAMPLE_INPUT = """
[Put example input here]
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data is not None


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result is not None


def test_part2():
    data = parse(EXAMPLE_INPUT)
    result = part2(data)
    assert result is not None


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
