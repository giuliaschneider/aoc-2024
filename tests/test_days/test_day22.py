from days.day22 import (
    parse,
    part1,
    part2,
    solve,
    calculate_new_secret_number,
    mix,
    prune,
)

EXAMPLE_INPUT = """
1
10
100
2024""".strip()


EXAMPLE_INPUT_2 = """
1
2
3
2024""".strip()


def test_mix():
    assert mix(15, 42) == 37


def test_prune():
    assert prune(100000000) == 16113920


def test_calculate_new_secret_number():
    assert calculate_new_secret_number(123) == 15887950


def test_parse():
    data = parse(EXAMPLE_INPUT)
    print(data)
    assert data[1] == 10


def test_part1():
    data = parse(EXAMPLE_INPUT)
    result = part1(data)
    assert result == 37327623


def test_part2():
    data = parse(EXAMPLE_INPUT_2)
    result = part2(data)
    assert result == 23


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
