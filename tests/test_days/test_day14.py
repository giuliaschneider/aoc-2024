from days.day14 import parse, part1, part2, solve, Position

EXAMPLE_INPUT = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data[:6] == [
        (Position(0, 4), Position(3, -3)),
        (Position(6, 3), Position(-1, -3)),
        (Position(10, 3), Position(-1, 2)),
        (Position(2, 0), Position(2, -1)),
        (Position(0, 0), Position(1, 3)),
        (Position(3, 0), Position(-2, -2)),
    ]


def test_part1():
    positions = parse(EXAMPLE_INPUT)
    result = part1(positions, 7, 11, 100)
    assert result is not None