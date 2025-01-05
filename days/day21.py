from functools import cache
from utils.grid import Grid, Position


NUMERICAL_GRID = Grid(4, 3, [Position(0, 3)])
DIRECTIONAL_GRID = Grid(2, 3, [Position(0, 0)])

DIRECTIONS = {
    NUMERICAL_GRID.UP: "^",
    NUMERICAL_GRID.DOWN: "v",
    NUMERICAL_GRID.RIGHT: ">",
    NUMERICAL_GRID.LEFT: "<",
}


def parse(puzzle_input: str) -> any:
    """Parse the puzzle input."""
    lines = puzzle_input.split("\n")
    return lines


def path_to_directional(path):
    directional_code = ""
    for pos, next_pos in zip(path[:-1], path[1:]):
        diff = next_pos - pos
        directional_code += DIRECTIONS[diff]
    return directional_code + "A"


@cache
def numerical_to_directional(start_char, end_char):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """

    keypad = {
        "0": Position(1, 3),
        "1": Position(0, 2),
        "2": Position(1, 2),
        "3": Position(2, 2),
        "4": Position(0, 1),
        "5": Position(1, 1),
        "6": Position(2, 1),
        "7": Position(0, 0),
        "8": Position(1, 0),
        "9": Position(2, 0),
        "A": Position(2, 3),
    }

    paths = NUMERICAL_GRID.find_all_shortest_path(keypad[start_char], keypad[end_char])
    return [path_to_directional(path) for path in paths]


@cache
def directional_to_directional(start_char, end_char):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    keypad = {
        "^": Position(1, 0),
        "v": Position(1, 1),
        "<": Position(0, 1),
        ">": Position(2, 1),
        "A": Position(2, 0),
    }

    paths = DIRECTIONAL_GRID.find_all_shortest_path(
        keypad[start_char], keypad[end_char]
    )
    return [path_to_directional(path) for path in paths]


@cache
def find_min_lenght(sequence, level):
    if level == 1:
        return len(sequence)

    result = 0
    for key1, key2 in zip("A" + sequence, sequence):
        if key1 in "0123456789" or key2 in "0123456789":
            paths = numerical_to_directional(key1, key2)
        else:
            paths = directional_to_directional(key1, key2)
        lengths = set()
        for path in paths:
            lengths.add(find_min_lenght(path, level - 1))
        result += min(lengths)
    return result


def get_complexity(code: str, depth: int = 2) -> int:
    return int(code[:-1]) * find_min_lenght(code, depth)


def part1(codes) -> int:
    """Solve part 1."""
    return sum(get_complexity(code, 4) for code in codes)


def part2(codes) -> int:
    """Solve part 2."""
    return sum(get_complexity(code, 27) for code in codes)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2
