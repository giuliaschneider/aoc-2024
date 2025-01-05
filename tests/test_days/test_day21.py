from days.day21 import (
    parse,
    part1,
    numerical_to_directional,
    find_min_lenght,
)

EXAMPLE_INPUT = """
029A
980A
179A
456A
379A""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data == ["029A", "980A", "179A", "456A", "379A"]


def test_numerical_to_directional():
    assert numerical_to_directional("0", "2") == ["^A"]


def test_find_min_length():
    code = "029A"
    assert find_min_lenght(code, 4) == 68


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 126384
