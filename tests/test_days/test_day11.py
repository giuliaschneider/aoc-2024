from days.day11 import parse, part1

EXAMPLE_INPUT = """
125 17
""".strip()

# 0 -> 1 -> 2024 -> 20 24 -> 2 0 2 4 -> 4048 1 4048 8096 -> 48 2024 40 48 80 96


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data == [125, 17]


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 55312
