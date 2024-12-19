from days.day19 import parse, part1, part2, solve

EXAMPLE_INPUT = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".strip()


def test_parse():
    available_towels, designs = parse(EXAMPLE_INPUT)
    assert available_towels == ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    assert designs[:1] == ["brwrr"]


def test_part1():
    available_towels, designs = parse(EXAMPLE_INPUT)
    result = part1(available_towels, designs)
    assert result == 6


def test_part2():
    available_towels, designs = parse(EXAMPLE_INPUT)
    result = part2(available_towels, designs)
    assert result == 16


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
