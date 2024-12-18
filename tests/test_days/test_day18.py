from days.day18 import parse, part1, part2, solve
from utils.grid import Position

EXAMPLE_INPUT = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()


def test_parse():
    data = parse(EXAMPLE_INPUT)
    assert data[:2] == [Position(5, 4), Position(4, 2)]


def test_part1():
    obstacles = parse(EXAMPLE_INPUT)
    result = part1(7, obstacles, 12)
    assert result == 22


def test_part2():
    obstacles = parse(EXAMPLE_INPUT)
    result = part2(7, obstacles, 12)
    assert result == "6,1"


def test_solve():
    solutions = solve(EXAMPLE_INPUT)
    assert len(solutions) == 2
    assert all(s is not None for s in solutions)
