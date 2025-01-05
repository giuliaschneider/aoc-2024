from days.day09 import parse, part1, part2, solve

EXAMPLE_INPUT = """
2333133121414131402
""".strip()


def test_parse():
    memeory_space, _, _ = parse(EXAMPLE_INPUT)
    assert memeory_space == [
        0,
        0,
        ".",
        ".",
        ".",
        1,
        1,
        1,
        ".",
        ".",
        ".",
        2,
        ".",
        ".",
        ".",
        3,
        3,
        3,
        ".",
        4,
        4,
        ".",
        5,
        5,
        5,
        5,
        ".",
        6,
        6,
        6,
        6,
        ".",
        7,
        7,
        7,
        ".",
        8,
        8,
        8,
        8,
        9,
        9,
    ]


def test_part1():
    memeory_space, free, _ = parse(EXAMPLE_INPUT)
    result = part1(memeory_space, free)
    assert result == 1928


def test_part2():
    memeory_space, free, files = parse(EXAMPLE_INPUT)
    result = part2(memeory_space, free, files)
    assert result == 2858


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
