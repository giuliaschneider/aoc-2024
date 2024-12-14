from days.day12 import parse, part1, part2, solve

EXAMPLE_INPUT = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
""".strip()


# EXAMPLE_INPUT = """
# AAAA
# BBCD
# BBCC
# EEEC
# """.strip()


def test_parse():
    grid, regions = parse(EXAMPLE_INPUT)
    assert grid is not None


def test_part1():
    grid, region = parse(EXAMPLE_INPUT)
    result = part1(grid, region)
    assert result is not None


def test_part2():
    grid, region = parse(EXAMPLE_INPUT)
    result = part2(grid, region)
    assert result == 368


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
